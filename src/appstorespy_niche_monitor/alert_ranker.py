from __future__ import annotations

from typing import Any

from .utils import clamp, log_score, safe_div


DEFAULT_SENDABLE_RULES = {
    "enabled": True,
    "min_sendable_alert_score": 80.0,
    "min_opportunity_score": 75.0,
    "min_trend_confidence_score": 65.0,
    "min_team_fit_score": 60.0,
    "min_data_quality_score": 70.0,
    "min_classification_confidence_avg": 0.60,
    "min_mvp_feasibility_score": 60.0,
    "min_app_count": 3,
    "min_successful_new_apps": 2,
    "min_unique_developers": 2,
    "min_total_daily_installs": 3000,
    "max_top_app_share": 0.60,
    "max_top3_app_share": 0.85,
    "max_growth_by_one_app_share": 0.65,
    "max_advertised_top_app_share": 0.60,
    "max_giant_developer_share": 0.50,
    "max_single_developer_share": 0.70,
    "block_single_app_breakout_as_regular_alert": True,
    "block_unknown_or_new_pattern_if_low_confidence": True,
    "block_other_niche_if_low_confidence": True,
    "blocked_risk_tags": ["severe_paid_spike", "low_data_quality"],
    "soft_penalty_risk_tags": [
        "possible_paid_spike",
        "leader_dominated",
        "growth_by_one_app",
        "classifier_low_confidence",
        "weak_revenue_signal",
        "weak_monetization_signal",
        "audience_uncertain",
        "mixed_unknown_cluster",
    ],
    "max_sendable_per_normalized_niche": 1,
    "max_sendable_per_core_mechanic": 2,
    "max_sendable_per_market_signal_key": 1,
    "hard_alert_max_top_app_share": 0.75,
    "hard_alert_max_growth_by_one_app_share": 0.75,
    "hard_alert_min_classification_confidence": 0.50,
    "hard_alert_min_data_quality_score": 60.0,
    "hard_alert_min_mvp_feasibility_score": 50.0,
    "unknown_pattern_alert_min_classification_confidence": 0.70,
    "unknown_pattern_alert_min_app_count": 4,
    "unknown_pattern_alert_min_successful_new_apps": 2,
    "unknown_pattern_alert_min_data_quality_score": 75.0,
}


def sendable_rules(config: dict[str, Any]) -> dict[str, Any]:
    configured = config.get("sendable_alert_rules", {})
    if not isinstance(configured, dict):
        configured = {}
    return {**DEFAULT_SENDABLE_RULES, **configured}


