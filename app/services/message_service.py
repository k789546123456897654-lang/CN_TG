from app.database.repository import MessageRepository


class ManagerService:

    def __init__(self):

        self.repository = MessageRepository()

        self.managers = {
            "drones": "Константин",
            "logistics": "Сергей",
            "customs": "Алексей",
            "documents": "Юлия",
            "payment": "Бухгалтерия",
            "supplier": "Константин",
            "other": "Константин"
        }

    def get_manager(
        self,
        message,
        analysis: dict
    ) -> str:

        # Если менеджер уже закреплен за клиентом —
        # в будущем будем возвращать его отсюда.

        category = analysis.get("category", "other")

        return self.managers.get(
            category,
            "Константин"
        )