from __future__ import annotations

from typing import Any

from .dedupe import make_alert_instance_id, make_dedupe_key, top_app_ids


STATUS_PRIORITY = {
    "ALERT": 5,
    "SINGLE_APP_WATCH": 4,
    "NEAR_MISS": 3,
    "WATCH": 2,
    "REJECT": 1,
}

SPECIFICITY_PRIORITY = {
    "core_mechanic_theme_meta": 5,
    "normalized_niche": 4,
    "core_mechanic_theme": 3,
    "market_category_core_mechanic": 2,
    "core_mechanic": 1,
}


def generate_candidates(
    summaries: list[dict[str, Any]],
    config: dict[str, Any],
    snapshot_date: str,
) -> list[dict[str, Any]]:
    candidates = [build_candidate(summary, config, snapshot_date) for summary in summaries]
    return dedupe_candidates(candidates)


def build_candidate(summary: dict[str, Any], config: dict[str, Any], snapshot_date: str) -> dict[str, Any]:
    top_ids = top_app_ids(summary)
    normalized_niche = str(summary.get("normalized_niche") or summary.get("niche") or "other")
    window = str(summary.get("release_date_window") or "last_180d")
    dedupe_key = make_dedupe_key(normalized_niche, top_ids, window)
    failed_alert_conditions = alert_failed_conditions(summary, config)
    severe_risk = bool(summary.get("severe_paid_spike_risk")) or "severe_paid_spike" in summary.get("risk_tags", [])
    status = determine_status(summary, config, failed_alert_conditions, severe_risk)
    reason_codes = list(summary.get("reason_codes", []))
    if status == "SINGLE_APP_WATCH":
        for reason in ("single_app_breakout", "needs_manual_validation"):
            if reason not in reason_codes:
                reason_codes.append(reason)
    candidate = {
        **summary,
        "candidate_id": f"{snapshot_date}:{dedupe_key}:{summary.get('group_key_type', 'group')}",
        "dedupe_key": dedupe_key,
        "alert_instance_id": make_alert_instance_id(snapshot_date, dedupe_key) if status == "ALERT" else None,
        "status": status,
        "mvp_feasibility_score": candidate_mvp_feasibility(summary),
        "failed_alert_conditions": failed_alert_conditions,
        "reason_codes": sorted(set(reason_codes)),
        "risk_tags": sorted(set(summary.get("risk_tags", []))),
        "llm_summary": None,
        "send_regular_alert": False,
        "initial_baseline_digest": False,
        "would_be_status": None,
        "exclude_from_cooldown": False,
    }
    return candidate


def alert_failed_conditions(summary: dict[str, Any], config: dict[str, Any]) -> list[str]:
    rules = config.get("candidate_generation", {}).get("alert", {})
    failures: list[str] = []
    if float(summary.get("opportunity_score", 0.0)) < float(rules.get("min_opportunity_score", 70)):
        failures.append("low_score")
    if int(summary.get("total_daily_installs", 0)) < int(rules.get("min_total_daily_installs", 5000)):
        failures.append("low_demand")
    if int(summary.get("app_count", 0)) < int(rules.get("min_apps_in_niche", 2)):
        failures.append("too_few_apps")
    if int(summary.get("successful_new_apps_count", 0)) < int(rules.get("min_successful_new_apps", 1)):
        failures.append("no_successful_new_apps")
    if float(summary.get("data_quality_score", 0.0)) < float(rules.get("min_data_quality_score", 65)):
        failures.append("weak_data_quality")
    if candidate_mvp_feasibility(summary) < float(rules.get("min_mvp_feasibility_score", 60)):
        failures.append("low_mvp_feasibility")
    if float(summary.get("giant_developer_share", 0.0)) >= float(rules.get("max_giant_developer_share", 0.7)):
        failures.append("giant_dominated")
    if rules.get("block_severe_paid_spike", True) and bool(summary.get("severe_paid_spike_risk")):
        failures.append("severe_paid_spike")
    return failures