def calculate_trend_confidence_score(
    candidate: dict[str, Any],
    config: dict[str, Any],
) -> tuple[float, list[str], list[str]]:
    rules = sendable_rules(config)
    reasons: list[str] = []
    failures: list[str] = []
    app_count = int_metric(candidate, "app_count")
    successful_new_apps = successful_new_apps_count(candidate)
    unique_developers = unique_developer_count(candidate)
    total_daily = int_metric(candidate, "total_daily_installs")
    weekly_growth = float_metric(candidate, "weekly_growth_percent")
    monthly_growth = float_metric(candidate, "monthly_growth_percent")
    history_depth = int_metric(candidate, "history_depth_days")
    top_app_share = ratio_metric(candidate, "top_app_share")
    growth_by_one_app_share = ratio_metric(candidate, "growth_by_one_app_share")
    advertised_top_app_share = ratio_metric(candidate, "advertised_top_app_share")
    giant_developer_share = ratio_metric(candidate, "giant_developer_share")
    single_developer_share = ratio_metric(candidate, "single_developer_share")
    quality = score_100(candidate, "data_quality_score")
    classification_confidence = ratio_metric(candidate, "classification_confidence_avg", default=0.70)

    score = 0.0
    score += 15.0 * min(safe_div(app_count, int(rules.get("min_app_count", 3))), 1.0)
    if app_count >= int(rules.get("min_app_count", 3)):
        reasons.append("multi_app_validation")
    else:
        failures.append("too_few_apps_for_trend_confidence")

    score += 15.0 * min(safe_div(successful_new_apps, int(rules.get("min_successful_new_apps", 2))), 1.0)
    if successful_new_apps >= int(rules.get("min_successful_new_apps", 2)):
        reasons.append("fresh_success_validation")
    else:
        failures.append("too_few_successful_new_apps_for_trend_confidence")

    score += 12.0 * min(safe_div(unique_developers, int(rules.get("min_unique_developers", 2))), 1.0)
    if unique_developers >= int(rules.get("min_unique_developers", 2)):
        reasons.append("multi_developer_validation")
    else:
        failures.append("low_developer_diversity")

    score += min(log_score(total_daily, 4.5, 16.0), 16.0)
    if total_daily >= int(rules.get("min_total_daily_installs", 3000)):
        reasons.append("healthy_install_volume")
    else:
        failures.append("low_total_daily_installs_for_trend_confidence")

    growth_points = 0.0
    if weekly_growth > 0:
        growth_points += min(weekly_growth / 5.0, 6.0)
    if monthly_growth > 0:
        growth_points += min(monthly_growth / 10.0, 4.0)
    score += growth_points
    if growth_points > 0:
        reasons.append("positive_growth_signal")
    elif history_depth <= 0:
        failures.append("no_growth_history")

    if history_depth >= 14:
        score += 5.0
        reasons.append("history_depth_14d")
    elif history_depth >= 7:
        score += 3.0
        reasons.append("history_depth_7d")

    score += (quality / 100.0) * 10.0
    if quality >= normalized_threshold_100(rules.get("min_data_quality_score", 70.0)):
        reasons.append("healthy_data_quality")
    else:
        failures.append("below_data_quality_for_trend_confidence")

    score += classification_confidence * 7.0
    if classification_confidence >= float(rules.get("min_classification_confidence_avg", 0.60)):
        reasons.append("classification_confident")
    else:
        failures.append("low_classification_confidence")

    penalty = 0.0
    if top_app_share > 0.60:
        penalty += min((top_app_share - 0.60) * 45.0, 14.0)
        failures.append("top_app_concentration_penalty")
    if growth_by_one_app_share > 0.60:
        penalty += min((growth_by_one_app_share - 0.60) * 45.0, 12.0)
        failures.append("one_app_growth_penalty")
    if advertised_top_app_share > 0.45:
        penalty += min((advertised_top_app_share - 0.45) * 40.0, 12.0)
        failures.append("paid_acquisition_penalty")
    if giant_developer_share > 0.35:
        penalty += min((giant_developer_share - 0.35) * 35.0, 10.0)
        failures.append("giant_developer_penalty")
    if single_developer_share > 0.65:
        penalty += min((single_developer_share - 0.65) * 30.0, 8.0)
        failures.append("single_developer_penalty")

    risk_tags = set(str(tag) for tag in candidate.get("risk_tags", []))
    if "severe_paid_spike" in risk_tags:
        penalty += 20.0
        failures.append("severe_paid_spike_penalty")
    elif "possible_paid_spike" in risk_tags:
        penalty += 8.0
        failures.append("possible_paid_spike_penalty")
    if "growth_by_one_app" in risk_tags:
        penalty += 6.0
    if "classifier_low_confidence" in risk_tags:
        penalty += 4.0

    return round(clamp(score - penalty), 2), sorted(set(reasons)), sorted(set(failures))


def calculate_team_fit_score(
    candidate: dict[str, Any],
    config: dict[str, Any],
) -> tuple[float, list[str], list[str]]:
    reasons: list[str] = []
    failures: list[str] = []
    mvp_feasibility = score_100(candidate, "mvp_feasibility_score", default=50.0)
    production_complexity = str(
        candidate.get("production_complexity")
        or candidate.get("full_product_complexity")
        or "unknown"
    ).lower()
    full_complexity = str(candidate.get("full_product_complexity") or production_complexity).lower()
    mvp_complexity = str(candidate.get("mvp_complexity") or production_complexity).lower()
    simplifiable = bool(candidate.get("simplifiable"))
    giant_developer_share = ratio_metric(candidate, "giant_developer_share")
    single_developer_share = ratio_metric(candidate, "single_developer_share")
    top_app_share = ratio_metric(candidate, "top_app_share")
    risk_tags = set(str(tag) for tag in candidate.get("risk_tags", []))

    score = mvp_feasibility * 0.55
    if mvp_feasibility >= 70:
        reasons.append("strong_mvp_feasibility")
    elif mvp_feasibility >= 60:
        reasons.append("acceptable_mvp_feasibility")
    else:
        failures.append("low_mvp_feasibility")

    complexity_points = {
        "low": 25.0,
        "medium": 15.0,
        "high": 4.0 if simplifiable else 0.0,
        "unknown": 8.0,
    }.get(production_complexity, 8.0)
    score += complexity_points
    if production_complexity == "low":
        reasons.append("low_production_complexity")
    elif production_complexity == "medium":
        reasons.append("medium_production_complexity")
    elif production_complexity == "high" and not simplifiable:
        failures.append("high_production_complexity")

    if mvp_complexity == "low":
        score += 8.0
        reasons.append("low_mvp_complexity")
    elif mvp_complexity == "medium":
        score += 4.0
    elif mvp_complexity == "high":
        failures.append("high_mvp_complexity")

    if simplifiable:
        score += 5.0
        reasons.append("simplifiable_scope")

    if full_complexity == "high" and production_complexity != "low":
        score -= 8.0
        failures.append("complex_full_product")

    if giant_developer_share <= 0.30:
        score += 5.0
        reasons.append("low_giant_developer_share")
    else:
        penalty = min((giant_developer_share - 0.30) * 35.0, 15.0)
        score -= penalty
        failures.append("giant_developer_competition")

    if single_developer_share >= 0.75:
        score -= 8.0
        failures.append("single_developer_dominance")
    if top_app_share >= 0.70:
        score -= 8.0
        failures.append("leader_dominated_market")

    content_tags = {"high_content_burden", "needs_large_content_pipeline", "complex_meta_loop"}
    if risk_tags & content_tags:
        score -= 12.0
        failures.extend(sorted(risk_tags & content_tags))
    if "too_competitive" in risk_tags:
        score -= 8.0
        failures.append("too_competitive")

    if score >= 70:
        reasons.append("small_team_fit")

    return round(clamp(score), 2), sorted(set(reasons)), sorted(set(failures))


