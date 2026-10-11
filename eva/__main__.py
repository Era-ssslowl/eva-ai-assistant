import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from eva.logging_setup import setup_logging
from eva.config import load_settings
from eva.brain.claude import Claude
from eva.chat.console import run_chat



ROOT = Path(__file__).resolve().parent.parent

def main():
    settings = load_settings(ROOT)
    setup_logging(log_file=settings.log_file, level=settings.log_level)

    log = logging.getLogger(__name__)
    log.info("Логгер запущен")

    claude = Claude(api_key=settings.claude_key, model=settings.model, max_tokens=settings.max_tokens, effort=settings.effort)
    while True:
        run_chat(claude)


if __name__ == "__main__":
    main()
