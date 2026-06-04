from __future__ import annotations

import datetime as dt
from typing import Any

from .candidate_generator import generate_candidates
from .dedupe import make_alert_instance_id, make_dedupe_key, top_app_ids
from .utils import parse_date, slugify


def apply_cooldown_and_alert_limits(
    candidates: list[dict[str, Any]],
    config: dict[str, Any],
    sent_alerts: dict[str, Any],
    snapshot_date: str,
) -> list[dict[str, Any]]:
    limits = config.get("alert_limits", {})
    max_alerts = int(limits.get("max_alerts_per_run", 3))
    cooldown_days = int(limits.get("cooldown_days", config.get("alert_rules", {}).get("cooldown_days", 7)))
    sent_count = 0
    enriched: list[dict[str, Any]] = []
    for candidate in sorted(candidates, key=lambda item: float(item.get("opportunity_score", 0.0)), reverse=True):
        item = dict(candidate)
        item.setdefault("send_regular_alert", False)
        item.setdefault("alert_filter_reasons", [])
        if item.get("exclude_from_cooldown"):
            item["send_regular_alert"] = False
            item["alert_filter_reasons"] = append_reason(item.get("alert_filter_reasons", []), "excluded_from_cooldown")
        elif item.get("status") == "ALERT":
            cooldown = was_sent_recently(
                str(item.get("dedupe_key")),
                str(item.get("normalized_niche")),
                sent_alerts,
                cooldown_days,
                snapshot_date,
            )
            if cooldown:
                item["send_regular_alert"] = False
                item["alert_filter_reasons"] = append_reason(item.get("alert_filter_reasons", []), "cooldown")
            elif sent_count >= max_alerts:
                item["send_regular_alert"] = False
                item["alert_filter_reasons"] = append_reason(item.get("alert_filter_reasons", []), "alert_limit")
            else:
                item["send_regular_alert"] = True
                item["alert_filter_reasons"] = append_reason(item.get("alert_filter_reasons", []), "passed")
                sent_count += 1
        else:
            item["send_regular_alert"] = False
        enriched.append(item)
    return sort_candidates(enriched)


def split_candidates(
    candidates: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    alerts = [item for item in candidates if item.get("status") == "ALERT"]
    watch = [item for item in candidates if item.get("status") in {"WATCH", "SINGLE_APP_WATCH"}]
    near_misses = [item for item in candidates if item.get("status") == "NEAR_MISS"]
    rejected = [item for item in candidates if item.get("status") == "REJECT"]
    urgent_alerts = [item for item in alerts if item.get("send_regular_alert")]
    return urgent_alerts, watch, near_misses, rejected, alerts


def sort_candidates(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    status_rank = {"ALERT": 4, "SINGLE_APP_WATCH": 3, "NEAR_MISS": 2, "WATCH": 1, "REJECT": 0}
    return sorted(
        candidates,
        key=lambda item: (
            -status_rank.get(str(item.get("status")), 0),
            -float(item.get("opportunity_score", 0.0)),
            str(item.get("normalized_niche", "")),
        ),
    )


def append_reason(reasons: Any, reason: str) -> list[str]:
    values = list(reasons) if isinstance(reasons, list) else []
    if reason not in values:
        values.append(reason)
    return values


def should_alert(
    row: dict[str, Any],
    config: dict[str, Any],
    sent_alerts: dict[str, Any],
    snapshot_date: str,
) -> tuple[bool, list[str]]:
    candidate = generate_candidates([row], config, snapshot_date)[0]
    filtered = apply_cooldown_and_alert_limits([candidate], config, sent_alerts, snapshot_date)[0]
    reasons = filtered.get("failed_alert_conditions", []) or filtered.get("alert_filter_reasons", [])
    return bool(filtered.get("send_regular_alert")), reasons or ["passed"]


def filter_alerts(
    summaries: list[dict[str, Any]],
    config: dict[str, Any],
    sent_alerts: dict[str, Any],
    snapshot_date: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    candidates = generate_candidates(summaries, config, snapshot_date)
    candidates = apply_cooldown_and_alert_limits(candidates, config, sent_alerts, snapshot_date)
    urgent_alerts, watch, near_misses, rejected, _alerts = split_candidates(candidates)
    return urgent_alerts, watch + near_misses, rejected


def alert_key(row: dict[str, Any]) -> str:
    return str(row.get("dedupe_key") or make_dedupe_key(normalized_niche(row), top_app_ids(row), release_date_window(row)))


def build_alert_id(row: dict[str, Any], snapshot_date: str) -> str:
    return str(row.get("alert_instance_id") or make_alert_instance_id(snapshot_date, alert_key(row)))


def normalized_niche(row: dict[str, Any]) -> str:
    value = row.get("normalized_niche")
    if value:
        return str(value)
    return slugify(
        "_".join(
            str(row.get(field, ""))
            for field in ("niche", "core_mechanic", "theme", "meta")
            if row.get(field)
        )
    )


def release_date_window(row: dict[str, Any]) -> str:
    return str(row.get("release_date_window") or "last_180d")


def was_sent_recently(
    dedupe_key: str,
    normalized_niche_value: str,
    sent_alerts: dict[str, Any],
    cooldown_days: int,
    snapshot_date: str,
) -> bool:
    current = parse_date(snapshot_date)
    if current is None:
        return False
    for key, item in sent_alerts.items():
        if not isinstance(item, dict):
            item = {"last_sent_at": item}
        if key != dedupe_key and item.get("normalized_niche") != normalized_niche_value:
            continue
        last_sent = parse_date(item.get("last_sent_at"))
        if last_sent is not None and (current - last_sent).days < cooldown_days:
            return True
    return False


def mark_sent(sent_alerts: dict[str, Any], alerts: list[dict[str, Any]], snapshot_date: str) -> dict[str, Any]:
    updated = dict(sent_alerts)
    now = dt.datetime.now(dt.UTC).isoformat()
    for alert in alerts:
        if alert.get("exclude_from_cooldown") or not alert.get("send_regular_alert", True):
            continue
        key = str(alert.get("dedupe_key") or alert_key(alert))
        updated[key] = {
            "normalized_niche": alert.get("normalized_niche"),
            "last_sent_at": now if "T" in now else snapshot_date,
            "last_alert_instance_id": alert.get("alert_instance_id") or build_alert_id(alert, snapshot_date),
            "top_app_ids": top_app_ids(alert),
            "last_status": alert.get("status", "ALERT"),
            "opportunity_score": alert.get("opportunity_score"),
            "updated_at": now,
        }
    return updated
