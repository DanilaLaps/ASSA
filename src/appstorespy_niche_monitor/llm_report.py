from __future__ import annotations

import json
import os
import urllib.request
from typing import Any

from .localization import (
    contains_non_russian_human_text,
    describe_reason_code,
    describe_risk_tag,
    ru_fallback_reason,
)


ANALYSIS_FIELDS = (
    "summary",
    "signal",
    "evidence",
    "entry_realism",
    "mvp",
    "monetization",
    "risks",
    "checks",
    "recommendation",
)

PACK_ANALYSIS_FIELDS = (
    "recommendation",
    "confidence",
    "why_interesting",
    "why_might_be_false_positive",
    "mvp_hypothesis",
    "simplified_mvp_scope",
    "competitor_takeaways",
    "entry_angle",
    "differentiation_idea",
    "why_top_products_validate_or_weaken_signal",
    "validation_steps",
    "risk_notes",
    "missing_data",
    "manual_review_needed",
)

PACK_HUMAN_READABLE_FIELDS = (
    "why_interesting",
    "why_might_be_false_positive",
    "mvp_hypothesis",
    "simplified_mvp_scope",
    "competitor_takeaways",
    "entry_angle",
    "differentiation_idea",
    "why_top_products_validate_or_weaken_signal",
    "validation_steps",
    "risk_notes",
    "missing_data",
)


def analyze_candidate_pack(
    candidates: list[dict[str, Any]],
    config: dict[str, Any],
    *,
    use_llm: bool = True,
    coverage_summary: dict[str, Any] | None = None,
    history_summary: dict[str, Any] | None = None,
) -> dict[str, Any]:
    pack_input = build_candidate_pack_input(candidates, config, coverage_summary, history_summary)
    fallback = generate_fallback_pack_analysis(pack_input)
    llm_status = build_llm_status(pack_input, config, use_llm=use_llm)
    fallback["llm_status"] = llm_status
    if llm_status.get("fallback_reason"):
        fallback["llm_fallback_note"] = llm_status.get("fallback_reason")
        fallback["llm_fallback_note_ru"] = f"ИИ-анализ не запускался: {ru_fallback_reason(llm_status.get('fallback_reason'))}."
    if not llm_status.get("should_call_openai"):
        return fallback
    try:
        return generate_openai_pack_analysis(pack_input, config, fallback, llm_status)
    except Exception as exc:  # pragma: no cover - network fallback
        llm_status = {
            **llm_status,
            "analysis_source": "fallback",
            "fallback_reason": "openai_error",
            "fallback_detail": str(exc),
        }
        fallback["llm_status"] = llm_status
        fallback["llm_fallback_note"] = f"openai_error: {exc}"
        fallback["llm_fallback_note_ru"] = "ИИ-анализ недоступен: OpenAI вернул ошибку, используется fallback-анализ."
    return fallback


def build_llm_status(pack_input: dict[str, Any], config: dict[str, Any], *, use_llm: bool) -> dict[str, Any]:
    llm_cfg = config.get("llm", {})
    enabled = bool(llm_cfg.get("enabled", True))
    model_env = str(llm_cfg.get("model_env", "OPENAI_MODEL"))
    model = os.environ.get(model_env) or llm_cfg.get("default_model", "gpt-4.1-mini")
    api_key_present = bool(os.environ.get("OPENAI_API_KEY"))
    counts = {
        "alerts": len(pack_input.get("alerts", [])),
        "watch": len(pack_input.get("watch", [])),
        "near_misses": len(pack_input.get("near_misses", [])),
        "initial_baseline_digest": len(pack_input.get("initial_baseline_digest", [])),
    }
    if not use_llm:
        source = "fallback"
        reason = "disabled_by_cli"
    elif not enabled:
        source = "fallback"
        reason = "disabled_in_config"
    elif counts["alerts"] <= 0:
        source = "fallback"
        reason = "no_sendable_alerts"
    elif not api_key_present:
        source = "fallback"
        reason = "missing_openai_api_key"
    else:
        source = "openai_pending"
        reason = None
    return {
        "analysis_source": source,
        "should_call_openai": source == "openai_pending",
        "fallback_reason": reason,
        "requested": bool(use_llm),
        "enabled": enabled,
        "api_key_present": api_key_present,
        "api_key_env": "OPENAI_API_KEY",
        "model": model,
        "model_env": model_env,
        "candidate_counts": counts,
    }