def calculate_sendable_alert_score(
    candidate: dict[str, Any],
    config: dict[str, Any],
) -> tuple[float, list[str], list[str]]:
    trend_score, trend_reasons, trend_failures = calculate_trend_confidence_score(candidate, config)
    team_score, team_reasons, team_failures = calculate_team_fit_score(candidate, config)
    score, reasons, failures, _components = calculate_sendable_score_with_inputs(
        candidate,
        config,
        trend_score,
        team_score,
    )
    return score, sorted(set(reasons + trend_reasons + team_reasons)), sorted(set(failures + trend_failures + team_failures))


def passes_sendable_hard_filters(candidate: dict[str, Any], config: dict[str, Any]) -> tuple[bool, list[str]]:
    rules = sendable_rules(config)
    if not bool(rules.get("enabled", True)):
        return True, []

    failures: list[str] = []
    if candidate.get("status") != "ALERT":
        failures.append("not_alert_status")

    sendable_score = float_metric(candidate, "sendable_alert_score")
    trend_score = float_metric(candidate, "trend_confidence_score")
    team_score = float_metric(candidate, "team_fit_score")
    opportunity_score = score_100(candidate, "opportunity_score")
    quality = score_100(candidate, "data_quality_score")
    confidence = ratio_metric(candidate, "classification_confidence_avg", default=0.0)
    mvp_feasibility = score_100(candidate, "mvp_feasibility_score")
    app_count = int_metric(candidate, "app_count")
    successful_new_apps = successful_new_apps_count(candidate)
    unique_developers = unique_developer_count(candidate)
    total_daily = int_metric(candidate, "total_daily_installs")
    top_app_share = ratio_metric(candidate, "top_app_share")
    top3_app_share = ratio_metric(candidate, "top3_app_share", default=top_app_share)
    growth_by_one_app_share = ratio_metric(candidate, "growth_by_one_app_share")
    advertised_top_app_share = ratio_metric(candidate, "advertised_top_app_share")
    giant_developer_share = ratio_metric(candidate, "giant_developer_share")
    single_developer_share = ratio_metric(candidate, "single_developer_share")

    if sendable_score < float(rules.get("min_sendable_alert_score", 80.0)):
        failures.append("below_sendable_alert_score")
    if opportunity_score < float(rules.get("min_opportunity_score", 75.0)):
        failures.append("below_opportunity_score")
    if trend_score < float(rules.get("min_trend_confidence_score", 65.0)):
        failures.append("below_trend_confidence_score")
    if team_score < float(rules.get("min_team_fit_score", 60.0)):
        failures.append("below_team_fit_score")
    if quality < normalized_threshold_100(rules.get("min_data_quality_score", 70.0)):
        failures.append("below_data_quality_score")
    if confidence < float(rules.get("min_classification_confidence_avg", 0.60)):
        failures.append("below_classification_confidence")
    if mvp_feasibility < float(rules.get("min_mvp_feasibility_score", 60.0)):
        failures.append("below_mvp_feasibility")
    if app_count < int(rules.get("min_app_count", 3)):
        failures.append("too_few_apps_for_sendable")
    if successful_new_apps < int(rules.get("min_successful_new_apps", 2)):
        failures.append("too_few_successful_new_apps")
    if unique_developers < int(rules.get("min_unique_developers", 2)):
        failures.append("too_few_unique_developers")
    if total_daily < int(rules.get("min_total_daily_installs", 3000)):
        failures.append("low_total_daily_installs")
    if top_app_share > float(rules.get("max_top_app_share", 0.60)):
        failures.append("top_app_too_dominant")
    if top3_app_share > float(rules.get("max_top3_app_share", 0.85)):
        failures.append("top3_too_dominant")
    if growth_by_one_app_share > float(rules.get("max_growth_by_one_app_share", 0.65)):
        failures.append("growth_by_one_app_too_high")
    if advertised_top_app_share > float(rules.get("max_advertised_top_app_share", 0.60)):
        failures.append("advertised_top_app_too_high")
    if giant_developer_share > float(rules.get("max_giant_developer_share", 0.50)):
        failures.append("giant_share_too_high")
    if single_developer_share > float(rules.get("max_single_developer_share", 0.70)):
        failures.append("single_developer_share_too_high")

    if bool(rules.get("block_single_app_breakout_as_regular_alert", True)):
        if app_count < 2 or "single_app_breakout" in candidate.get("reason_codes", []):
            failures.append("single_app_breakout_not_regular_alert")

    normalized_niche = str(candidate.get("normalized_niche") or candidate.get("niche") or "other").lower()
    unknown_pattern_blocker_active = bool(candidate.get("unknown_pattern_blocker_active"))
    if bool(rules.get("block_unknown_or_new_pattern_if_low_confidence", True)) and unknown_pattern_blocker_active:
        failures.append("unknown_pattern_blocker_active")
    if (
        bool(rules.get("block_other_niche_if_low_confidence", True))
        and normalized_niche == "other"
        and unknown_pattern_blocker_active
        and confidence < 0.70
    ):
        failures.append("other_niche_low_confidence")

    risk_tags = set(str(tag) for tag in candidate.get("risk_tags", []))
    blocked = risk_tags & set(str(tag) for tag in rules.get("blocked_risk_tags", []))
    if blocked:
        failures.append("blocked_risk_tag")

    organic_confidence = str(candidate.get("organic_confidence") or "").upper()
    if organic_confidence == "LOW":
        failures.append("organic_confidence_low")

    return not failures, sorted(set(failures))


