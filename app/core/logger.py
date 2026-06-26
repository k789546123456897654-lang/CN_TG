import logging
import os

from config import Config


os.makedirs("logs", exist_ok=True)


logger = logging.getLogger("CNBridgeAI")
logger.setLevel(Config.LOG_LEVEL)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

console = logging.StreamHandler()
console.setFormatter(formatter)

file = logging.FileHandler(
    Config.LOG_FILE,
    encoding="utf-8"
)

file.setFormatter(formatter)

logger.handlers.clear()

logger.addHandler(console)
logger.addHandler(file)