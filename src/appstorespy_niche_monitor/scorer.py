from __future__ import annotations

import math
from typing import Any

from .coverage import coverage_risk_tags
from .utils import clamp, log_score


def score_summaries(summaries: list[dict[str, Any]], config: dict[str, Any]) -> list[dict[str, Any]]:
    percentiles = demand_percentiles(summaries)
    return [
        score_summary(summary, config, demand_percentile=percentiles.get(str(summary.get("group_key"))))
        for summary in summaries
    ]


def score_summary(
    summary: dict[str, Any],
    config: dict[str, Any],
    *,
    demand_percentile: float | None = None,
) -> dict[str, Any]:
    history_available = bool(summary.get("has_history")) and int(summary.get("history_depth_days", 0)) >= int(
        config.get("scoring", {}).get("use_percentile_demand_after_snapshots", 7)
    )
    demand = demand_score(int(summary.get("total_daily_installs", 0)), history_available, demand_percentile)
    freshness = freshness_score(summary)
    monetization_signal = calculate_monetization_signal(summary)
    revenue = monetization_score(summary, monetization_signal, config)
    rating = rating_score(float(summary.get("avg_rating", 0.0)), float(summary.get("rating_confidence", 1.0)))
    adjustments = config.get("_feedback_adjustments", {})
    mvp_score_value = clamp(
        inferred_mvp_feasibility(summary) + float(adjustments.get("mvp_feasibility_delta", 0.0)),
        0.0,
        100.0,
    )
    mvp = mvp_score_value * 0.15
    quality = clamp(float(summary.get("data_quality_score", 0.0)), 0.0, 100.0) * 0.2
    competition_penalty = calculate_competition_penalty(summary) * float(
        adjustments.get("competition_penalty_multiplier", 1.0)
    )
    giant_penalty = min(float(summary.get("giant_developer_share", 0.0)) * 25.0, 25.0)
    paid_spike_penalty = calculate_paid_spike_penalty(summary) * float(
        adjustments.get("paid_spike_penalty_multiplier", 1.0)
    )

    raw_score = demand + freshness + revenue + rating + mvp + quality - competition_penalty - giant_penalty - paid_spike_penalty
    components = {
        "demand": round(demand, 2),
        "freshness": round(freshness, 2),
        "revenue_monetization": round(revenue, 2),
        "rating": round(rating, 2),
        "mvp_feasibility": round(mvp, 2),
        "data_quality": round(quality, 2),
        "competition_penalty": round(competition_penalty, 2),
        "giant_risk_penalty": round(giant_penalty, 2),
        "paid_spike_penalty": round(paid_spike_penalty, 2),
    }
    scored = dict(summary)
    scored["monetization_signal"] = monetization_signal
    scored["score_components"] = components
    scored["opportunity_score"] = round(clamp(raw_score), 2)
    scored["risk_tags"] = risk_tags(scored)
    scored["reason_codes"] = reason_codes(scored)
    scored["severe_paid_spike_risk"] = "severe_paid_spike" in scored["risk_tags"]
    return scored


def demand_percentiles(summaries: list[dict[str, Any]]) -> dict[str, float]:
    values = sorted({int(item.get("total_daily_installs", 0)) for item in summaries})
    if not values:
        return {}
    if len(values) == 1:
        return {str(item.get("group_key")): 1.0 for item in summaries}
    return {
        str(item.get("group_key")): values.index(int(item.get("total_daily_installs", 0))) / (len(values) - 1)
        for item in summaries
    }


def inferred_mvp_feasibility(summary: dict[str, Any]) -> float:
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


def demand_score(total_daily_installs: int, history_available: bool, percentile: float | None) -> float:
    if history_available and percentile is not None:
        return round(percentile * 25, 2)
    if total_daily_installs >= 20000:
        return 25
    if total_daily_installs >= 10000:
        return 22
    if total_daily_installs >= 5000:
        return 18
    if total_daily_installs >= 2000:
        return 12
    if total_daily_installs >= 1000:
        return 8
    return 0


def freshness_score(summary: dict[str, Any]) -> float:
    return min(
        int(summary.get("traction_fresh_apps_count", 0)) * 6
        + int(summary.get("successful_new_apps_count", 0)) * 2,
        15,
    )


def calculate_monetization_signal(summary: dict[str, Any]) -> dict[str, Any]:
    top_apps = summary.get("top_apps", [])
    iap_values = [app.get("iap") for app in top_apps if app.get("iap") is not None]
    ads_values = [app.get("ads") for app in top_apps if app.get("ads") is not None]
    iap_present = any(bool(value) for value in iap_values) if iap_values else "unknown"
    ads_present = any(bool(value) for value in ads_values) if ads_values else "unknown"
    revenue_month_available = float(summary.get("total_monthly_revenue", 0.0)) > 0
    if ads_present is True and iap_present is True:
        model = "hybrid"
    elif ads_present is True:
        model = "ads"
    elif iap_present is True:
        model = "iap"
    else:
        model = "unknown"
    confidence = "high" if revenue_month_available else ("medium" if model != "unknown" else "low")
    return {
        "iap_present": iap_present,
        "ads_present": ads_present,
        "revenue_month_available": revenue_month_available,
        "revenue_confidence": confidence,
        "monetization_model": model,
    }


def monetization_score(
    summary: dict[str, Any],
    monetization_signal: dict[str, Any],
    config: dict[str, Any],
) -> float:
    revenue = float(summary.get("total_monthly_revenue", 0.0))
    if revenue > 0:
        return log_score(revenue, 3.0, 15.0)
    if monetization_signal.get("monetization_model") in {"ads", "iap", "hybrid"}:
        return float(config.get("scoring", {}).get("neutral_monetization_score", 6))
    return 0.0


