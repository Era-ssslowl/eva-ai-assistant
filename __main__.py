import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging(level='INFO'):
    fmt = logging.Formatter("%(asctime)s %(levelname)-5s %(name)-10s %(message)s", "%H:%M:%S")
    console = logging.StreamHandler()
    console.setLevel(level)
    os.makedirs("logs", exist_ok=True)
    file = RotatingFileHandler("logs/eva.log", maxBytes=1_000_000, backupCount=3, encoding="utf-8")

    for h in (console, file):
        h.setFormatter(fmt)
    logging.basicConfig(level="DEBUG", handlers=[console, file])

if __name__ == "__main__":
    setup_logging()
    log = logging.getLogger(__name__)
    log.info("Тест логгера")