def build_candidate_pack_input(
    candidates: list[dict[str, Any]],
    config: dict[str, Any],
    coverage_summary: dict[str, Any] | None = None,
    history_summary: dict[str, Any] | None = None,
) -> dict[str, Any]:
    limits = config.get("alert_limits", {})
    alerts = select_alerts_for_llm(candidates, int(limits.get("max_alerts_per_run", 3)))
    return {
        "alerts": [compact_candidate_for_llm(item) for item in alerts],
        "watch": [],
        "near_misses": [],
        "initial_baseline_digest": [],
        "coverage_summary": coverage_summary or coverage_from_candidates(candidates),
        "history_summary": history_summary or {},
        "rules_summary": {
            "candidate_generation": config.get("candidate_generation", {}),
            "alert_limits": config.get("alert_limits", {}),
            "important_risk_tags": [
                "leader_dominated",
                "possible_paid_spike",
                "severe_paid_spike",
                "giant_developer_risk",
                "weak_revenue_signal",
                "sample_truncated",
                "unknown_coverage",
            ],
        },
    }


def select_alerts_for_llm(candidates: list[dict[str, Any]], max_alerts: int) -> list[dict[str, Any]]:
    return [
        item
        for item in candidates
        if item.get("status") == "ALERT"
        and item.get("send_regular_alert") is True
        and item.get("alert_stage") == "SENDABLE_ALERT"
    ][:max_alerts]


def compact_candidate_for_llm(candidate: dict[str, Any]) -> dict[str, Any]:
    fields = (
        "candidate_id",
        "dedupe_key",
        "status",
        "would_be_status",
        "platform",
        "niche",
        "normalized_niche",
        "group_key_type",
        "group_key_value",
        "source_scope",
        "release_date_window",
        "collection_sort",
        "min_app_daily_installs",
        "market_category",
        "core_mechanic",
        "theme",
        "meta",
        "audience",
        "audience_summary",
        "production_complexity",
        "full_product_complexity",
        "mvp_complexity",
        "simplifiable",
        "simplification_idea",
        "app_count",
        "total_daily_installs",
        "avg_daily_installs",
        "median_daily_installs",
        "total_monthly_downloads",
        "total_monthly_revenue",
        "avg_rating",
        "rating_count_total",
        "successful_new_apps_count",
        "traction_fresh_apps_count",
        "top_app_share",
        "growth_by_one_app_share",
        "advertised_top_app_share",
        "giant_developer_share",
        "single_developer_share",
        "opportunity_score",
        "score_components",
        "data_quality_score",
        "organic_confidence",
        "organic_confidence_score",
        "organic_confidence_reasons",
        "mvp_feasibility_score",
        "trend_confidence_score",
        "team_fit_score",
        "sendable_alert_score",
        "sendable_alert_rank",
        "sendable_score_components",
        "sendable_threshold_margins",
        "sendable_alert_reasons",
        "sendable_alert_failures",
        "first_blocking_failure",
        "alert_stage",
        "telegram_delivery_channel",
        "market_signal_key",
        "market_signal_label",
        "risk_tags",
        "reason_codes",
        "failed_alert_conditions",
        "alert_filter_reasons",
        "confidence_level",
        "classification_confidence_avg",
        "unknown_app_count",
        "unknown_app_share",
        "unknown_installs_share",
        "top_app_unknown",
        "top3_unknown_app_share",
        "mixed_unknown_cluster",
        "unknown_dominant_cluster",
        "unknown_pattern_blocker_active",
        "cluster_pattern_status",
        "unknown_or_new_pattern_cluster",
        "first_run_without_history",
        "send_regular_alert",
    )
    compact = {field: candidate.get(field) for field in fields if field in candidate}
    top_apps = [compact_top_product_for_llm(app) for app in candidate.get("top_apps", [])[:5]]
    compact["top_apps"] = top_apps
    compact["top_products"] = top_apps[:3]
    compact["top_competitors"] = top_apps[:3]
    return compact


