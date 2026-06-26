from app.database.repository import Repository


class ManagerService:

    def __init__(self):

        self.repository = Repository()

        self.category_map = {
            "drones": "Константин",
            "logistics": "Сергей",
            "customs": "Алексей",
            "documents": "Юлия",
            "certification": "Юлия",
            "payment": "Бухгалтерия",
            "supplier": "Константин",
            "order": "Константин",
            "complaint": "Константин",
            "other": "Константин",
        }

    def get_manager(self, analysis: dict):

        category = analysis.get(
            "category",
            "other",
        )

        managers = self.repository.get_active_managers()

        if managers:

            for manager in managers:

                if manager.name == self.category_map.get(
                    category,
                    "Константин",
                ):

                    return manager

            return managers[0]

        return {
            "id": 0,
            "name": self.category_map.get(
                category,
                "Константин",
            ),
            "telegram_id": 0,
        }