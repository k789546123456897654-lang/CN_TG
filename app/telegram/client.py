from telethon import TelegramClient, events

from config import Config
from app.core.logger import logger
from app.database.repository import Repository
from app.telegram.router import MessageRouter


class TelegramService:

    def __init__(self):

        self.repository = Repository()
        self.router = MessageRouter()

        self.client = TelegramClient(
            Config.SESSION_NAME,
            Config.API_ID,
            Config.API_HASH,
        )

    async def start(self):

        logger.info("=" * 60)
        logger.info("Подключение к Telegram...")
        logger.info("=" * 60)

        await self.client.connect()

        if not await self.client.is_user_authorized():
            raise RuntimeError(
                "Сессия не авторизована. Запустите login_qr.py"
            )

        me = await self.client.get_me()

        logger.info(
            f"Авторизован как {me.first_name} ({me.id})"
        )

        self.client.add_event_handler(
            self.on_new_message,
            events.NewMessage(incoming=True),
        )

        logger.info("Мониторинг сообщений запущен.")

        await self.client.run_until_disconnected()

    async def stop(self):
        await self.client.disconnect()

    async def on_new_message(self, event):

        try:

            if event.chat_id is None:
                return

            watched_chat = self.repository.get_chat(
                event.chat_id
            )

            if watched_chat is None:
                return

            logger.info(
                f"Новое сообщение: chat={event.chat_id}"
            )

            await self.router.process(event)

        except Exception:
            logger.exception("Ошибка обработки сообщения")