def compact_top_product_for_llm(app: dict[str, Any]) -> dict[str, Any]:
    return {
        "app_id": app.get("app_id"),
        "bundle": app.get("bundle"),
        "name": app.get("name"),
        "developer_name": app.get("developer_name"),
        "developer_id": app.get("developer_id"),
        "category": app.get("category"),
        "category_type": app.get("category_type"),
        "downloads_daily": app.get("downloads_daily"),
        "downloads_month": app.get("downloads_month"),
        "downloads_exact": app.get("downloads_exact"),
        "downloads_mark": app.get("downloads_mark"),
        "revenue_month": app.get("revenue_month"),
        "rating_avg": app.get("rating_avg"),
        "rating_count": app.get("rating_count"),
        "review_count": app.get("review_count"),
        "release_date": app.get("release_date"),
        "update_date": app.get("update_date"),
        "advertised": app.get("advertised"),
        "ads": app.get("ads"),
        "iap": app.get("iap"),
        "icon": app.get("icon"),
        "screenshots": list(app.get("screenshots", [])[:3]) if isinstance(app.get("screenshots"), list) else [],
        "description_short": truncate_text(app.get("description_short", ""), 500),
        "description_excerpt": truncate_text(
            app.get("description_excerpt") or app.get("description_full") or app.get("description", ""),
            1200,
        ),
        "url_appstorespy": app.get("url_appstorespy"),
        "url": app.get("url"),
        "website": app.get("website"),
        "is_unknown_or_new_pattern": app.get("is_unknown_or_new_pattern"),
    }


def truncate_text(value: Any, max_chars: int) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 3].rstrip() + "..."


def coverage_from_candidates(candidates: list[dict[str, Any]]) -> dict[str, Any]:
    for candidate in candidates:
        coverage = candidate.get("coverage")
        if isinstance(coverage, dict) and coverage:
            return coverage
    return {}


def generate_fallback_pack_analysis(pack_input: dict[str, Any]) -> dict[str, Any]:
    all_candidates = (
        pack_input.get("alerts", [])
        + pack_input.get("watch", [])
        + pack_input.get("near_misses", [])
        + pack_input.get("initial_baseline_digest", [])
    )
    candidate_analyses = {
        str(item.get("candidate_id")): generate_pack_item_fallback(item)
        for item in all_candidates
        if item.get("candidate_id")
    }
    return {
        "analysis_source": "fallback",
        "candidate_analysis_sources": {
            candidate_id: "fallback" for candidate_id in candidate_analyses
        },
        "pack_input": pack_input,
        "candidate_analyses": candidate_analyses,
    }


