from __future__ import annotations

import datetime as dt
from typing import Any

from .utils import parse_date, slugify


def filter_alerts(
    summaries: list[dict[str, Any]],
    config: dict[str, Any],
    sent_alerts: dict[str, Any],
    snapshot_date: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    alerts: list[dict[str, Any]] = []
    watch: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    limits = config.get("alert_limits", {})
    max_alerts = int(limits.get("max_alerts_per_run", 3))
    max_watch = int(limits.get("max_watch_items_per_digest", 10))
    max_country = int(limits.get("max_alerts_per_country_per_run", 1))
    country_counts: dict[str, int] = {}

    ranked = sorted(summaries, key=lambda item: float(item.get("opportunity_score", 0.0)), reverse=True)
    for summary in ranked:
        candidate = dict(summary)
        passed, reasons = should_alert(candidate, config, sent_alerts, snapshot_date)
        candidate["alert_id"] = build_alert_id(candidate, snapshot_date)
        candidate["alert_filter_reasons"] = reasons
        if passed and len(alerts) < max_alerts and country_counts.get(str(candidate.get("country")), 0) < max_country:
            candidate["alert_tier"] = "TEST"
            alerts.append(candidate)
            country_counts[str(candidate.get("country"))] = country_counts.get(str(candidate.get("country")), 0) + 1
        elif is_watch_candidate(candidate, config) and len(watch) < max_watch:
            candidate["alert_tier"] = "WATCH"
            watch.append(candidate)
        else:
            candidate["alert_tier"] = "REJECTED"
            rejected.append(candidate)
    return alerts, watch, rejected


def should_alert(
    row: dict[str, Any],
    config: dict[str, Any],
    sent_alerts: dict[str, Any],
    snapshot_date: str,
) -> tuple[bool, list[str]]:
    rules = config.get("alert_rules", {})
    reasons: list[str] = []
    if not row.get("has_history"):
        reasons.append("baseline_only")
    if float(row.get("opportunity_score", 0.0)) < float(rules.get("min_opportunity_score", 75)):
        reasons.append("low_score")
    if int(row.get("total_daily_installs", 0)) < int(rules.get("min_total_daily_installs", 50000)):
        reasons.append("low_demand")
    if float(row.get("weekly_growth_percent", 0.0)) < float(rules.get("min_weekly_growth_percent", 25)):
        reasons.append("low_growth")
    if int(row.get("app_count", 0)) < int(rules.get("min_apps_in_niche", 2)):
        reasons.append("too_few_apps")
    if int(row.get("successful_new_apps_count", 0)) < int(rules.get("min_successful_new_apps", 1)):
        reasons.append("no_successful_new_apps")
    if float(row.get("giant_developer_share", 0.0)) >= float(rules.get("max_giant_developer_share", 0.7)):
        reasons.append("giant_dominated")
    if float(row.get("top_app_share", 0.0)) > float(rules.get("max_top_app_share", 0.75)):
        reasons.append("top_app_dominance")
    if float(row.get("growth_by_one_app_share", 0.0)) > float(rules.get("max_growth_by_one_app_share", 0.6)):
        reasons.append("one_app_growth")
    if float(row.get("data_quality_score", 0.0)) < float(rules.get("min_data_quality_score", 70)):
        reasons.append("weak_data_quality")
    if was_sent_recently(alert_key(row), sent_alerts, int(rules.get("cooldown_days", 7)), snapshot_date):
        reasons.append("cooldown")
    return not reasons, reasons or ["passed"]


def is_watch_candidate(row: dict[str, Any], config: dict[str, Any]) -> bool:
    rules = config.get("alert_rules", {})
    score_ok = float(row.get("opportunity_score", 0.0)) >= float(rules.get("min_opportunity_score", 75)) - 15
    demand_ok = int(row.get("total_daily_installs", 0)) >= int(rules.get("min_total_daily_installs", 50000)) * 0.5
    return score_ok and demand_ok


def alert_key(row: dict[str, Any]) -> str:
    return str(row.get("group_key", ""))


def build_alert_id(row: dict[str, Any], snapshot_date: str) -> str:
    country = slugify(row.get("country", "country"), max_length=12)
    niche = slugify(
        "_".join(
            str(row.get(field, ""))
            for field in ("niche", "core_mechanic", "theme", "meta", "audience")
            if row.get(field)
        )
    )
    return f"{snapshot_date}_{country}_{niche}"


def was_sent_recently(key: str, sent_alerts: dict[str, Any], cooldown_days: int, snapshot_date: str) -> bool:
    item = sent_alerts.get(key)
    if not item:
        return False
    last_sent = parse_date(item.get("last_sent_at") if isinstance(item, dict) else item)
    current = parse_date(snapshot_date)
    if last_sent is None or current is None:
        return False
    return (current - last_sent).days < cooldown_days


def mark_sent(sent_alerts: dict[str, Any], alerts: list[dict[str, Any]], snapshot_date: str) -> dict[str, Any]:
    updated = dict(sent_alerts)
    now = dt.datetime.now(dt.UTC).isoformat()
    for alert in alerts:
        updated[alert_key(alert)] = {
            "last_sent_at": snapshot_date,
            "alert_id": alert.get("alert_id"),
            "opportunity_score": alert.get("opportunity_score"),
            "updated_at": now,
        }
    return updated
