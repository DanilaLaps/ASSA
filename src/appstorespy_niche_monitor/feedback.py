from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
from typing import Any


def read_feedback(path: str | Path) -> list[dict[str, Any]]:
    feedback_path = Path(path)
    if not feedback_path.exists():
        return []
    data = json.loads(feedback_path.read_text(encoding="utf-8"))
    return data if isinstance(data, list) else []


def write_feedback(path: str | Path, records: list[dict[str, Any]]) -> None:
    feedback_path = Path(path)
    feedback_path.parent.mkdir(parents=True, exist_ok=True)
    feedback_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")


def add_feedback(
    path: str | Path,
    config: dict[str, Any],
    *,
    alert_id: str,
    status: str,
    reason: str,
    notes: str = "",
    reviewed_at: str | None = None,
) -> dict[str, Any]:
    feedback_cfg = config.get("feedback", {})
    if status not in feedback_cfg.get("allowed_statuses", []):
        raise ValueError(f"Unsupported feedback status: {status}")
    if reason not in feedback_cfg.get("allowed_reasons", []):
        raise ValueError(f"Unsupported feedback reason: {reason}")
    records = read_feedback(path)
    record = {
        "alert_id": alert_id,
        "status": status,
        "reason": reason,
        "notes": notes,
        "reviewed_at": reviewed_at or dt.datetime.now(dt.UTC).date().isoformat(),
    }
    records = [item for item in records if item.get("alert_id") != alert_id]
    records.append(record)
    write_feedback(path, records)
    return record


def feedback_summary(records: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for record in records:
        status = str(record.get("status", "unknown"))
        counts[status] = counts.get(status, 0) + 1
    return counts