def enrich_sendable_alert_fields(candidates: list[dict[str, Any]], config: dict[str, Any]) -> list[dict[str, Any]]:
    enriched: list[dict[str, Any]] = []
    for candidate in candidates:
        item = dict(candidate)
        fill_signal_defaults(item)
        organic_label, organic_score, organic_reasons = calculate_organic_confidence(item)
        item.setdefault("organic_confidence", organic_label)
        item.setdefault("organic_confidence_score", organic_score)
        item.setdefault("organic_confidence_reasons", organic_reasons)

        trend_score, trend_reasons, trend_failures = calculate_trend_confidence_score(item, config)
        team_score, team_reasons, team_failures = calculate_team_fit_score(item, config)
        sendable_score, score_reasons, score_failures, components = calculate_sendable_score_with_inputs(
            item,
            config,
            trend_score,
            team_score,
        )
        hard_passed, hard_failures = passes_sendable_hard_filters(
            {
                **item,
                "trend_confidence_score": trend_score,
                "team_fit_score": team_score,
                "sendable_alert_score": sendable_score,
            },
            config,
        )

        item["trend_confidence_score"] = trend_score
        item["team_fit_score"] = team_score
        item["sendable_alert_score"] = sendable_score
        item["sendable_score_components"] = components
        item["sendable_threshold_margins"] = calculate_sendable_threshold_margins(
            {
                **item,
                "trend_confidence_score": trend_score,
                "team_fit_score": team_score,
                "sendable_alert_score": sendable_score,
            },
            config,
        )
        item.setdefault("sendable_alert_rank", None)
        item.setdefault("send_regular_alert", False)
        item.setdefault("telegram_delivery_channel", "none")
        item.setdefault("alert_filter_reasons", [])

        reasons = list(item.get("sendable_alert_reasons", []))
        failures = list(item.get("sendable_alert_failures", []))
        reasons.extend(score_reasons + trend_reasons + team_reasons)
        new_failures = score_failures + trend_failures + team_failures + hard_failures
        failures.extend(new_failures)
        if new_failures and not item.get("first_blocking_failure"):
            item["first_blocking_failure"] = str(new_failures[0])
        else:
            item.setdefault("first_blocking_failure", None)
        if item.get("status") == "ALERT":
            reasons.append("qualified_alert_candidate")
            item.setdefault("alert_stage", "QUALIFIED_CANDIDATE")
        else:
            item.setdefault("alert_stage", "NONE")
        if hard_passed:
            reasons.append("passed_sendable_hard_filters")

        item["sendable_alert_reasons"] = sorted(set(str(reason) for reason in reasons))
        item["sendable_alert_failures"] = sorted(set(str(reason) for reason in failures))
        assign_blocker_fields(item, config)
        item["alert_strength"] = calculate_alert_strength(item, config)
        enriched.append(item)
    return enriched


def assign_blocker_fields(candidate: dict[str, Any], config: dict[str, Any]) -> None:
    hard_blockers, soft_blockers = classify_blockers(candidate, config)
    candidate["hard_blockers"] = hard_blockers
    candidate["soft_blockers"] = soft_blockers
    candidate["hard_blockers_count"] = len(hard_blockers)
    candidate["soft_blockers_count"] = len(soft_blockers)