def generate_pack_item_fallback(candidate: dict[str, Any]) -> dict[str, Any]:
    status = candidate.get("status")
    first_run = bool(candidate.get("first_run_without_history"))
    severe = "severe_paid_spike" in candidate.get("risk_tags", [])
    if severe or "giant_developer_risk" in candidate.get("risk_tags", []):
        recommendation = "AVOID"
    elif status == "ALERT" and not first_run:
        recommendation = "TEST"
    else:
        recommendation = "WATCH"
    confidence = "medium" if first_run else ("high" if float(candidate.get("data_quality_score", 0.0)) >= 75 else "medium")
    if float(candidate.get("data_quality_score", 0.0)) < 45:
        confidence = "low"
    reason_codes = candidate.get("reason_codes", [])
    why_interesting = (
        [describe_reason_code(code) for code in reason_codes[:3]]
        if reason_codes
        else ["Кандидат прошел детерминированные scoring-сигналы в одном AppStoreSpy query-срезе."]
    )
    risk_tags = candidate.get("risk_tags", [])
    risk_notes = (
        [describe_risk_tag(tag) for tag in risk_tags]
        if risk_tags
        else ["Нужна ручная проверка, потому что один AppStoreSpy query-срез не подтверждает рынок полностью."]
    )
    mvp_hypothesis = (
        f"Проверить узкий MVP вокруг механики {candidate.get('core_mechanic')} "
        f"с темой {candidate.get('theme')} и коротким core-loop."
    )
    top_products = candidate.get("top_products") or candidate.get("top_competitors") or candidate.get("top_apps", [])[:3]
    product_names = [str(app.get("name")) for app in top_products if isinstance(app, dict) and app.get("name")]
    competitor_takeaways = (
        [f"Top products из этого query-среза: {', '.join(product_names[:3])}."]
        if product_names
        else ["Top products для конкурентного просмотра не найдены в срезе."]
    )
    return {
        "recommendation": recommendation,
        "confidence": confidence,
        "why_interesting": why_interesting,
        "why_might_be_false_positive": risk_notes[:4],
        "mvp_hypothesis": mvp_hypothesis,
        "simplified_mvp_scope": "Один core-loop, одна контентная тема, легкая meta-прогрессия.",
        "competitor_takeaways": competitor_takeaways,
        "entry_angle": (
            f"Использовать спрос на {candidate.get('core_mechanic')}, но сузить scope, тему и глубину контента."
        ),
        "differentiation_idea": (
            "Отличаться более ясным first-session UX, меньшей стоимостью контента и отдельным store creative angle."
        ),
        "why_top_products_validate_or_weaken_signal": (
            "Top products помогают проверить спрос, но концентрацию, ads и долю крупных разработчиков нужно проверить вручную."
        ),
        "validation_steps": [
            "Проверить top apps вручную в AppStoreSpy и сторах.",
            "Отделить органическую traction от paid acquisition.",
            "Проверить creatives и monetization-сигналы до production.",
        ],
        "risk_notes": risk_notes,
        "missing_data": [
            describe_reason_code(condition) for condition in candidate.get("failed_alert_conditions", [])
        ],
        "manual_review_needed": status in {"WATCH", "SINGLE_APP_WATCH", "NEAR_MISS"} or first_run,
        "summary": (
            f"{candidate.get('normalized_niche')} выглядит как {recommendation}-кандидат в одном AppStoreSpy query-срезе."
        ),
        "signal": ", ".join(why_interesting) or "Кандидат прошел детерминированные scoring-сигналы.",
        "evidence": why_interesting,
        "entry_realism": f"MVP feasibility score: {candidate.get('mvp_feasibility_score')}.",
        "mvp": mvp_hypothesis,
        "monetization": "Проверить ads/IAP/revenue-сигналы до production.",
        "risks": risk_notes or ["Нужна ручная валидация."],
        "checks": [
            "Проверить top apps вручную в AppStoreSpy и сторах.",
            "Подтвердить, что сигнал не является paid traffic.",
        ],
    }


def generate_openai_pack_analysis(
    pack_input: dict[str, Any],
    config: dict[str, Any],
    fallback: dict[str, Any],
    llm_status: dict[str, Any] | None = None,
) -> dict[str, Any]:
    llm_cfg = config.get("llm", {})
    model = os.environ.get(llm_cfg.get("model_env", "OPENAI_MODEL")) or llm_cfg.get("default_model", "gpt-4.1-mini")
    payload: dict[str, Any] = {
        "model": model,
        "input": build_pack_prompt(pack_input),
    }
    if llm_cfg.get("max_output_tokens") is not None:
        payload["max_output_tokens"] = int(llm_cfg.get("max_output_tokens", 6000))
    request = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(request, timeout=int(llm_cfg.get("timeout_seconds", 60))) as response:
        data = json.loads(response.read().decode("utf-8"))
    parsed = parse_json_object(extract_response_text(data))
    raw_candidate_analyses = parsed.get("candidate_analyses")
    fallback_analyses = fallback.get("candidate_analyses", {})
    if not isinstance(raw_candidate_analyses, dict):
        raise ValueError("OpenAI response missing candidate_analyses object.")
    candidate_analyses = dict(fallback_analyses)
    candidate_analysis_sources = {
        candidate_id: "fallback_missing_from_openai"
        for candidate_id in fallback_analyses
    }
    expected_ids = set(fallback_analyses)
    openai_candidate_analyses_count = 0
    for candidate_id, analysis in raw_candidate_analyses.items():
        candidate_key = str(candidate_id)
        if expected_ids and candidate_key not in expected_ids:
            continue
        if not isinstance(analysis, dict):
            continue
        normalized_analysis = normalize_pack_item_analysis(
            analysis,
            fallback_analyses.get(candidate_key, {}),
        )
        if pack_item_has_non_russian_text(normalized_analysis):
            normalized_analysis["llm_language_warning"] = "non_russian_text_detected"
        candidate_analyses[candidate_key] = normalized_analysis
        candidate_analysis_sources[candidate_key] = "openai"
        openai_candidate_analyses_count += 1
    if expected_ids and openai_candidate_analyses_count == 0:
        raise ValueError("OpenAI response contained no usable candidate analyses.")
    parsed["candidate_analyses"] = candidate_analyses
    parsed["candidate_analysis_sources"] = candidate_analysis_sources
    parsed["analysis_source"] = "openai"
    parsed["llm_status"] = {
        **(llm_status or {}),
        "analysis_source": "openai",
        "fallback_reason": None,
        "openai_candidate_analyses_count": openai_candidate_analyses_count,
        "fallback_filled_candidate_analyses_count": sum(
            1 for source in candidate_analysis_sources.values() if source != "openai"
        ),
    }
    parsed["pack_input"] = pack_input
    return parsed


