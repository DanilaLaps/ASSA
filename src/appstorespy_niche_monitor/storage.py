from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from .config import resolve_path
from .utils import slugify


def storage_paths(config: dict[str, Any], config_dir: Path) -> dict[str, Path]:
    storage = config.get("storage", {})
    return {
        "raw_dir": resolve_path(config_dir, storage.get("raw_dir", "data/raw")),
        "processed_dir": resolve_path(config_dir, storage.get("processed_dir", "data/processed")),
        "history_dir": resolve_path(config_dir, storage.get("history_dir", "data/history")),
        "sent_alerts_path": resolve_path(config_dir, storage.get("sent_alerts_path", "data/sent_alerts.json")),
        "feedback_path": resolve_path(config_dir, storage.get("feedback_path", "data/feedback.json")),
        "reports_alerts_dir": resolve_path(config_dir, storage.get("reports_alerts_dir", "reports/alerts")),
        "reports_weekly_dir": resolve_path(config_dir, storage.get("reports_weekly_dir", "reports/weekly")),
    }


def ensure_storage(config: dict[str, Any], config_dir: Path) -> dict[str, Path]:
    paths = storage_paths(config, config_dir)
    for key, path in paths.items():
        if key.endswith("_dir"):
            path.mkdir(parents=True, exist_ok=True)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
    if not paths["sent_alerts_path"].exists():
        write_json(paths["sent_alerts_path"], {})
    if not paths["feedback_path"].exists():
        write_json(paths["feedback_path"], [])
    return paths


def read_json(path: str | Path, default: Any = None) -> Any:
    json_path = Path(path)
    if not json_path.exists():
        return default
    return json.loads(json_path.read_text(encoding="utf-8"))


def write_json(path: str | Path, data: Any) -> None:
    json_path = Path(path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = json_path.with_suffix(json_path.suffix + ".tmp")
    temp_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    temp_path.replace(json_path)


def write_csv(path: str | Path, rows: list[dict[str, Any]]) -> None:
    csv_path = Path(path)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        csv_path.write_text("", encoding="utf-8")
        return
    fieldnames = sorted({key for row in rows for key in row.keys() if key != "top_apps"})
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def save_raw(paths: dict[str, Path], raw_records: list[dict[str, Any]], snapshot_date: str) -> Path:
    path = paths["raw_dir"] / f"{snapshot_date}_raw.json"
    write_json(path, raw_records)
    return path


def save_processed(paths: dict[str, Path], name: str, rows: list[dict[str, Any]], snapshot_date: str) -> tuple[Path, Path]:
    json_path = paths["processed_dir"] / f"{snapshot_date}_{name}.json"
    csv_path = paths["processed_dir"] / f"{snapshot_date}_{name}.csv"
    write_json(json_path, rows)
    write_csv(csv_path, rows)
    return json_path, csv_path


def load_history_summaries(paths: dict[str, Path]) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for path in sorted(paths["history_dir"].glob("*_summaries.json")):
        data = read_json(path, [])
        if isinstance(data, list):
            summaries.extend(item for item in data if isinstance(item, dict))
    return summaries


def save_history_summaries(paths: dict[str, Path], summaries: list[dict[str, Any]], snapshot_date: str) -> Path:
    path = paths["history_dir"] / f"{snapshot_date}_summaries.json"
    write_json(path, summaries)
    return path


def write_alert_report(paths: dict[str, Path], alert: dict[str, Any], markdown: str) -> Path:
    alert_id = slugify(alert.get("alert_id", "alert"), max_length=120)
    path = paths["reports_alerts_dir"] / f"{alert_id}.md"
    path.write_text(markdown, encoding="utf-8")
    return path