def rating_confidence(rating_count: int | None) -> float:
    if not rating_count:
        return 0.0
    return min(math.log10(rating_count + 1) / 4, 1.0)


def rating_score(avg_rating: float, confidence: float = 1.0) -> float:
    if avg_rating <= 0:
        return 0.0
    distance = abs(avg_rating - 4.45)
    base = clamp(10.0 - distance * 8.0, 0.0, 10.0)
    return base * clamp(confidence, 0.0, 1.0)


def calculate_competition_penalty(summary: dict[str, Any]) -> float:
    top_app_share = float(summary.get("top_app_share", 0.0))
    single_developer_share = float(summary.get("single_developer_share", 0.0))
    penalty = min(int(summary.get("app_count", 0)) * 0.25, 3.0)
    if top_app_share > 0.75:
        penalty += (top_app_share - 0.75) * 12.0
    if single_developer_share > 0.8:
        penalty += (single_developer_share - 0.8) * 15.0
    return min(penalty, 20.0)


def calculate_paid_spike_penalty(summary: dict[str, Any]) -> float:
    if severe_paid_spike(summary):
        return 15.0
    penalty = 0.0
    if float(summary.get("growth_by_one_app_share", 0.0)) >= 0.8:
        penalty += 8.0
    if float(summary.get("advertised_top_app_share", 0.0)) >= 0.7:
        penalty += 7.0
    elif float(summary.get("advertised_top_app_share", 0.0)) >= 0.5:
        penalty += 4.0
    return min(penalty, 15.0)


def severe_paid_spike(summary: dict[str, Any]) -> bool:
    top_apps = summary.get("top_apps", [])
    top_app = top_apps[0] if top_apps else {}
    weak_rating = float(summary.get("rating_confidence", 0.0)) < 0.3
    current_slice_spike = (
        float(summary.get("top_app_share", 0.0)) >= 0.85
        and bool(top_app.get("advertised", False))
        and int(summary.get("app_count", 0)) <= 2
        and weak_rating
    )
    history_spike = (
        float(summary.get("growth_by_one_app_share", 0.0)) >= 0.8
        and int(summary.get("app_count", 0)) <= 2
    )
    return current_slice_spike or history_spike


def reason_codes(summary: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    if int(summary.get("app_count", 0)) >= 2:
        reasons.append("multi_app_cluster")
    if float(summary.get("total_daily_installs", 0.0)) >= 5000:
        reasons.append("strong_daily_installs")
    if int(summary.get("traction_fresh_apps_count", 0)) > 0 or int(summary.get("successful_new_apps_count", 0)) > 0:
        reasons.append("fresh_traction")
    if str(summary.get("mvp_complexity")) == "low":
        reasons.append("low_mvp_complexity")
    if summary.get("full_product_complexity") == "high" and summary.get("simplifiable"):
        reasons.append("simplifiable_high_complexity")
    if float(summary.get("giant_developer_share", 0.0)) < 0.7:
        reasons.append("low_giant_share")
    if float(summary.get("top_app_share", 0.0)) < 0.75 and int(summary.get("app_count", 0)) >= 2:
        reasons.append("diversified_apps")
    if summary.get("monetization_signal", {}).get("monetization_model") != "unknown":
        reasons.append("monetization_signal_present")
    if float(summary.get("rating_confidence", 0.0)) >= 0.5:
        reasons.append("good_rating_confidence")
    if summary.get("unknown_or_new_pattern_cluster"):
        reasons.append("new_pattern_detected")
    if int(summary.get("app_count", 0)) == 1 and float(summary.get("total_daily_installs", 0.0)) >= 3000:
        reasons.append("single_app_breakout")
    if float(summary.get("weekly_growth_percent", 0.0)) > 0:
        reasons.append("growing_vs_previous_snapshot")
    if float(summary.get("weekly_growth_percent", 0.0)) >= 25:
        reasons.append("historical_growth")
    if summary.get("production_complexity") == "low" or summary.get("mvp_complexity") == "low":
        reasons.append("small_team_fit")
    return sorted(set(reasons))


def risk_tags(summary: dict[str, Any]) -> list[str]:
    risks: list[str] = []
    if float(summary.get("top_app_share", 0.0)) >= 0.75:
        risks.append("leader_dominated")
    if severe_paid_spike(summary):
        risks.append("severe_paid_spike")
    elif float(summary.get("advertised_top_app_share", 0.0)) >= 0.5:
        risks.append("possible_paid_spike")
    if float(summary.get("growth_by_one_app_share", 0.0)) >= 0.8:
        risks.append("growth_by_one_app")
    if float(summary.get("giant_developer_share", 0.0)) >= 0.7:
        risks.append("giant_developer_risk")
    if float(summary.get("single_developer_share", 0.0)) >= 0.8:
        risks.append("single_developer_cluster")
    if float(summary.get("rating_confidence", 0.0)) < 0.3:
        risks.append("weak_rating_signal")
    if summary.get("monetization_signal", {}).get("revenue_confidence") != "high":
        risks.append("weak_revenue_signal")
    if summary.get("monetization_signal", {}).get("monetization_model") == "unknown":
        risks.append("weak_monetization_signal")
    if float(summary.get("data_quality_score", 0.0)) < 45:
        risks.append("low_data_quality")
    if float(summary.get("classification_confidence_avg", 1.0)) < 0.7:
        risks.append("classifier_low_confidence")
    coverage = summary.get("coverage", {})
    if isinstance(coverage, dict):
        risks.extend(coverage_risk_tags(coverage))
    if summary.get("full_product_complexity") == "high":
        risks.append("high_full_complexity")
    if "unknown" in str(summary.get("audience_summary", "")):
        risks.append("audience_uncertain")
    return sorted(set(risks))