def classify_blockers(candidate: dict[str, Any], config: dict[str, Any]) -> tuple[list[str], list[str]]:
    rules = sendable_rules(config)
    failures = set(str(failure) for failure in candidate.get("sendable_alert_failures", []))
    risk_tags = set(str(tag) for tag in candidate.get("risk_tags", []))
    hard: set[str] = set()
    soft: set[str] = set()

    quality = score_100(candidate, "data_quality_score")
    confidence = ratio_metric(candidate, "classification_confidence_avg", default=0.0)
    mvp_feasibility = score_100(candidate, "mvp_feasibility_score")
    top_app_share = ratio_metric(candidate, "top_app_share")
    growth_by_one_app_share = ratio_metric(candidate, "growth_by_one_app_share")

    hard_quality_min = normalized_threshold_100(rules.get("hard_alert_min_data_quality_score", 60.0))
    hard_confidence_min = float(rules.get("hard_alert_min_classification_confidence", 0.50))
    hard_mvp_min = normalized_threshold_100(rules.get("hard_alert_min_mvp_feasibility_score", 50.0))
    hard_top_app_max = float(rules.get("hard_alert_max_top_app_share", 0.75))
    hard_growth_max = float(rules.get("hard_alert_max_growth_by_one_app_share", 0.75))

    for code in (
        "severe_paid_spike",
        "duplicate_market_signal",
        "market_signal_duplicate",
        "cooldown_exact_dedupe_key",
        "cooldown_normalized_niche",
        "unknown_pattern_blocker_active",
        "organic_confidence_low",
        "sendable_hard_filter_failed",
    ):
        if code in failures:
            hard.add(code)
    if "blocked_risk_tag" in failures:
        hard.add("blocked_risk_tag")
    if "severe_paid_spike" in risk_tags or bool(candidate.get("severe_paid_spike_risk")):
        hard.add("severe_paid_spike")
    if bool(candidate.get("unknown_pattern_blocker_active")):
        hard.add("unknown_pattern_blocker_active")
    if str(candidate.get("organic_confidence") or "").upper() == "LOW":
        hard.add("organic_confidence_low")
    if top_app_share > hard_top_app_max:
        hard.add("top_app_share_above_hard_max")
    if growth_by_one_app_share > hard_growth_max:
        hard.add("growth_by_one_app_share_above_hard_max")
    if quality < hard_quality_min:
        hard.add("data_quality_below_hard_min")
    if confidence < hard_confidence_min:
        hard.add("classification_confidence_below_hard_min")
    if mvp_feasibility < hard_mvp_min:
        hard.add("mvp_feasibility_below_hard_min")

    for code in (
        "below_sendable_alert_score",
        "below_opportunity_score",
        "below_trend_confidence_score",
        "below_team_fit_score",
        "too_few_apps_for_sendable",
        "too_few_successful_new_apps",
        "too_few_unique_developers",
        "low_total_daily_installs",
        "top3_too_dominant",
        "advertised_top_app_too_high",
        "giant_share_too_high",
        "single_developer_share_too_high",
        "single_app_breakout_not_regular_alert",
        "other_niche_low_confidence",
        "no_growth_history",
        "below_data_quality_for_trend_confidence",
        "low_classification_confidence",
        "low_mvp_feasibility",
    ):
        if code in failures:
            soft.add(code)
    if "below_data_quality_score" in failures:
        if quality < hard_quality_min:
            hard.add("data_quality_below_hard_min")
        else:
            soft.add("below_data_quality_score")
    if "below_classification_confidence" in failures:
        if confidence < hard_confidence_min:
            hard.add("classification_confidence_below_hard_min")
        else:
            soft.add("below_classification_confidence")
    if "below_mvp_feasibility" in failures:
        if mvp_feasibility < hard_mvp_min:
            hard.add("mvp_feasibility_below_hard_min")
        else:
            soft.add("below_mvp_feasibility")
    if "top_app_too_dominant" in failures:
        if top_app_share > hard_top_app_max:
            hard.add("top_app_share_above_hard_max")
        else:
            soft.add("top_app_too_dominant")
    if "growth_by_one_app_too_high" in failures:
        if growth_by_one_app_share > hard_growth_max:
            hard.add("growth_by_one_app_share_above_hard_max")
        else:
            soft.add("growth_by_one_app_too_high")

    if "weak_revenue_signal" in risk_tags:
        soft.add("weak_revenue_signal")
    if "weak_monetization_signal" in risk_tags:
        soft.add("weak_monetization_signal")
    if "possible_paid_spike" in risk_tags:
        soft.add("possible_paid_spike")
    if "mixed_unknown_cluster" in risk_tags and "unknown_pattern_blocker_active" not in hard:
        soft.add("mixed_unknown_cluster")

    soft.difference_update(hard)
    return sorted(hard), sorted(soft)


