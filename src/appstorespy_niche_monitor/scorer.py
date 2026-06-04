from __future__ import annotations

from typing import Any

from .utils import clamp, log_score


def score_summaries(summaries: list[dict[str, Any]], config: dict[str, Any]) -> list[dict[str, Any]]:
    return [score_summary(summary, config) for summary in summaries]


def score_summary(summary: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    demand = log_score(float(summary.get("total_daily_installs", 0)), 5.0, 25.0)
    freshness = min(float(summary.get("successful_new_apps_count", 0)) * 7.5, 15.0)
    revenue = log_score(float(summary.get("total_monthly_revenue", 0.0)), 3.0, 15.0)
    rating = rating_score(float(summary.get("avg_rating", 0.0)))
    production = float(
        config.get("production_scores", {}).get(
            summary.get("niche", "other"),
            config.get("production_scores", {}).get("other", 3),
        )
    )
    quality = clamp(float(summary.get("data_quality_score", 0.0)), 0.0, 100.0) * 0.2
    competition_penalty = calculate_competition_penalty(summary)
    giant_penalty = min(float(summary.get("giant_developer_share", 0.0)) * 25.0, 25.0)
    paid_spike_penalty = calculate_paid_spike_penalty(summary)

    raw_score = (
        demand
        + freshness
        + revenue
        + rating
        + production
        + quality
        - competition_penalty
        - giant_penalty
        - paid_spike_penalty
    )
    components = {
        "demand": round(demand, 2),
        "freshness": round(freshness, 2),
        "revenue": round(revenue, 2),
        "rating": round(rating, 2),
        "production": round(production, 2),
        "data_quality": round(quality, 2),
        "competition_penalty": round(competition_penalty, 2),
        "giant_risk_penalty": round(giant_penalty, 2),
        "paid_spike_penalty": round(paid_spike_penalty, 2),
    }
    scored = dict(summary)
    scored["score_components"] = components
    scored["opportunity_score"] = round(clamp(raw_score), 2)
    scored["reason_codes"] = reason_codes(scored)
    return scored


def rating_score(avg_rating: float) -> float:
    if avg_rating <= 0:
        return 0.0
    # Sweet spot: strong demand, but still room to outperform incumbents.
    distance = abs(avg_rating - 4.45)
    return clamp(10.0 - distance * 8.0, 0.0, 10.0)


def calculate_competition_penalty(summary: dict[str, Any]) -> float:
    app_count = int(summary.get("app_count", 0))
    top_app_share = float(summary.get("top_app_share", 0.0))
    penalty = min(app_count * 0.5, 5.0)
    penalty += top_app_share * 8.0
    if top_app_share > 0.55:
        penalty += (top_app_share - 0.55) * 25.0
    return min(penalty, 20.0)


def calculate_paid_spike_penalty(summary: dict[str, Any]) -> float:
    one_app_growth_share = float(summary.get("growth_by_one_app_share", 0.0))
    advertised_share = float(summary.get("advertised_top_app_share", 0.0))
    penalty = 0.0
    if one_app_growth_share >= 0.7:
        penalty += 10.0
    elif one_app_growth_share >= 0.5:
        penalty += 5.0
    if advertised_share >= 0.7:
        penalty += 8.0
    elif advertised_share >= 0.5:
        penalty += 4.0
    return min(penalty, 15.0)


def reason_codes(summary: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    if float(summary.get("total_daily_installs", 0.0)) >= 50000:
        reasons.append("high_demand")
    elif float(summary.get("total_daily_installs", 0.0)) >= 5000:
        reasons.append("demand_signal")
    if float(summary.get("weekly_growth_percent", 0.0)) >= 25:
        reasons.append("historical_growth")
    if int(summary.get("successful_new_apps_count", 0)) > 0:
        reasons.append("fresh_successes")
    if float(summary.get("total_monthly_revenue", 0.0)) > 0:
        reasons.append("monetization_signal")
    if float(summary.get("top_app_share", 0.0)) >= 0.75:
        reasons.append("top_app_concentration")
    if float(summary.get("growth_by_one_app_share", 0.0)) >= 0.7 or float(summary.get("advertised_top_app_share", 0.0)) >= 0.7:
        reasons.append("paid_spike_risk")
    if float(summary.get("giant_developer_share", 0.0)) >= 0.7:
        reasons.append("giant_dominated")
    if float(summary.get("data_quality_score", 0.0)) < 65:
        reasons.append("weak_data_quality")
    if summary.get("production_complexity") == "low":
        reasons.append("small_team_fit")
    if summary.get("production_complexity") == "high":
        reasons.append("high_production_complexity")
    return sorted(set(reasons))