def normalize_pack_item_analysis(value: dict[str, Any], fallback: dict[str, Any]) -> dict[str, Any]:
    analysis = dict(fallback)
    for field in PACK_ANALYSIS_FIELDS:
        if field in value:
            analysis[field] = value[field]
    for legacy_field in ("summary", "signal", "evidence", "entry_realism", "mvp", "monetization", "risks", "checks"):
        if legacy_field in value:
            analysis[legacy_field] = value[legacy_field]
    recommendation = str(analysis.get("recommendation", "WATCH")).upper()
    analysis["recommendation"] = recommendation if recommendation in {"TEST", "WATCH", "AVOID"} else "WATCH"
    confidence = str(analysis.get("confidence", "medium")).lower()
    analysis["confidence"] = confidence if confidence in {"low", "medium", "high"} else "medium"
    return analysis


def pack_item_has_non_russian_text(analysis: dict[str, Any]) -> bool:
    return any(contains_non_russian_human_text(analysis.get(field)) for field in PACK_HUMAN_READABLE_FIELDS)


def build_pack_prompt(pack_input: dict[str, Any]) -> str:
    compact = json.dumps(pack_input, ensure_ascii=False, indent=2)
    return (
        "Ты аналитик мобильных игр для небольшой команды разработчиков.\n"
        "Отвечай только на русском языке.\n"
        "Пиши весь человекочитаемый анализ на русском языке: why_interesting, why_might_be_false_positive, "
        "mvp_hypothesis, simplified_mvp_scope, competitor_takeaways, entry_angle, differentiation_idea, "
        "why_top_products_validate_or_weaken_signal, validation_steps, risk_notes и missing_data.\n"
        "Стиль: практичный, короткий, без маркетинговой воды. Не обещай успех ниши; всегда указывай риски "
        "и возможные false positive.\n"
        "Не используй английские заголовки и английские фразы вроде Why interesting, MVP, Risks или Recommendation explanation.\n"
        "Не переводи machine-readable поля и enum-значения: candidate_id, recommendation, confidence, reason_codes, "
        "risk_tags, status, alert_stage, source_scope, score fields, URLs, app IDs и bundle IDs.\n"
        "Поле recommendation оставь только TEST, WATCH или AVOID. Поле confidence оставь только low, medium или high.\n"
        "Данные получены из одного AppStoreSpy query. В query нет фильтра по стране, языку или active_countries. "
        "Не называй срез глобальным рынком и не делай country-specific выводов.\n"
        "Top competitors — это top apps из того же одного query-среза, а не полный рынок.\n"
        "Отделяй fresh demand от paid traffic spikes. Не рекомендуй прямую конкуренцию с giant developers.\n"
        "Если это первый запуск без совместимой истории, не называй кандидатов подтвержденными alerts; "
        "трактуй их как INITIAL_BASELINE_NO_HISTORY и ограничь confidence уровнем medium.\n"
        "Массив alerts содержит только кандидатов, которые Python уже выбрал для Telegram в этом run. "
        "Python deterministic scoring уже выбрал sendable alerts; ты не выбираешь, что отправлять, и не меняешь список. "
        "Recommendation TEST/WATCH/AVOID — это комментарий, а не команда отправки. TEST не должен подразумевать "
        "отдельное Telegram-сообщение.\n"
        "Верни анализ для каждого candidate_id из alerts и не добавляй анализы для кандидатов вне alerts.\n"
        "Return only a JSON object with key candidate_analyses. Верни JSON строго по контракту. Ключи — candidate_id. "
        "Каждое значение должно содержать recommendation TEST/WATCH/AVOID, confidence, why_interesting, "
        "why_might_be_false_positive, mvp_hypothesis, simplified_mvp_scope, competitor_takeaways, entry_angle, "
        "differentiation_idea, why_top_products_validate_or_weaken_signal, validation_steps, risk_notes, missing_data, "
        "manual_review_needed.\n\n"
        f"Candidate pack JSON:\n{compact}"
    )