def calculate_alert_strength(candidate: dict[str, Any], config: dict[str, Any]) -> str:
    if candidate.get("status") != "ALERT":
        return "NONE"
    risk_tags = set(str(tag) for tag in candidate.get("risk_tags", []))
    if (
        score_100(candidate, "opportunity_score") >= 75.0
        and score_100(candidate, "data_quality_score") >= 60.0
        and ratio_metric(candidate, "classification_confidence_avg", default=0.0) >= 0.55
        and int_metric(candidate, "app_count") >= 3
        and successful_new_apps_count(candidate) >= 2
        and unique_developer_count(candidate) >= 2
        and str(candidate.get("organic_confidence") or "").upper() != "LOW"
        and not bool(candidate.get("unknown_pattern_blocker_active"))
        and "severe_paid_spike" not in risk_tags
        and ratio_metric(candidate, "top_app_share") <= 0.75
        and ratio_metric(candidate, "growth_by_one_app_share") <= 0.80
    ):
        return "STRONG_ALERT"
    if (
        score_100(candidate, "opportunity_score") >= 70.0
        and score_100(candidate, "data_quality_score") >= 55.0
        and ratio_metric(candidate, "classification_confidence_avg", default=0.0) >= 0.50
    ):
        return "MEDIUM_ALERT"
    return "WEAK_ALERT"


def calculate_sendable_score_with_inputs(
    candidate: dict[str, Any],
    config: dict[str, Any],
    trend_score: float,
    team_score: float,
) -> tuple[float, list[str], list[str], dict[str, float]]:
    rules = sendable_rules(config)
    reasons: list[str] = []
    failures: list[str] = []
    opportunity_score = score_100(candidate, "opportunity_score")
    quality = score_100(candidate, "data_quality_score")
    classification_confidence = ratio_metric(candidate, "classification_confidence_avg", default=0.70)
    top_app_share = ratio_metric(candidate, "top_app_share")
    growth_by_one_app_share = ratio_metric(candidate, "growth_by_one_app_share")
    advertised_top_app_share = ratio_metric(candidate, "advertised_top_app_share")
    unknown_app_share = ratio_metric(candidate, "unknown_app_share")
    unknown_installs_share = ratio_metric(candidate, "unknown_installs_share")
    risk_tags = set(str(tag) for tag in candidate.get("risk_tags", []))

    opportunity_component = opportunity_score * 0.40
    trend_component = trend_score * 0.30
    team_component = team_score * 0.20
    data_quality_component = quality / 10.0
    concentration_penalty = -1.0 * max(top_app_share - 0.45, 0.0) * 40.0
    concentration_penalty += -1.0 * max(growth_by_one_app_share - 0.45, 0.0) * 35.0
    paid_spike_penalty = -1.0 * max(advertised_top_app_share - 0.35, 0.0) * 35.0
    classifier_penalty = -1.0 * max(float(rules.get("min_classification_confidence_avg", 0.60)) - classification_confidence, 0.0) * 25.0

    soft_penalty_tags = set(str(tag) for tag in rules.get("soft_penalty_risk_tags", []))
    risk_penalty = -4.0 * len(risk_tags & soft_penalty_tags)
    if "severe_paid_spike" in risk_tags:
        risk_penalty -= 20.0
    elif "possible_paid_spike" in risk_tags:
        risk_penalty -= 8.0

    final = clamp(
        opportunity_component
        + trend_component
        + team_component
        + data_quality_component
        + concentration_penalty
        + paid_spike_penalty
        + classifier_penalty
        + risk_penalty
    )
    min_score = float(rules.get("min_sendable_alert_score", 80.0))
    if final >= min_score:
        reasons.append("high_sendable_alert_score")
    else:
        failures.append("below_sendable_alert_score")
    if concentration_penalty == 0.0:
        reasons.append("low_concentration")
    if paid_spike_penalty == 0.0 and "severe_paid_spike" not in risk_tags:
        reasons.append("no_paid_spike_blocker")

    components = {
        "opportunity_score_component": round(opportunity_component, 2),
        "trend_confidence_component": round(trend_component, 2),
        "team_fit_component": round(team_component, 2),
        "data_quality_component": round(data_quality_component, 2),
        "concentration_penalty": round(concentration_penalty, 2),
        "paid_spike_penalty": round(paid_spike_penalty, 2),
        "classifier_penalty": round(classifier_penalty, 2),
        "risk_penalty": round(risk_penalty, 2),
        "unknown_app_share": round(unknown_app_share, 4),
        "unknown_installs_share": round(unknown_installs_share, 4),
        "final": round(final, 2),
    }
    return round(final, 2), reasons, failures, components


