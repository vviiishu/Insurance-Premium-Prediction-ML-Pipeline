import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOGS_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def get_logger(name: str = __name__) -> logging.Logger:
    """Return a configured logger instance."""
    return logging.getLogger(name)


if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.info("Logging has started")
