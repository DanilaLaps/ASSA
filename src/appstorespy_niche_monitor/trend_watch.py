from __future__ import annotations

import datetime as dt
from typing import Any

from .alert_filter import cooldown_failure_reasons
from .alert_ranker import int_metric, ratio_metric, score_100
from .dedupe import top_app_ids
from .utils import clamp, log_score


DEFAULT_TREND_WATCH_RULES = {
    "enabled": True,
    "max_items_per_run": 1,
    "cooldown_days": 7,
    "allowed_statuses": ["ALERT", "WATCH", "NEAR_MISS"],
    "exclude_regular_alerts": True,
    "min_weekly_growth_percent": 10.0,
    "min_monthly_growth_percent": 20.0,
    "min_history_depth_days": 2,
    "min_total_daily_installs": 5000,
    "min_app_count": 3,
    "min_successful_new_apps": 1,
    "min_data_quality_score": 60.0,
    "min_classification_confidence_avg": 0.50,
    "max_growth_by_one_app_share": 0.75,
    "max_top_app_share": 0.80,
    "block_unknown_pattern_if_low_confidence": True,
    "blocked_risk_tags": ["severe_paid_spike", "low_data_quality"],
}


def trend_watch_rules(config: dict[str, Any]) -> dict[str, Any]:
    configured = config.get("trend_watch", {})
    if not isinstance(configured, dict):
        configured = {}
    return {**DEFAULT_TREND_WATCH_RULES, **configured}