def calculate_sendable_threshold_margins(
    candidate: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, float]:
    rules = sendable_rules(config)
    opportunity_score = score_100(candidate, "opportunity_score")
    sendable_score = float_metric(candidate, "sendable_alert_score")
    trend_score = float_metric(candidate, "trend_confidence_score")
    team_score = float_metric(candidate, "team_fit_score")
    quality = score_100(candidate, "data_quality_score")
    confidence = ratio_metric(candidate, "classification_confidence_avg", default=0.0)
    mvp_feasibility = score_100(candidate, "mvp_feasibility_score")
    app_count = int_metric(candidate, "app_count")
    successful_new_apps = successful_new_apps_count(candidate)
    unique_developers = unique_developer_count(candidate)
    total_daily = int_metric(candidate, "total_daily_installs")
    top_app_share = ratio_metric(candidate, "top_app_share")
    top3_app_share = ratio_metric(candidate, "top3_app_share", default=top_app_share)
    growth_by_one_app_share = ratio_metric(candidate, "growth_by_one_app_share")
    advertised_top_app_share = ratio_metric(candidate, "advertised_top_app_share")
    giant_developer_share = ratio_metric(candidate, "giant_developer_share")
    single_developer_share = ratio_metric(candidate, "single_developer_share")
    unknown_app_share = ratio_metric(candidate, "unknown_app_share")
    unknown_installs_share = ratio_metric(candidate, "unknown_installs_share")
    return {
        "sendable_alert_score": round(sendable_score - float(rules.get("min_sendable_alert_score", 80.0)), 4),
        "opportunity_score": round(opportunity_score - float(rules.get("min_opportunity_score", 75.0)), 4),
        "trend_confidence_score": round(trend_score - float(rules.get("min_trend_confidence_score", 65.0)), 4),
        "team_fit_score": round(team_score - float(rules.get("min_team_fit_score", 60.0)), 4),
        "data_quality_score": round(quality - normalized_threshold_100(rules.get("min_data_quality_score", 70.0)), 4),
        "classification_confidence_avg": round(
            confidence - float(rules.get("min_classification_confidence_avg", 0.60)),
            4,
        ),
        "mvp_feasibility_score": round(mvp_feasibility - float(rules.get("min_mvp_feasibility_score", 60.0)), 4),
        "app_count": round(app_count - int(rules.get("min_app_count", 3)), 4),
        "successful_new_apps_count": round(successful_new_apps - int(rules.get("min_successful_new_apps", 2)), 4),
        "unique_developer_count": round(unique_developers - int(rules.get("min_unique_developers", 2)), 4),
        "total_daily_installs": round(total_daily - int(rules.get("min_total_daily_installs", 3000)), 4),
        "top_app_share": round(float(rules.get("max_top_app_share", 0.60)) - top_app_share, 4),
        "top3_app_share": round(float(rules.get("max_top3_app_share", 0.85)) - top3_app_share, 4),
        "growth_by_one_app_share": round(
            float(rules.get("max_growth_by_one_app_share", 0.65)) - growth_by_one_app_share,
            4,
        ),
        "advertised_top_app_share": round(
            float(rules.get("max_advertised_top_app_share", 0.60)) - advertised_top_app_share,
            4,
        ),
        "giant_developer_share": round(float(rules.get("max_giant_developer_share", 0.50)) - giant_developer_share, 4),
        "single_developer_share": round(
            float(rules.get("max_single_developer_share", 0.70)) - single_developer_share,
            4,
        ),
        "unknown_app_share_to_dominance": round(0.50 - unknown_app_share, 4),
        "unknown_installs_share_to_dominance": round(0.60 - unknown_installs_share, 4),
        "classification_confidence_for_unknown_blocker": round(confidence - 0.70, 4),
    }


