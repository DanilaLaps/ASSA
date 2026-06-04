from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_config(path: str | Path = "config.yaml") -> tuple[dict[str, Any], Path]:
    config_path = Path(path).resolve()
    text = config_path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text)
    except ModuleNotFoundError:
        data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError(f"Config must be a mapping: {config_path}")
    return data, config_path.parent


def resolve_path(config_dir: Path, value: str | Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return config_dir / path
