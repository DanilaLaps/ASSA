from __future__ import annotations

from typing import Any

from .utils import date_distance_days


FIRST_RUN_NO_HISTORY = "FIRST_RUN_NO_HISTORY"
HISTORY_AVAILABLE = "HISTORY_AVAILABLE"
WEEKLY_HISTORY_AVAILABLE = "WEEKLY_HISTORY_AVAILABLE"


CONFIDENCE_ORDER = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}


def detect_history_state(
    history_summaries: list[dict[str, Any]],
    config: dict[str, Any],
    snapshot_date: str,
) -> str:
    score_version = config.get("app", {}).get("score_version", "v1.3.2")
    compatible = [
        item
        for item in history_summaries
        if str(item.get("snapshot_date", "")) < snapshot_date
        and item.get("score_version") == score_version
    ]
    if not compatible:
        return FIRST_RUN_NO_HISTORY
    weekly_days = int(config.get("first_run_behavior", {}).get("allow_growth_based_alerts_after_snapshots", 7))
    for item in compatible:
        distance = date_distance_days(snapshot_date, str(item.get("snapshot_date", "")))
        if distance is not None and abs(distance - weekly_days) <= 2:
            return WEEKLY_HISTORY_AVAILABLE
    return HISTORY_AVAILABLE


def confidence_level(candidate: dict[str, Any], history_state: str) -> str:
    if history_state == FIRST_RUN_NO_HISTORY:
        return "MEDIUM" if float(candidate.get("data_quality_score", 0.0)) >= 65 else "LOW"
    if float(candidate.get("data_quality_score", 0.0)) >= 75 and history_state == WEEKLY_HISTORY_AVAILABLE:
        return "HIGH"
    if float(candidate.get("data_quality_score", 0.0)) >= 55:
        return "MEDIUM"
    return "LOW"


def cap_confidence(level: str, maximum: str) -> str:
    if CONFIDENCE_ORDER.get(level, 0) <= CONFIDENCE_ORDER.get(maximum, 1):
        return level
    return maximum


def apply_initial_baseline_rules(
    candidates: list[dict[str, Any]],
    config: dict[str, Any],
    history_state: str,
) -> list[dict[str, Any]]:
    first_run = history_state == FIRST_RUN_NO_HISTORY
    first_cfg = config.get("first_run_behavior", {})
    include_statuses = set(
        first_cfg.get(
            "include_statuses_in_initial_digest",
            ["ALERT", "WATCH", "SINGLE_APP_WATCH", "NEAR_MISS"],
        )
    )
    max_items = int(first_cfg.get("max_initial_digest_items", 10))
    required_reason = str(first_cfg.get("required_reason_code", "INITIAL_BASELINE_NO_HISTORY"))
    max_confidence = str(first_cfg.get("max_confidence_level", "MEDIUM"))
    ranked_indexes = [
        index
        for index, candidate in sorted(
            enumerate(candidates),
            key=lambda pair: float(pair[1].get("opportunity_score", 0.0)),
            reverse=True,
        )
        if pair_status(candidate) in include_statuses
    ]
    digest_indexes = set(ranked_indexes[:max_items]) if first_run else set()

    enriched: list[dict[str, Any]] = []
    for index, candidate in enumerate(candidates):
        item = dict(candidate)
        item["history_state"] = history_state
        item["first_run_without_history"] = first_run
        item["confidence_level"] = confidence_level(item, history_state)
        item.setdefault("would_be_status", None)
        item.setdefault("initial_baseline_digest", False)
        item.setdefault("exclude_from_cooldown", False)
        item.setdefault("send_regular_alert", False)
        if first_run:
            item["would_be_status"] = item.get("status")
            item["send_regular_alert"] = False
            item["exclude_from_cooldown"] = True
            item["confidence_level"] = cap_confidence(item["confidence_level"], max_confidence)
            if index in digest_indexes:
                item["initial_baseline_digest"] = True
                reason_codes = list(item.get("reason_codes", []))
                if required_reason not in reason_codes:
                    reason_codes.append(required_reason)
                item["reason_codes"] = reason_codes
        enriched.append(item)
    return enriched


def pair_status(candidate: dict[str, Any]) -> str:
    return str(candidate.get("status", "REJECT"))
