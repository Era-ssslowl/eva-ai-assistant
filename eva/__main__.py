from eva.core.config import load_settings
from eva.brain.claude import Claude 

import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def setup_logging(log_file: Path, level='INFO'):
    fmt = logging.Formatter("%(asctime)s %(levelname)-5s %(name)-10s %(message)s", "%H:%M:%S")
    console = logging.StreamHandler()
    console.setLevel(level)
    log_file.parent.mkdir(parents=True, exist_ok=True)   # создаёт папку logs, если её нет
    file = RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=3, encoding="utf-8")
    for h in (console, file):
        h.setFormatter(fmt)
    logging.basicConfig(level="DEBUG", handlers=[console, file])

if __name__ == "__main__":
    settings = load_settings(ROOT)
    setup_logging(log_file=settings.log_file, level=settings.log_level)
    log = logging.getLogger(__name__)
    log.info("Логгер запущен")


    claude = Claude(api_key=settings.claude_key, model=settings.model, max_tokens=settings.max_tokens, effort=settings.effort)
    claude.ask('привет, клод')
