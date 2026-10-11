import os
from dataclasses import dataclass
from pathlib import Path

import yaml
from dotenv import load_dotenv


@dataclass
class Settings:
    claude_key: str
    model: str
    max_tokens: int
    effort: str
    log_level: str
    log_file: Path


def load_settings(root: Path) -> Settings:
    load_dotenv(root / ".env")
    with open(root / "config.yaml", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    return Settings(
        claude_key=os.environ["EVA_CLAUDE_KEY"],
        model=cfg["brain"]["model"],
        max_tokens=cfg["brain"]["max_tokens"],
        effort=cfg["brain"]["effort"],
        log_level=cfg["logging"]["level"],
        log_file=root / cfg["logging"]["dir"] / cfg["logging"]["file"],
    )