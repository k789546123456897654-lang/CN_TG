import json

from openai import OpenAI

from config import Config
from app.ai.prompts import SYSTEM_PROMPT
from app.core.logger import logger


class AIAnalyzer:

    def __init__(self):

        self.client = None

        if Config.OPENAI_API_KEY:

            self.client = OpenAI(
                api_key=Config.OPENAI_API_KEY
            )

    def analyze(self, text: str) -> dict:

        if not self.client:

            logger.warning("OpenAI отключен.")

            return {
                "summary": text,
                "category": "other",
                "priority": "medium",
                "manager_required": True,
                "reply": "",
            }

        try:

            response = self.client.responses.create(

                model=Config.OPENAI_MODEL,

                input=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT,
                    },
                    {
                        "role": "user",
                        "content": text,
                    },
                ],

                text={
                    "format": {
                        "type": "json_object"
                    }
                }

            )

            content = response.output_text

            result = json.loads(content)

            return {

                "summary": result.get(
                    "summary",
                    "",
                ),

                "category": result.get(
                    "category",
                    "other",
                ),

                "priority": result.get(
                    "priority",
                    "medium",
                ),

                "manager_required": result.get(
                    "manager_required",
                    True,
                ),

                "reply": result.get(
                    "reply",
                    "",
                ),
            }

        except Exception:

            logger.exception(
                "Ошибка OpenAI"
            )

            return {
                "summary": text,
                "category": "other",
                "priority": "medium",
                "manager_required": True,
                "reply": "",
            }