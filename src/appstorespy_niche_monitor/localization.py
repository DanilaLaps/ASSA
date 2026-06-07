from __future__ import annotations

import re
from typing import Any


RU_CONFIDENCE = {
    "low": "низкая",
    "medium": "средняя",
    "high": "высокая",
}

RU_RECOMMENDATION_EXPLANATIONS = {
    "TEST": "TEST — можно рассмотреть быстрый тест после ручной проверки.",
    "WATCH": "WATCH — наблюдать, нужна ручная проверка перед тестом.",
    "AVOID": "AVOID — сигнал выглядит слабым или рискованным.",
}

RU_COVERAGE = {
    "unknown": "неизвестно",
    "partial": "частичное",
    "good": "хорошее",
    "full": "полное",
    "true": "частичное, срез может быть усечен",
    "false": "хорошее, срез не усечен",
}

RU_LLM_SOURCE = {
    "openai": "OpenAI",
    "fallback": "fallback-анализ",
    "fallback_missing_from_openai": "fallback: OpenAI не вернул этот candidate_id",
}

RU_FALLBACK_REASON = {
    "no_sendable_alerts": "нет финальных SENDABLE_ALERT-кандидатов",
    "missing_api_key": "не задан OPENAI_API_KEY",
    "missing_openai_api_key": "не задан OPENAI_API_KEY",
    "disabled_by_cli": "LLM отключен параметром запуска",
    "disabled_in_config": "LLM отключен в config",
    "llm_disabled": "LLM отключен в config",
    "openai_error": "ошибка OpenAI",
    "fallback_missing_from_openai": "OpenAI не вернул анализ для этого candidate_id",
    "missing_from_openai_response": "OpenAI не вернул анализ для этого candidate_id",
}

RU_RISK_TAG_DESCRIPTIONS = {
    "unknown_coverage": "покрытие данных неизвестно или неполное",
    "weak_rating_signal": "слабая надежность rating-сигнала",
    "weak_revenue_signal": "слабый revenue-сигнал",
    "weak_monetization_signal": "слабый monetization-сигнал",
    "leader_dominated": "ниша сильно зависит от лидера",
    "top_app_dominance": "слишком высокая доля top-приложения",
    "growth_by_one_app": "рост может идти за счет одного приложения",
    "possible_paid_spike": "возможен paid UA spike",
    "severe_paid_spike": "сильный риск paid UA spike",
    "unknown_dominant_cluster": "unknown-приложения доминируют в кластере",
    "mixed_unknown_cluster": "в кластере есть unknown-приложения",
    "giant_developer_risk": "высокая доля крупного разработчика",
    "low_data_quality": "низкое качество данных",
}

RU_REASON_CODE_DESCRIPTIONS = {
    "high_demand": "есть заметный спрос в одном AppStoreSpy query-срезе",
    "historical_growth": "история показывает рост сигнала",
    "strong_daily_installs": "высокие daily installs в кластере",
    "classification_confident": "классификация достаточно уверенная",
    "closest_to_sendable_thresholds": "кандидат близок к sendable-порогам",
    "fresh_success_validation": "есть свежие успешные приложения",
    "healthy_data_quality": "качество данных достаточно хорошее",
    "INITIAL_BASELINE_NO_HISTORY": "первый запуск без совместимой истории",
    "promoted_best_clean_alert_when_no_sendable": "лучший чистый кандидат повышен при отсутствии sendable alerts",
}


def ru_confidence(value: Any) -> str:
    key = str(value or "").lower()
    return RU_CONFIDENCE.get(key, str(value or "неизвестно"))


def ru_recommendation(value: Any) -> str:
    key = str(value or "WATCH").upper()
    return RU_RECOMMENDATION_EXPLANATIONS.get(key, RU_RECOMMENDATION_EXPLANATIONS["WATCH"])


def ru_coverage(value: Any) -> str:
    key = str(value if value is not None else "unknown").lower()
    return RU_COVERAGE.get(key, str(value or "неизвестно"))


def ru_llm_source(value: Any) -> str:
    key = str(value or "fallback")
    return RU_LLM_SOURCE.get(key, key)


def ru_fallback_reason(value: Any) -> str:
    key = str(value or "")
    return RU_FALLBACK_REASON.get(key, key)


def describe_risk_tag(code: Any) -> str:
    key = str(code)
    description = RU_RISK_TAG_DESCRIPTIONS.get(key)
    return f"{key} — {description}" if description else key


def describe_reason_code(code: Any) -> str:
    key = str(code)
    description = RU_REASON_CODE_DESCRIPTIONS.get(key)
    return f"{key} — {description}" if description else key


def human_join(values: Any) -> str:
    if not isinstance(values, list):
        values = [values]
    clean = [str(value).strip() for value in values if str(value).strip()]
    return ", ".join(clean) if clean else "none"


def release_window_ru(value: Any) -> str:
    text = str(value or "last_180d")
    match = re.fullmatch(r"last_(\d+)d", text)
    if match:
        return f"последние {match.group(1)} дней"
    return text


def contains_non_russian_human_text(value: Any) -> bool:
    if isinstance(value, list):
        return any(contains_non_russian_human_text(item) for item in value)
    if not isinstance(value, str):
        return False
    text = value.strip()
    if not text:
        return False
    cyrillic = len(re.findall(r"[А-Яа-яЁё]", text))
    latin = len(re.findall(r"[A-Za-z]", text))
    return latin >= 20 and cyrillic == 0
