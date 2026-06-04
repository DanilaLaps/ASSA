from __future__ import annotations

from collections import defaultdict
from typing import Any

from .utils import date_distance_days, percent_change, parse_date, safe_div


def detect_trends(
    summaries: list[dict[str, Any]],
    history_summaries: list[dict[str, Any]],
    snapshot_date: str,
) -> list[dict[str, Any]]:
    history_by_key: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in history_summaries:
        if item.get("group_key"):
            history_by_key[str(item["group_key"])].append(item)

    for key_items in history_by_key.values():
        key_items.sort(key=lambda item: item.get("snapshot_date", ""))

    enriched: list[dict[str, Any]] = []
    for summary in summaries:
        item = dict(summary)
        history = history_by_key.get(str(summary.get("group_key")), [])
        if not history:
            item["has_history"] = False
            item["history_depth_days"] = 0
            item["weekly_growth_percent"] = 0.0
            item["monthly_growth_percent"] = 0.0
            item["growth_by_one_app_share"] = 0.0
            item["previous_total_daily_installs"] = 0
            enriched.append(item)
            continue
        latest = latest_before(history, snapshot_date)
        if latest is None:
            item["has_history"] = False
            item["history_depth_days"] = 0
            item["weekly_growth_percent"] = 0.0
            item["monthly_growth_percent"] = 0.0
            item["growth_by_one_app_share"] = 0.0
            item["previous_total_daily_installs"] = 0
            enriched.append(item)
            continue
        weekly = nearest_before(history, snapshot_date, target_days=7)
        monthly = nearest_before(history, snapshot_date, target_days=30)
        baseline = weekly or latest
        item["has_history"] = bool(history)
        item["history_depth_days"] = history_depth_days(history, snapshot_date)
        item["weekly_growth_percent"] = round(
            percent_change(float(item.get("total_daily_installs", 0)), float((baseline or {}).get("total_daily_installs", 0))),
            2,
        )
        item["monthly_growth_percent"] = round(
            percent_change(float(item.get("total_daily_installs", 0)), float((monthly or baseline or {}).get("total_daily_installs", 0))),
            2,
        )
        item["growth_by_one_app_share"] = round(growth_by_one_app_share(item, baseline), 4)
        item["previous_total_daily_installs"] = int((baseline or {}).get("total_daily_installs", 0))
        enriched.append(item)
    return enriched


def latest_before(history: list[dict[str, Any]], snapshot_date: str) -> dict[str, Any] | None:
    candidates = [item for item in history if str(item.get("snapshot_date", "")) < snapshot_date]
    return candidates[-1] if candidates else None


def nearest_before(history: list[dict[str, Any]], snapshot_date: str, target_days: int) -> dict[str, Any] | None:
    candidates: list[tuple[int, dict[str, Any]]] = []
    for item in history:
        item_date = item.get("snapshot_date")
        if not item_date or str(item_date) >= snapshot_date:
            continue
        distance = date_distance_days(snapshot_date, str(item_date))
        if distance is None:
            continue
        candidates.append((abs(distance - target_days), item))
    if not candidates:
        return None
    candidates.sort(key=lambda pair: pair[0])
    return candidates[0][1]


def history_depth_days(history: list[dict[str, Any]], snapshot_date: str) -> int:
    dates = [parse_date(item.get("snapshot_date")) for item in history]
    dates = [date for date in dates if date is not None and date.isoformat() < snapshot_date]
    current = parse_date(snapshot_date)
    if not dates or current is None:
        return 0
    return (current - min(dates)).days


def growth_by_one_app_share(current: dict[str, Any], previous: dict[str, Any] | None) -> float:
    if not previous:
        return 0.0
    previous_apps = {
        str(app.get("app_id")): int(app.get("downloads_daily", 0))
        for app in previous.get("top_apps", [])
    }
    positive_growths: list[int] = []
    for app in current.get("top_apps", []):
        app_id = str(app.get("app_id"))
        current_daily = int(app.get("downloads_daily", 0))
        delta = current_daily - previous_apps.get(app_id, 0)
        if delta > 0:
            positive_growths.append(delta)
    if not positive_growths:
        return 0.0
    return safe_div(max(positive_growths), sum(positive_growths))
