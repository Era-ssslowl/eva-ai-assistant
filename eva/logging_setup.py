import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logging(log_file: Path, level='INFO'):
    fmt = logging.Formatter("%(asctime)s %(levelname)-5s %(name)-10s %(message)s", "%H:%M:%S")
    console = logging.StreamHandler()
    console.setLevel(level)
    log_file.parent.mkdir(parents=True, exist_ok=True)   # создаёт папку logs, если её нет
    file = RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=3, encoding="utf-8")
    for h in (console, file):
        h.setFormatter(fmt)
    logging.basicConfig(level="DEBUG", handlers=[console, file])