def determine_status(
    summary: dict[str, Any],
    config: dict[str, Any],
    failed_alert_conditions: list[str],
    severe_risk: bool,
) -> str:
    if not failed_alert_conditions:
        return "ALERT"
    if severe_risk:
        return "REJECT"
    if is_single_app_watch(summary, config):
        return "SINGLE_APP_WATCH"
    if is_near_miss(summary, config, failed_alert_conditions):
        return "NEAR_MISS"
    if is_watch(summary, config, failed_alert_conditions):
        return "WATCH"
    return "REJECT"


def is_watch(summary: dict[str, Any], config: dict[str, Any], failed_alert_conditions: list[str]) -> bool:
    rules = config.get("candidate_generation", {}).get("watch", {})
    threshold_delta = float(config.get("_feedback_adjustments", {}).get("watch_threshold_delta", 0.0))
    primary = (
        float(summary.get("opportunity_score", 0.0)) >= float(rules.get("min_opportunity_score", 50)) + threshold_delta
        and int(summary.get("total_daily_installs", 0)) >= int(rules.get("min_total_daily_installs", 2000))
        and int(summary.get("app_count", 0)) >= int(rules.get("min_apps_in_niche", 2))
        and float(summary.get("data_quality_score", 0.0)) >= float(rules.get("min_data_quality_score", 45))
        and candidate_mvp_feasibility(summary) >= float(rules.get("min_mvp_feasibility_score", 50))
    )
    unknown_pattern = bool(summary.get("unknown_or_new_pattern_cluster")) and int(summary.get("total_daily_installs", 0)) >= 1500
    close_to_alert = len(failed_alert_conditions) <= 3
    return primary or unknown_pattern or close_to_alert


def is_single_app_watch(summary: dict[str, Any], config: dict[str, Any]) -> bool:
    rules = config.get("candidate_generation", {}).get("single_app_watch", {})
    top_daily = int(summary.get("top_apps", [{}])[0].get("downloads_daily", 0)) if summary.get("top_apps") else 0
    return (
        int(summary.get("app_count", 0)) == 1
        and top_daily >= int(rules.get("min_top_app_daily_installs", 3000))
        and float(summary.get("giant_developer_share", 0.0)) < 0.7
        and candidate_mvp_feasibility(summary) >= float(rules.get("min_mvp_feasibility_score", 50))
        and float(summary.get("data_quality_score", 0.0)) >= float(rules.get("min_data_quality_score", 40))
        and not bool(summary.get("severe_paid_spike_risk"))
    )


def is_near_miss(summary: dict[str, Any], config: dict[str, Any], failed_alert_conditions: list[str]) -> bool:
    rules = config.get("candidate_generation", {}).get("near_miss", {})
    return (
        float(summary.get("opportunity_score", 0.0)) >= float(rules.get("min_opportunity_score", 60))
        and len(failed_alert_conditions) <= int(rules.get("max_failed_alert_conditions", 2))
        and not bool(summary.get("severe_paid_spike_risk"))
    )


def candidate_mvp_feasibility(summary: dict[str, Any]) -> float:
    if summary.get("mvp_feasibility_score") not in (None, ""):
        return float(summary.get("mvp_feasibility_score", 50.0))
    complexity = str(summary.get("production_complexity") or summary.get("full_product_complexity") or "unknown")
    if complexity == "low":
        return 85.0
    if complexity == "medium":
        return 65.0
    if complexity == "high" and summary.get("simplifiable"):
        return 58.0
    if complexity == "high":
        return 35.0
    return 50.0


def dedupe_candidates(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    best_by_key: dict[str, dict[str, Any]] = {}
    for candidate in candidates:
        key = str(candidate.get("dedupe_key"))
        current = best_by_key.get(key)
        if current is None or candidate_rank(candidate) > candidate_rank(current):
            best_by_key[key] = candidate
    return sorted(
        best_by_key.values(),
        key=lambda item: (
            -STATUS_PRIORITY.get(str(item.get("status")), 0),
            -float(item.get("opportunity_score", 0.0)),
            str(item.get("group_key_value", "")),
        ),
    )


def candidate_rank(candidate: dict[str, Any]) -> tuple[int, int, float, int]:
    return (
        STATUS_PRIORITY.get(str(candidate.get("status")), 0),
        SPECIFICITY_PRIORITY.get(str(candidate.get("group_key_type")), 0),
        float(candidate.get("opportunity_score", 0.0)),
        int(candidate.get("app_count", 0)),
    )