def calculate_organic_confidence(candidate: dict[str, Any]) -> tuple[str, float, list[str]]:
    reasons: list[str] = []
    app_count = int_metric(candidate, "app_count")
    unique_developers = unique_developer_count(candidate)
    top_app_share = ratio_metric(candidate, "top_app_share")
    growth_by_one_app_share = ratio_metric(candidate, "growth_by_one_app_share")
    advertised_top_app_share = ratio_metric(candidate, "advertised_top_app_share")
    rating_count_total = int_metric(candidate, "rating_count_total")
    total_daily = int_metric(candidate, "total_daily_installs")
    risk_tags = set(str(tag) for tag in candidate.get("risk_tags", []))

    score = 50.0
    if app_count >= 3 and unique_developers >= 2:
        score += 25.0
        reasons.append("organic_confidence_high_multi_developer")
    if top_app_share <= 0.60 and growth_by_one_app_share <= 0.60:
        score += 15.0
    if advertised_top_app_share in (0.0, None) or advertised_top_app_share <= 0.35:
        score += 10.0
    elif advertised_top_app_share >= 0.60:
        score -= 30.0
        reasons.append("organic_confidence_low_paid_spike")
    else:
        score -= 10.0
        reasons.append("organic_confidence_medium_incomplete_ad_data")
    if top_app_share >= 0.75:
        score -= 35.0
        reasons.append("organic_confidence_low_top_app_dominance")
    if growth_by_one_app_share >= 0.75:
        score -= 30.0
        reasons.append("organic_confidence_low_growth_by_one_app")
    if "severe_paid_spike" in risk_tags:
        score -= 50.0
        reasons.append("organic_confidence_low_paid_spike")
    elif "possible_paid_spike" in risk_tags:
        score -= 15.0
        reasons.append("organic_confidence_medium_incomplete_ad_data")
    if total_daily >= 10000 and 0 < rating_count_total < 20:
        score -= 20.0
        reasons.append("organic_confidence_low_review_download_mismatch")

    score = clamp(score)
    if score >= 75.0:
        label = "HIGH"
    elif score >= 45.0:
        label = "MEDIUM"
    else:
        label = "LOW"
    return label, round(score, 2), sorted(set(reasons))


def fill_signal_defaults(candidate: dict[str, Any]) -> None:
    top_apps = candidate.get("top_apps", [])
    if not isinstance(top_apps, list):
        top_apps = []
    total_daily = int_metric(candidate, "total_daily_installs")
    top3_daily = sum(int(app.get("downloads_daily", 0)) for app in top_apps[:3] if isinstance(app, dict))
    unique_developers = unique_developer_count(candidate)
    app_count = int_metric(candidate, "app_count")
    successful_new = successful_new_apps_count(candidate)
    candidate.setdefault("unique_developer_count", unique_developers)
    candidate.setdefault("developer_diversity_score", round(min(safe_div(unique_developers, max(app_count, 1)), 1.0), 4))
    candidate.setdefault("fresh_success_ratio", round(safe_div(successful_new, max(app_count, 1)), 4))
    candidate.setdefault("top3_app_share", round(safe_div(top3_daily, total_daily), 4) if total_daily > 0 else ratio_metric(candidate, "top_app_share"))
    candidate.setdefault(
        "cluster_diversity_score",
        round(
            (
                min(safe_div(unique_developers, max(app_count, 1)), 1.0)
                + max(1.0 - ratio_metric(candidate, "top_app_share"), 0.0)
            )
            / 2.0,
            4,
        ),
    )


def successful_new_apps_count(candidate: dict[str, Any]) -> int:
    return int_metric(candidate, "successful_new_apps_count", fallback_keys=["successful_new_apps"])


def unique_developer_count(candidate: dict[str, Any]) -> int:
    existing = candidate.get("unique_developer_count")
    if existing not in (None, ""):
        return int_metric(candidate, "unique_developer_count")
    top_apps = candidate.get("top_apps", [])
    if not isinstance(top_apps, list):
        return 0
    developers = {
        str(app.get("developer_id") or app.get("developer_name"))
        for app in top_apps
        if isinstance(app, dict) and (app.get("developer_id") or app.get("developer_name"))
    }
    return len(developers)


def int_metric(candidate: dict[str, Any], key: str, *, fallback_keys: list[str] | None = None) -> int:
    value = first_metric(candidate, key, fallback_keys or [])
    try:
        return int(float(str(value).replace(",", "")))
    except (TypeError, ValueError):
        return 0


def float_metric(candidate: dict[str, Any], key: str, *, default: float = 0.0) -> float:
    value = first_metric(candidate, key, [])
    if value in (None, ""):
        return default
    try:
        return float(str(value).replace(",", ""))
    except (TypeError, ValueError):
        return default


def score_100(candidate: dict[str, Any], key: str, *, default: float = 0.0) -> float:
    value = float_metric(candidate, key, default=default)
    if 0.0 <= value <= 1.0:
        return value * 100.0
    return clamp(value)


def ratio_metric(candidate: dict[str, Any], key: str, *, default: float = 0.0) -> float:
    value = float_metric(candidate, key, default=default)
    if value > 1.0:
        return clamp(value, 0.0, 100.0) / 100.0
    return clamp(value, 0.0, 1.0)


def normalized_threshold_100(value: Any) -> float:
    try:
        threshold = float(value)
    except (TypeError, ValueError):
        return 70.0
    if 0.0 <= threshold <= 1.0:
        return threshold * 100.0
    return threshold


def first_metric(candidate: dict[str, Any], key: str, fallback_keys: list[str]) -> Any:
    for candidate_key in [key, *fallback_keys]:
        if candidate.get(candidate_key) not in (None, ""):
            return candidate.get(candidate_key)
    return None
