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
    country_counts = country_count_by_signature(summaries)
    return [
        {
            **summary,
            **calculate_data_quality(
                summary,
                apps_by_key.get(str(summary.get("group_key")), []),
                config,
                country_counts.get(str(summary.get("signal_signature")), 1),
            ),
        }
        for summary in summaries
    ]


def country_count_by_signature(summaries: list[dict[str, Any]]) -> dict[str, int]:
    countries: dict[str, set[str]] = {}
    for summary in summaries:
        signature = str(summary.get("signal_signature", ""))
        countries.setdefault(signature, set()).add(str(summary.get("country", "")))
    return {key: len(value) for key, value in countries.items()}


def calculate_data_quality(
    summary: dict[str, Any],
    apps: list[dict[str, Any]],
    config: dict[str, Any],
    countries_with_signal: int,
) -> dict[str, Any]:
    quality_cfg = config.get("data_quality", {})
    required_fields = quality_cfg.get("required_fields", [])
    reasons: list[str] = []
    field_completeness = field_completeness_ratio(apps, required_fields)
    field_score = 30.0 * field_completeness

    history_depth = int(summary.get("history_depth_days", 0))
    history_score = 15.0 if history_depth >= 7 else (8.0 if history_depth > 0 else 0.0)
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

    min_countries = int(quality_cfg.get("min_countries_for_strong_signal", 2))
    geo_score = 10.0 * min(safe_div(countries_with_signal, min_countries), 1.0)
    if countries_with_signal < min_countries:
        reasons.append("single_country_signal")

    penalty = 0.0
    if field_completeness < 1.0:
        penalty += (1.0 - field_completeness) * 15.0
        reasons.append("missing_required_fields")

    one_app_threshold = float(quality_cfg.get("one_app_growth_penalty_threshold", 0.7))
    if float(summary.get("growth_by_one_app_share", 0.0)) >= one_app_threshold:
        penalty += 15.0
        reasons.append("one_app_growth")

    score = clamp(field_score + history_score + sample_score + diversity_score + monetization_score + geo_score - penalty)
    return {
        "data_quality_score": round(score, 2),
        "data_quality_components": {
            "field_completeness": round(field_score, 2),
            "history_depth": round(history_score, 2),
            "sample_size": round(sample_score, 2),
            "signal_diversity": round(diversity_score, 2),
            "monetization_reliability": round(monetization_score, 2),
            "geo_confirmation": round(geo_score, 2),
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