def select_trend_watch(
    candidates: list[dict[str, Any]],
    config: dict[str, Any],
    sent_trend_watch: dict[str, Any],
    snapshot_date: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rules = trend_watch_rules(config)
    enriched = [with_trend_watch_defaults(candidate, config) for candidate in candidates]
    if not bool(rules.get("enabled", True)):
        return enriched, []

    max_items = int(rules.get("max_items_per_run", 1))
    if max_items <= 0:
        return enriched, []

    eligible: list[dict[str, Any]] = []
    cooldown_days = int(rules.get("cooldown_days", 7))
    for item in enriched:
        failures = trend_watch_filter_failures(item, rules)
        cooldown_failures: list[str] = []
        if not failures:
            cooldown_failures = trend_watch_cooldown_failures(item, sent_trend_watch, cooldown_days, snapshot_date)
            failures.extend(cooldown_failures)
        item["trend_watch_failures"] = sorted(set(str(failure) for failure in failures))
        if cooldown_failures:
            add_trend_watch_reasons(item, ["trend_watch_cooldown_checked"])
        if failures:
            continue
        eligible.append(item)

    eligible.sort(
        key=lambda item: (
            -float(item.get("trend_watch_score", 0.0)),
            -float(item.get("weekly_growth_percent", 0.0)),
            -float(item.get("monthly_growth_percent", 0.0)),
            -float(item.get("total_daily_installs", 0.0)),
            str(item.get("normalized_niche", "")),
            str(item.get("candidate_id", "")),
        )
    )
    selected = eligible[:max_items]
    selected_ids = {str(item.get("candidate_id")) for item in selected}
    for rank, item in enumerate(selected, start=1):
        item["send_trend_watch"] = True
        item["trend_watch_stage"] = "TREND_WATCH"
        item["trend_watch_rank"] = rank
        item["trend_watch_delivery_channel"] = "trend_watch"
        item["telegram_delivery_channel"] = "trend_watch"
        item["trend_watch_instance_id"] = make_trend_watch_instance_id(snapshot_date, item)
        add_trend_watch_reasons(
            item,
            ["trend_watch_selected", "strong_growth_trend_watch", "trend_watch_cooldown_available"],
        )
        add_reason_codes(item, ["trend_watch_selected", "strong_growth_trend_watch"])

    for item in eligible[max_items:]:
        if str(item.get("candidate_id")) not in selected_ids:
            item["trend_watch_failures"] = sorted(
                set([*item.get("trend_watch_failures", []), "trend_watch_daily_limit_blocked"])
            )
    return enriched, selected


def with_trend_watch_defaults(candidate: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    item = dict(candidate)
    score, reasons, components = calculate_trend_watch_score(item, config)
    item["trend_watch_score"] = score
    item["trend_watch_score_components"] = components
    item["trend_watch_reasons"] = sorted(set(str(reason) for reason in reasons))
    item.setdefault("trend_watch_failures", [])
    item.setdefault("send_trend_watch", False)
    item.setdefault("trend_watch_stage", "NONE")
    item.setdefault("trend_watch_rank", None)
    item.setdefault("trend_watch_delivery_channel", "none")
    item.setdefault("trend_watch_instance_id", None)
    item["trend_watch_cooldown_key"] = trend_watch_key(item)
    return item


def calculate_trend_watch_score(candidate: dict[str, Any], config: dict[str, Any]) -> tuple[float, list[str], dict[str, float]]:
    weekly_growth = max(float_metric(candidate, "weekly_growth_percent"), 0.0)
    monthly_growth = max(float_metric(candidate, "monthly_growth_percent"), 0.0)
    total_daily = int_metric(candidate, "total_daily_installs")
    app_count = int_metric(candidate, "app_count")
    successful_new_apps = int_metric(candidate, "successful_new_apps_count", fallback_keys=["successful_new_apps"])
    quality = score_100(candidate, "data_quality_score")
    confidence = ratio_metric(candidate, "classification_confidence_avg", default=0.0)
    growth_by_one = ratio_metric(candidate, "growth_by_one_app_share")
    top_app_share = ratio_metric(candidate, "top_app_share")
    risk_tags = set(str(tag) for tag in candidate.get("risk_tags", []))

    weekly_component = min(weekly_growth / 5.0, 30.0)
    monthly_component = min(monthly_growth / 10.0, 20.0)
    demand_component = min(log_score(total_daily, 4.0, 15.0), 15.0)
    breadth_component = min(app_count / 10.0, 1.0) * 10.0
    fresh_component = min(successful_new_apps / 3.0, 1.0) * 10.0
    quality_component = quality / 10.0
    confidence_component = confidence * 5.0
    concentration_penalty = -1.0 * max(growth_by_one - 0.55, 0.0) * 40.0
    concentration_penalty += -1.0 * max(top_app_share - 0.65, 0.0) * 25.0
    risk_penalty = 0.0
    if "severe_paid_spike" in risk_tags:
        risk_penalty -= 30.0
    elif "possible_paid_spike" in risk_tags:
        risk_penalty -= 8.0
    if "classifier_low_confidence" in risk_tags:
        risk_penalty -= 4.0
    if "weak_monetization_signal" in risk_tags:
        risk_penalty -= 2.0

    final = clamp(
        weekly_component
        + monthly_component
        + demand_component
        + breadth_component
        + fresh_component
        + quality_component
        + confidence_component
        + concentration_penalty
        + risk_penalty
    )
    reasons: list[str] = []
    if weekly_growth > 0:
        reasons.append("positive_weekly_growth")
    if monthly_growth > 0:
        reasons.append("positive_monthly_growth")
    if weekly_growth >= float(trend_watch_rules(config).get("min_weekly_growth_percent", 10.0)):
        reasons.append("strong_weekly_growth")
    if monthly_growth >= float(trend_watch_rules(config).get("min_monthly_growth_percent", 20.0)):
        reasons.append("strong_monthly_growth")
    if growth_by_one <= 0.55:
        reasons.append("distributed_growth")
    if total_daily >= int(trend_watch_rules(config).get("min_total_daily_installs", 5000)):
        reasons.append("healthy_trend_watch_volume")

    components = {
        "weekly_growth_component": round(weekly_component, 2),
        "monthly_growth_component": round(monthly_component, 2),
        "demand_component": round(demand_component, 2),
        "breadth_component": round(breadth_component, 2),
        "fresh_success_component": round(fresh_component, 2),
        "data_quality_component": round(quality_component, 2),
        "classification_confidence_component": round(confidence_component, 2),
        "concentration_penalty": round(concentration_penalty, 2),
        "risk_penalty": round(risk_penalty, 2),
        "final": round(final, 2),
    }
    return round(final, 2), sorted(set(reasons)), components


def trend_watch_filter_failures(candidate: dict[str, Any], rules: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    allowed_statuses = {str(status) for status in rules.get("allowed_statuses", [])}
    if str(candidate.get("status")) not in allowed_statuses:
        failures.append("trend_watch_status_not_allowed")
    if bool(rules.get("exclude_regular_alerts", True)) and candidate.get("send_regular_alert") is True:
        failures.append("trend_watch_regular_alert_excluded")

    weekly_growth = float_metric(candidate, "weekly_growth_percent")
    monthly_growth = float_metric(candidate, "monthly_growth_percent")
    if (
        weekly_growth < float(rules.get("min_weekly_growth_percent", 10.0))
        and monthly_growth < float(rules.get("min_monthly_growth_percent", 20.0))
    ):
        failures.append("trend_watch_growth_below_threshold")
    if int_metric(candidate, "history_depth_days") < int(rules.get("min_history_depth_days", 2)):
        failures.append("trend_watch_history_too_shallow")
    if int_metric(candidate, "total_daily_installs") < int(rules.get("min_total_daily_installs", 5000)):
        failures.append("trend_watch_low_total_daily_installs")
    if int_metric(candidate, "app_count") < int(rules.get("min_app_count", 3)):
        failures.append("trend_watch_too_few_apps")
    if int_metric(candidate, "successful_new_apps_count", fallback_keys=["successful_new_apps"]) < int(
        rules.get("min_successful_new_apps", 1)
    ):
        failures.append("trend_watch_too_few_successful_new_apps")
    if score_100(candidate, "data_quality_score") < float(rules.get("min_data_quality_score", 60.0)):
        failures.append("trend_watch_low_data_quality")
    if ratio_metric(candidate, "classification_confidence_avg", default=0.0) < float(
        rules.get("min_classification_confidence_avg", 0.50)
    ):
        failures.append("trend_watch_low_classification_confidence")
    if ratio_metric(candidate, "growth_by_one_app_share") > float(rules.get("max_growth_by_one_app_share", 0.75)):
        failures.append("trend_watch_growth_by_one_app_too_high")
    if ratio_metric(candidate, "top_app_share") > float(rules.get("max_top_app_share", 0.80)):
        failures.append("trend_watch_top_app_too_dominant")
    if (
        bool(rules.get("block_unknown_pattern_if_low_confidence", True))
        and bool(candidate.get("unknown_pattern_blocker_active"))
    ):
        failures.append("trend_watch_unknown_pattern_blocker_active")

    risk_tags = set(str(tag) for tag in candidate.get("risk_tags", []))
    blocked = risk_tags & set(str(tag) for tag in rules.get("blocked_risk_tags", []))
    if blocked:
        failures.append("trend_watch_blocked_risk_tag")
    return sorted(set(failures))


def trend_watch_cooldown_failures(
    candidate: dict[str, Any],
    sent_trend_watch: dict[str, Any],
    cooldown_days: int,
    snapshot_date: str,
) -> list[str]:
    failures = cooldown_failure_reasons(
        trend_watch_key(candidate),
        str(candidate.get("normalized_niche") or candidate.get("niche") or "other"),
        sent_trend_watch,
        cooldown_days,
        snapshot_date,
    )
    return [
        "trend_watch_cooldown_normalized_niche" if failure == "cooldown_normalized_niche" else failure
        for failure in failures
    ]


def mark_trend_watch_sent(
    sent_trend_watch: dict[str, Any],
    items: list[dict[str, Any]],
    snapshot_date: str,
) -> dict[str, Any]:
    updated = dict(sent_trend_watch)
    now = dt.datetime.now(dt.UTC).isoformat()
    for item in items:
        if item.get("send_trend_watch") is not True or item.get("trend_watch_stage") != "TREND_WATCH":
            continue
        key = trend_watch_key(item)
        updated[key] = {
            "normalized_niche": item.get("normalized_niche"),
            "last_sent_at": now if "T" in now else snapshot_date,
            "last_trend_watch_instance_id": item.get("trend_watch_instance_id")
            or make_trend_watch_instance_id(snapshot_date, item),
            "top_app_ids": top_app_ids(item),
            "last_status": item.get("status"),
            "trend_watch_score": item.get("trend_watch_score"),
            "weekly_growth_percent": item.get("weekly_growth_percent"),
            "monthly_growth_percent": item.get("monthly_growth_percent"),
            "updated_at": now,
        }
    return updated


def trend_watch_key(candidate: dict[str, Any]) -> str:
    normalized_niche = str(candidate.get("normalized_niche") or candidate.get("niche") or "other")
    return f"trend_watch:{normalized_niche}"


def make_trend_watch_instance_id(snapshot_date: str, candidate: dict[str, Any]) -> str:
    return f"{snapshot_date}:{trend_watch_key(candidate)}"


def add_trend_watch_reasons(item: dict[str, Any], reasons: list[str]) -> None:
    values = list(item.get("trend_watch_reasons", []))
    for reason in reasons:
        if reason not in values:
            values.append(reason)
    item["trend_watch_reasons"] = sorted(set(str(reason) for reason in values))


def add_reason_codes(item: dict[str, Any], reasons: list[str]) -> None:
    values = list(item.get("reason_codes", []))
    for reason in reasons:
        if reason not in values:
            values.append(reason)
    item["reason_codes"] = sorted(set(str(reason) for reason in values))


def float_metric(candidate: dict[str, Any], key: str, *, default: float = 0.0) -> float:
    value = candidate.get(key)
    if value in (None, ""):
        return default
    try:
        return float(str(value).replace(",", ""))
    except (TypeError, ValueError):
        return default
