from dotenv import load_dotenv
import os

load_dotenv()


class Config:

    API_ID = int(os.getenv("API_ID"))

    API_HASH = os.getenv("API_HASH")

    SESSION_NAME = os.getenv(
        "SESSION_NAME",
        "cnbridge"
    )

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY",
        ""
    )

    OPENAI_MODEL = os.getenv(
        "OPENAI_MODEL",
        "gpt-5"
    )

    DATABASE_PATH = os.getenv(
        "DATABASE_PATH",
        "cnbridge.db"
    )

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    LOG_FILE = os.getenv(
        "LOG_FILE",
        "logs/cnbridge.log"
    )

    FIRST_REMINDER_MIN = int(
        os.getenv(
            "FIRST_REMINDER_MIN",
            "15"
        )
    )

    SECOND_REMINDER_MIN = int(
        os.getenv(
            "SECOND_REMINDER_MIN",
            "30"
        )
    )

    THIRD_REMINDER_MIN = int(
        os.getenv(
            "THIRD_REMINDER_MIN",
            "60"
        )
    )