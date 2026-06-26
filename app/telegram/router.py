from app.ai.analyzer import AIAnalyzer
from app.core.logger import logger
from app.database.repository import Repository
from app.services.manager_service import ManagerService
from app.services.notification_service import NotificationService


class MessageRouter:

    def __init__(self):

        self.repository = Repository()

        self.ai = AIAnalyzer()

        self.manager_service = ManagerService()

        self.notification_service = NotificationService()

    async def process(self, event):

        logger.info("Новое сообщение")

        sender = await event.get_sender()

        client_name = ""

        if sender:

            if sender.first_name:

                client_name = sender.first_name

            if sender.last_name:

                client_name += f" {sender.last_name}"

            client_name = client_name.strip()

        message = self.repository.save_message(

            telegram_message_id=event.id,

            telegram_chat_id=event.chat_id,

            telegram_user_id=event.sender_id,

            client_name=client_name,

            text=event.raw_text,

        )

        analysis = self.ai.analyze(
            event.raw_text
        )

        self.repository.update_ai_result(

            message_id=message.id,

            summary=analysis["summary"],

            category=analysis["category"],

            priority=analysis["priority"],

            suggested_reply=analysis["reply"],

            manager_required=analysis["manager_required"],

        )

        manager = self.manager_service.get_manager(
            analysis
        )

        if analysis["manager_required"]:

            self.notification_service.notify_manager(

                manager=manager,

                message=message,

                analysis=analysis,

            )

        logger.info("Обработка завершена")