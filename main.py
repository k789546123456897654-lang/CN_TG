import asyncio

from app.core.logger import logger
from app.database.db import init_db
from app.services.scheduler import Scheduler
from app.telegram.client import TelegramService
from config import Config


async def main():

    logger.info("=" * 60)
    logger.info("CNBridge AI")
    logger.info("Инициализация...")
    logger.info("=" * 60)

    init_db()

    print("API_ID =", Config.API_ID)
    print("API_HASH =", Config.API_HASH)

    telegram = TelegramService()

    scheduler = Scheduler()

    telegram_task = asyncio.create_task(
        telegram.start()
    )

    scheduler_task = asyncio.create_task(
        scheduler.start()
    )

    await asyncio.gather(
        telegram_task,
        scheduler_task,
    )


if __name__ == "__main__":

    try:

        asyncio.run(main())

    except KeyboardInterrupt:

        logger.info("Завершение работы...")