def generate_alert_report(alert: dict[str, Any], config: dict[str, Any], *, use_llm: bool = True) -> str:
    analysis = generate_alert_analysis(alert, config, use_llm=use_llm)
    return render_alert_report(alert, analysis)


def generate_alert_analysis(alert: dict[str, Any], config: dict[str, Any], *, use_llm: bool = True) -> dict[str, Any]:
    if use_llm and config.get("llm", {}).get("enabled", True) and os.environ.get("OPENAI_API_KEY"):
        try:
            return generate_openai_analysis(alert, config)
        except Exception as exc:  # pragma: no cover - network fallback
            analysis = generate_fallback_analysis(alert)
            analysis["llm_fallback_note"] = str(exc)
            return analysis
    return generate_fallback_analysis(alert)


def generate_openai_analysis(alert: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    llm_cfg = config.get("llm", {})
    model = os.environ.get(llm_cfg.get("model_env", "OPENAI_MODEL")) or llm_cfg.get("default_model", "gpt-4.1-mini")
    prompt = build_prompt(alert)
    payload = {"model": model, "input": prompt}
    request = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(request, timeout=int(llm_cfg.get("timeout_seconds", 60))) as response:
        data = json.loads(response.read().decode("utf-8"))
    text = extract_response_text(data)
    return validate_analysis(parse_json_object(text), alert)


def extract_response_text(data: dict[str, Any]) -> str:
    if data.get("output_text"):
        return str(data["output_text"])
    chunks: list[str] = []
    for output in data.get("output", []):
        for content in output.get("content", []):
            if content.get("type") in ("output_text", "text"):
                chunks.append(str(content.get("text", "")))
    if chunks:
        return "\n".join(chunks)
    raise RuntimeError("OpenAI response did not contain output text.")


def build_prompt(alert: dict[str, Any]) -> str:
    compact = json.dumps(alert, ensure_ascii=False, indent=2)
    return (
        "Ты аналитик мобильных игр для небольшой команды разработчиков.\n"
        "Отвечай только на русском языке. Все человекочитаемые строки и массивы должны быть на русском.\n"
        "Не переводи machine-readable поля и enum-значения. Поле recommendation оставь только TEST, WATCH или AVOID.\n"
        "Кандидат ниже получен ровно из одного AppStoreSpy Google Play /play/apps/query request.\n"
        "В request намеренно нет country, language или active_countries filters. Не называй это глобальным рынком "
        "и не делай country-specific выводов.\n"
        "Не рекомендуй прямую конкуренцию с giant developers и не выводи opportunity только из installs.\n"
        "Отделяй noisy market от реалистичного small-team entry. Если сигнал слабый, концентрированный "
        "или похож на paid traffic spike, честно выбери WATCH или AVOID.\n\n"
        "Analyze the AppStoreSpy alert candidate and return only a JSON object, without markdown.\n"
        "JSON schema:\n"
        "{\n"
        '  "summary": "brief conclusion",\n'
        '  "signal": "why this is a signal",\n'
        '  "evidence": ["fact 1", "fact 2"],\n'
        '  "entry_realism": "why entry is realistic or unrealistic",\n'
        '  "mvp": "4-8 week MVP concept",\n'
        '  "monetization": "monetization angle",\n'
        '  "risks": ["risk 1", "risk 2"],\n'
        '  "checks": ["manual check 1", "manual check 2"],\n'
        '  "recommendation": "TEST|WATCH|AVOID"\n'
        "}\n"
        "Не придумывай метрики. Используй только JSON facts. Учитывай data_quality_score и false-positive risk.\n\n"
        f"Alert JSON:\n{compact}"
    )


def parse_json_object(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = stripped.strip("`")
        if stripped.lower().startswith("json"):
            stripped = stripped[4:].strip()
    start = stripped.find("{")
    end = stripped.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("LLM response did not contain a JSON object.")
    parsed = json.loads(stripped[start : end + 1])
    if not isinstance(parsed, dict):
        raise ValueError("LLM JSON output must be an object.")
    return parsed


def validate_analysis(value: dict[str, Any], alert: dict[str, Any]) -> dict[str, Any]:
    fallback = generate_fallback_analysis(alert)
    analysis: dict[str, Any] = {}
    for field in ANALYSIS_FIELDS:
        candidate = value.get(field, fallback[field])
        if field in ("evidence", "risks", "checks"):
            if isinstance(candidate, list):
                analysis[field] = [str(item) for item in candidate if str(item).strip()]
            else:
                analysis[field] = [str(candidate)] if str(candidate).strip() else fallback[field]
        else:
            analysis[field] = str(candidate).strip() or fallback[field]
    recommendation = analysis["recommendation"].upper()
    analysis["recommendation"] = recommendation if recommendation in {"TEST", "WATCH", "AVOID"} else fallback["recommendation"]
    if any(contains_non_russian_human_text(analysis.get(field)) for field in ANALYSIS_FIELDS if field != "recommendation"):
        analysis["llm_language_warning"] = "non_russian_text_detected"
    return analysis


def generate_fallback_analysis(alert: dict[str, Any]) -> dict[str, Any]:
    quality = float(alert.get("data_quality_score", 0.0))
    score = float(alert.get("opportunity_score", 0.0))
    filter_reasons = set(alert.get("alert_filter_reasons", []))
    reason_codes = set(alert.get("reason_codes", []))
    if alert.get("alert_tier") == "TEST" and quality >= 65 and score >= 70:
        recommendation = "TEST"
    elif "giant_dominated" in reason_codes or "top_app_concentration" in reason_codes:
        recommendation = "AVOID"
    elif filter_reasons and filter_reasons != {"passed"}:
        recommendation = "WATCH"
    else:
        recommendation = "WATCH"

    top_apps = [str(app.get("name", "")) for app in alert.get("top_apps", []) if app.get("name")]
    evidence = [
        (
            "Охват источника: один AppStoreSpy Google Play query без country/language filters, "
            f"окно релизов {alert.get('release_date_window', 'last_180d')}."
        ),
        (
            f"Daily installs: {alert.get('total_daily_installs')}; app count: {alert.get('app_count')}; "
            f"data quality: {alert.get('data_quality_score')}."
        ),
    ]
    if top_apps:
        evidence.append(f"Top apps, подтверждающие сигнал: {', '.join(top_apps[:3])}.")
    risks = list_risks(alert)
    return {
        "summary": (
            f"{alert.get('niche')} выглядит как {recommendation}-кандидат в одном AppStoreSpy query-срезе "
            f"со score {alert.get('opportunity_score')} и quality {alert.get('data_quality_score')}."
        ),
        "signal": (
            f"Сигнал объединяет demand, fresh app activity, monetization, data quality и micro-niche dimensions "
            f"{alert.get('core_mechanic')} + {alert.get('theme')} + {alert.get('meta')}."
        ),
        "evidence": evidence,
        "entry_realism": (
            f"Production complexity: {alert.get('production_complexity')}; это реалистичнее для небольшой команды, "
            "если top-app concentration и giant share остаются ниже configured limits."
        ),
        "mvp": (
            f"Собрать MVP на 4-8 недель вокруг {alert.get('core_mechanic')} gameplay, темы {alert.get('theme')} "
            f"и {alert.get('meta')} progression для {alert.get('audience')}."
        ),
        "monetization": "Проверить rewarded ads, interstitial pacing и легкие IAP bundles после validation retention.",
        "risks": risks,
        "checks": [
            "Проверить, является ли рост organic или paid user acquisition.",
            "Проверить top apps вручную в AppStoreSpy и сторах.",
            "Не трактовать single-query slice как country-specific или global market estimate.",
            "Подтвердить monetization per install до production.",
        ],
        "recommendation": recommendation,
    }


def list_risks(alert: dict[str, Any]) -> list[str]:
    risks: list[str] = []
    if float(alert.get("growth_by_one_app_share", 0.0)) >= 0.7 or float(alert.get("advertised_top_app_share", 0.0)) >= 0.7:
        risks.append("Рост или demand могут быть вызваны одним приложением или paid user acquisition.")
    if float(alert.get("top_app_share", 0.0)) >= 0.75:
        risks.append("Top app concentration высокая.")
    if float(alert.get("giant_developer_share", 0.0)) >= 0.7:
        risks.append("Giant developer share слишком высока для прямой конкуренции.")
    if float(alert.get("data_quality_score", 0.0)) < 65:
        risks.append("Data quality ниже alert threshold.")
    if alert.get("production_complexity") == "high":
        risks.append("Production complexity слишком высокая для small-team entry.")
    if not risks:
        risks.append("Нужна ручная проверка store creatives, UA pressure и retention assumptions.")
    return risks


def render_alert_report(alert: dict[str, Any], analysis: dict[str, Any]) -> str:
    top_apps = "\n".join(
        (
            f"- {app.get('name')} ({app.get('developer_name')}): {app.get('downloads_daily')} daily installs"
            f"{'; AppStoreSpy: ' + str(app.get('url_appstorespy')) if app.get('url_appstorespy') else ''}"
        )
        for app in alert.get("top_apps", [])
    )
    components = json.dumps(alert.get("score_components", {}), ensure_ascii=False, indent=2)
    sendable_components = json.dumps(alert.get("sendable_score_components", {}), ensure_ascii=False, indent=2)
    analysis_json = json.dumps(analysis, ensure_ascii=False, indent=2)
    return (
        f"# Alert: {alert.get('alert_id')}\n\n"
        f"Recommendation: {analysis.get('recommendation')}\n\n"
        f"Tier: {alert.get('alert_tier', 'WATCH')}\n\n"
        f"Alert stage: {alert.get('alert_stage', 'UNKNOWN')}\n\n"
        f"Sendable alert score: {alert.get('sendable_alert_score')}\n\n"
        "## Summary\n"
        f"{analysis.get('summary')}\n\n"
        "## Signal\n"
        f"{analysis.get('signal')}\n\n"
        "## Classification\n"
        f"Market: {alert.get('market_category')}; mechanic: {alert.get('core_mechanic')}; "
        f"theme: {alert.get('theme')}; meta: {alert.get('meta')}; audience: {alert.get('audience')}; "
        f"complexity: {alert.get('production_complexity')}.\n\n"
        "## Source Scope\n"
        "One AppStoreSpy Google Play query; no country, language, or active_countries filter; "
        f"release window: {alert.get('release_date_window', 'last_180d')}; "
        f"sort: {alert.get('collection_sort', '-release_date')}; "
        f"minimum app daily installs: {alert.get('min_app_daily_installs', 500)}.\n\n"
        "## Evidence\n"
        f"Total daily installs: {alert.get('total_daily_installs')}; monthly revenue: "
        f"{alert.get('total_monthly_revenue')}; app count: {alert.get('app_count')}; "
        f"successful new apps: {alert.get('successful_new_apps_count')}.\n\n"
        f"{format_bullets(analysis.get('evidence', []))}\n\n"
        "## Entry realism\n"
        f"{analysis.get('entry_realism')}\n\n"
        "## MVP\n"
        f"{analysis.get('mvp')}\n\n"
        "## Monetization\n"
        f"{analysis.get('monetization')}\n\n"
        "## Risks\n"
        f"{format_bullets(analysis.get('risks', []))}\n\n"
        "## What to check\n"
        f"{format_bullets(analysis.get('checks', []))}\n\n"
        "## Top apps\n"
        f"{top_apps or '- No top apps captured'}\n\n"
        "## Score components\n"
        f"```json\n{components}\n```\n\n"
        "## Sendable score components\n"
        f"```json\n{sendable_components}\n```\n\n"
        "## Sendable reasons\n"
        f"{format_bullets(alert.get('sendable_alert_reasons', []))}\n\n"
        "## Sendable failures\n"
        f"{format_bullets(alert.get('sendable_alert_failures', []))}\n\n"
        "## Structured analysis\n"
        f"```json\n{analysis_json}\n```\n\n"
        "## Filter notes\n"
        f"Reason codes: {', '.join(alert.get('reason_codes', [])) or 'none'}.\n"
        f"Filter notes: {', '.join(alert.get('alert_filter_reasons', [])) or 'none'}.\n"
    )


def format_bullets(items: Any) -> str:
    if not isinstance(items, list):
        items = [items]
    clean_items = [str(item).strip() for item in items if str(item).strip()]
    return "\n".join(f"- {item}" for item in clean_items) or "- No details."
