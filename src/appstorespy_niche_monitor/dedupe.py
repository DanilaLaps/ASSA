from __future__ import annotations

import hashlib
from typing import Any


def stable_sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]


def make_dedupe_key(
    normalized_niche: str,
    top_app_ids: list[str],
    window: str = "last_180d",
) -> str:
    stable_apps = ",".join(sorted(str(app_id) for app_id in top_app_ids[:3] if app_id))
    raw = f"{normalized_niche}|{stable_apps}|{window}"
    return stable_sha256(raw)


def make_alert_instance_id(snapshot_date: str, dedupe_key: str) -> str:
    return f"{snapshot_date}:{dedupe_key}"


def top_app_ids(row: dict[str, Any], limit: int = 3) -> list[str]:
    ids = [
        str(app.get("app_id") or app.get("bundle") or app.get("name", ""))
        for app in row.get("top_apps", [])
        if app.get("app_id") or app.get("bundle") or app.get("name")
    ]
    return sorted(ids)[:limit]
