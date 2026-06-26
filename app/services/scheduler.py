import asyncio

from app.core.logger import logger
from app.services.reminder_service import ReminderService


class Scheduler:

    def __init__(self):

        self.reminder = ReminderService()

    async def start(self):

        logger.info(
            "Scheduler запущен."
        )

        while True:

            try:

                self.reminder.check()

            except Exception as e:

                logger.exception(e)

            await asyncio.sleep(60)