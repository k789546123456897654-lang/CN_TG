from datetime import datetime, timedelta

from app.core.logger import logger
from app.database.repository import Repository
from config import Config


class ReminderService:

    def __init__(self):

        self.repository = Repository()

    def check(self):

        messages = self.repository.get_unanswered_messages()

        now = datetime.utcnow()

        for message in messages:

            if message.reminder_sent:
                continue

            delta = now - message.created_at

            minutes = delta.total_seconds() / 60

            if minutes >= Config.FIRST_REMINDER_MIN:

                logger.info(
                    f"Напоминание для сообщения #{message.id}"
                )

                self.repository.mark_reminder_sent(
                    message.id
                )