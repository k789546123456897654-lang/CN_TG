from app.core.logger import logger


class NotificationService:

    def notify_manager(
        self,
        manager,
        message,
        analysis,
    ):

        logger.info("================================")

        logger.info(
            f"Менеджер: {manager.name if hasattr(manager,'name') else manager['name']}"
        )

        logger.info(
            f"Клиент: {message.client_name}"
        )

        logger.info(
            f"Категория: {analysis['category']}"
        )

        logger.info(
            f"Приоритет: {analysis['priority']}"
        )

        logger.info(
            f"Сообщение:\n{message.text}"
        )

        logger.info(
            f"Ответ AI:\n{analysis['reply']}"
        )

        logger.info("================================")