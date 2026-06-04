from __future__ import annotations

from collections import Counter
from typing import Any

from .aggregator import stable_key
from .utils import clamp, safe_div


def enrich_data_quality(
    summaries: list[dict[str, Any]],
    apps: list[dict[str, Any]],
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    apps_by_key: dict[str, list[dict[str, Any]]] = {}
    for app in apps:
        apps_by_key.setdefault(stable_key(app), []).append(app)
    return [
        {
            **summary,
            **calculate_data_quality(
                summary,
                apps_by_key.get(str(summary.get("group_key")), []),
                config,
            ),
        }
        for summary in summaries
    ]


def calculate_data_quality(
    summary: dict[str, Any],
    apps: list[dict[str, Any]],
    config: dict[str, Any],
) -> dict[str, Any]:
    quality_cfg = config.get("data_quality", {})
    required_fields = quality_cfg.get("required_fields", [])
    reasons: list[str] = []
    field_completeness = field_completeness_ratio(apps, required_fields)
    field_score = 35.0 * field_completeness

    history_depth = int(summary.get("history_depth_days", 0))
    history_score = 10.0 if history_depth >= 7 else (5.0 if history_depth > 0 else 0.0)
    if history_score == 0.0:
        reasons.append("no_history")

    min_apps = int(quality_cfg.get("min_apps_for_reliable_signal", 3))
    sample_score = 20.0 * min(safe_div(int(summary.get("app_count", 0)), min_apps), 1.0)
    if int(summary.get("app_count", 0)) < min_apps:
        reasons.append("low_sample_size")

    top_app_share = float(summary.get("top_app_share", 0.0))
    diversity_score = 15.0 * clamp(1.0 - max(top_app_share - 0.35, 0.0) / 0.65, 0.0, 1.0)
    if top_app_share >= 0.75:
        reasons.append("top_app_dominance")

    revenue_present_ratio = field_completeness_ratio(apps, ["revenue_month"])
    revenue_value = float(summary.get("total_monthly_revenue", 0.0))
    monetization_score = 10.0 if revenue_value > 0 else 4.0 * revenue_present_ratio
    if revenue_value <= 0 and quality_cfg.get("penalize_missing_revenue", True):
        reasons.append("weak_monetization_data")

    freshness_score = 10.0 * min(safe_div(int(summary.get("successful_new_apps_count", 0)), 2), 1.0)
    if int(summary.get("successful_new_apps_count", 0)) <= 0:
        reasons.append("no_successful_new_apps")

    penalty = 0.0
    if field_completeness < 1.0:
        penalty += (1.0 - field_completeness) * 15.0
        reasons.append("missing_required_fields")

    one_app_threshold = float(quality_cfg.get("one_app_growth_penalty_threshold", 0.7))
    if float(summary.get("growth_by_one_app_share", 0.0)) >= one_app_threshold:
        penalty += 15.0
        reasons.append("one_app_growth")

    if float(summary.get("advertised_top_app_share", 0.0)) >= 0.7:
        penalty += 10.0
        reasons.append("paid_spike_risk")

    score = clamp(field_score + history_score + sample_score + diversity_score + monetization_score + freshness_score - penalty)
    return {
        "data_quality_score": round(score, 2),
        "data_quality_components": {
            "field_completeness": round(field_score, 2),
            "history_depth": round(history_score, 2),
            "sample_size": round(sample_score, 2),
            "signal_diversity": round(diversity_score, 2),
            "monetization_reliability": round(monetization_score, 2),
            "fresh_success_reliability": round(freshness_score, 2),
            "penalty": round(penalty, 2),
        },
        "data_quality_reasons": sorted(set(reasons)),
    }


def field_completeness_ratio(apps: list[dict[str, Any]], fields: list[str]) -> float:
    if not apps or not fields:
        return 0.0
    total = len(apps) * len(fields)
    present = 0
    missing_counter: Counter[str] = Counter()
    for app in apps:
        for field in fields:
            if app.get(field) not in (None, ""):
                present += 1
            else:
                missing_counter[field] += 1
    return safe_div(present, total)
