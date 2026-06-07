from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
from typing import Any

from .localization import (
    describe_reason_code,
    describe_risk_tag,
    human_join,
    release_window_ru,
    ru_confidence,
    ru_coverage,
    ru_fallback_reason,
    ru_llm_source,
    ru_recommendation,
)


def format_alert_message(alert: dict[str, Any]) -> str:
    analysis = alert.get("llm_analysis", {})
    if not isinstance(analysis, dict):
        analysis = {}
    evidence_items = analysis.get("why_interesting") or analysis.get("evidence")
    if not evidence_items:
        evidence_items = [describe_reason_code(code) for code in alert.get("reason_codes", [])]
    risk_items = analysis.get("risk_notes") or analysis.get("risks")
    if not risk_items:
        risk_items = [describe_risk_tag(tag) for tag in alert.get("risk_tags", [])]
    recommendation = str(analysis.get("recommendation", alert.get("status", "WATCH"))).upper()
    mvp = (
        analysis.get("mvp_hypothesis")
        or analysis.get("mvp")
        or "Проверить нишу вручную перед стартом production."
    )
    competitors = format_competitors(alert.get("top_competitors") or alert.get("top_products") or alert.get("top_apps", []), limit=3)
    coverage_status = extract_coverage_status(alert.get("coverage", {}))
    return (
        f"{format_alert_title(alert, recommendation)}\n\n"
        "Платформа: Google Play\n"
        "Охват данных: один запрос AppStoreSpy, без фильтра страны и языка\n"
        "Источник: один AppStoreSpy query\n"
        f"Окно релизов: {release_window_ru(alert.get('release_date_window', 'last_180d'))}; "
        f"сортировка: {alert.get('collection_sort', '-release_date')}\n"
        "Минимум установок в исходном запросе: "
        f"{alert.get('min_app_daily_installs', 500)} в день на приложение\n"
        f"Покрытие данных: {ru_coverage(coverage_status)}\n\n"
        "Классификация:\n"
        f"- market_category: {alert.get('market_category', 'unknown')}\n"
        f"- core_mechanic: {alert.get('core_mechanic', 'unknown')}\n"
        f"- theme: {alert.get('theme', 'unknown')}\n"
        f"- meta: {alert.get('meta', 'unknown')}\n"
        f"- audience: {alert.get('audience', 'unknown')}\n"
        f"- production_complexity: {alert.get('production_complexity', 'unknown')}\n\n"
        "Оценки:\n"
        f"- Opportunity score: {alert.get('opportunity_score')}/100\n"
        f"- Sendable alert score: {alert.get('sendable_alert_score')}/100\n"
        f"- Уверенность тренда: {alert.get('trend_confidence_score')}/100\n"
        f"- Подходит небольшой команде: {alert.get('team_fit_score')}/100\n"
        f"- Органическая уверенность: {alert.get('organic_confidence', 'unknown')}\n"
        f"- Стадия alert-а: {alert.get('alert_stage', 'unknown')}\n"
        f"- Качество данных: {alert.get('data_quality_score')}/100\n"
        f"- Реализуемость MVP: {alert.get('mvp_feasibility_score')}/100\n\n"
        "Размер ниши:\n"
        f"- Приложений в кластере: {alert.get('app_count')}\n"
        f"- Суммарные daily installs: {alert.get('total_daily_installs')}\n"
        f"- Доля top-приложения: {alert.get('top_app_share')}\n\n"
        "Risk tags:\n"
        f"{format_code_list(alert.get('risk_tags', []), describe_risk_tag)}\n\n"
        f"{format_alert_ai_status(alert, analysis)}\n\n"
        "Почему интересно:\n"
        f"{format_list(evidence_items, limit=3)}\n\n"
        "Почему отправлено сейчас:\n"
        f"{format_code_list(alert.get('sendable_alert_reasons', []), describe_reason_code, limit=4)}\n\n"
        "Гипотеза MVP:\n"
        f"{mvp}\n\n"
        "Основные конкуренты:\n"
        f"{competitors}\n\n"
        "Риски:\n"
        f"{format_list(risk_items, limit=3)}\n\n"
        "Почему сигнал может быть ложноположительным:\n"
        f"{format_code_list(alert.get('sendable_alert_failures') or alert.get('risk_tags', []), describe_risk_tag, limit=4)}\n\n"
        f"Alert ID: {alert.get('alert_instance_id') or alert.get('alert_id')}"
    )


def format_alert_title(alert: dict[str, Any], recommendation: str) -> str:
    niche = alert.get("normalized_niche", alert.get("niche"))
    selection_mode = str(alert.get("selection_mode") or "")
    if selection_mode == "calibrated_promotion" or alert.get("calibrated_promotion") is True:
        return f"Кандидат для ручной проверки: {niche}"
    if selection_mode == "normal_sendable" and recommendation == "TEST":
        return f"Свежий сигнал по игровой нише: {niche}"
    if recommendation == "WATCH":
        return f"Кандидат для наблюдения: {niche}"
    return f"Сигнал по игровой нише: {niche}"


def extract_coverage_status(coverage: Any) -> Any:
    if not isinstance(coverage, dict):
        return "unknown"
    if "status" in coverage:
        return coverage.get("status")
    if "sample_truncated" in coverage:
        return coverage.get("sample_truncated")
    return "unknown"


def format_alert_ai_status(alert: dict[str, Any], analysis: dict[str, Any]) -> str:
    source = str(alert.get("llm_analysis_source") or "")
    llm_status = alert.get("llm_status")
    if not source and isinstance(llm_status, dict):
        source = str(llm_status.get("analysis_source") or "")
    source = source or "fallback"
    lines = [
        "ИИ-анализ:",
        f"- Источник: {ru_llm_source(source)}",
    ]
    if analysis.get("confidence"):
        lines.append(f"- Уверенность: {ru_confidence(analysis.get('confidence'))}")
    fallback_reason = alert.get("llm_fallback_reason")
    if source != "openai" and fallback_reason:
        lines.append(f"- fallback_reason: {fallback_reason} ({ru_fallback_reason(fallback_reason)})")
    recommendation = analysis.get("recommendation")
    if recommendation:
        lines.append(f"- Рекомендация ИИ: {ru_recommendation(recommendation)}")
    warning = analysis.get("llm_language_warning") or alert.get("llm_language_warning")
    if warning == "non_russian_text_detected":
        lines.append("- Предупреждение: OpenAI вернул часть анализа не на русском языке.")
    return "\n".join(lines)


def format_competitors(apps: Any, limit: int = 3) -> str:
    if not isinstance(apps, list):
        return "- Основные конкуренты не найдены в срезе."
    lines: list[str] = []
    for index, app in enumerate([item for item in apps if isinstance(item, dict)][:limit], start=1):
        name = app.get("name") or app.get("bundle") or app.get("app_id") or "Unknown app"
        developer = app.get("developer_name") or "unknown developer"
        daily = app.get("downloads_daily", "unknown")
        revenue = app.get("revenue_month")
        rating = app.get("rating_avg")
        lines.append(f"{index}. {name} — {developer}")
        lines.append(f"   Daily installs: {daily}")
        if revenue not in (None, ""):
            lines.append(f"   Monthly revenue: {revenue}")
        if rating not in (None, ""):
            lines.append(f"   Rating: {rating}")
        appstorespy_url = app.get("url_appstorespy") or app.get("appstorespy_url")
        if appstorespy_url:
            lines.append(f"   AppStoreSpy: {appstorespy_url}")
        elif app.get("url"):
            lines.append(f"   Store: {app.get('url')}")
        lines.append("")
    return "\n".join(lines).rstrip() if lines else "- Основные конкуренты не найдены в срезе."


def send_alerts(alerts: list[dict[str, Any]], config: dict[str, Any]) -> list[dict[str, Any]]:
    telegram_cfg = config.get("telegram", {})
    if not telegram_cfg.get("enabled", True):
        return []
    token = os.environ.get(telegram_cfg.get("bot_token_env", "TELEGRAM_BOT_TOKEN"))
    chat_id = os.environ.get(telegram_cfg.get("chat_id_env", "TELEGRAM_CHAT_ID"))
    if not token or not chat_id:
        raise RuntimeError("TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID are required to send notifications.")
    sent: list[dict[str, Any]] = []
    for alert in alerts:
        if alert.get("send_regular_alert") is not True:
            continue
        assert alert.get("status") == "ALERT"
        assert alert.get("alert_stage") == "SENDABLE_ALERT"
        send_message(token, chat_id, format_alert_message(alert), int(telegram_cfg.get("max_message_chars", 3900)))
        sent.append(alert)
    return sent


def format_initial_baseline_digest_message(items: list[dict[str, Any]]) -> str:
    lines = [
        "Первичный baseline-отчет",
        "",
        "Это первый запуск без совместимой истории.",
        "Обычные ALERT-сообщения не отправляются.",
        "",
        "Источник: один AppStoreSpy query",
        "Охват данных: один запрос AppStoreSpy, без фильтра страны и языка",
        "Окно релизов: последние 180 дней",
        "Найденные кандидаты не считаются отправленными alert-ами.",
        "Для них используется reason_code = INITIAL_BASELINE_NO_HISTORY.",
        "Уверенность ограничена уровнем MEDIUM.",
    ]
    lines.extend(format_initial_llm_status(items))
    lines.extend(["", "Кандидаты для первичного просмотра:"])
    for index, item in enumerate(items, start=1):
        lines.append(
            f"{index}. {item.get('normalized_niche')} — would_be_status={item.get('would_be_status')}, "
            f"score={item.get('opportunity_score')}, installs={item.get('total_daily_installs')}, "
            f"reason_codes={human_join(item.get('reason_codes', []))}"
        )
        analysis = item.get("llm_analysis")
        if isinstance(analysis, dict) and analysis:
            source = item.get("llm_analysis_source", "fallback")
            fallback_reason = item.get("llm_fallback_reason")
            lines.append(f"   Рекомендация ИИ: {ru_recommendation(analysis.get('recommendation', 'WATCH'))}")
            lines.append(f"   Уверенность: {ru_confidence(analysis.get('confidence', item.get('confidence_level', 'MEDIUM')))}")
            lines.append(f"   Источник: {ru_llm_source(source)}")
            if source != "openai" and fallback_reason:
                lines.append(f"   fallback_reason: {fallback_reason} ({ru_fallback_reason(fallback_reason)})")
            if analysis.get("mvp_hypothesis"):
                lines.append(f"   Гипотеза MVP: {analysis.get('mvp_hypothesis')}")
            risks = analysis.get("why_might_be_false_positive") or analysis.get("risk_notes") or []
            if risks:
                risk_text = "; ".join(str(risk) for risk in risks[:3])
                lines.append(f"   Риски: {risk_text}")
    lines.extend(
        [
            "",
            "Ограничения:",
            "- Нет исторического подтверждения роста.",
            "- Риск paid-spike оценивается только по текущему срезу.",
            "- Эти кандидаты не записаны в sent_alerts.json и не запускают cooldown.",
        ]
    )
    return "\n".join(lines)


def format_initial_llm_status(items: list[dict[str, Any]]) -> list[str]:
    status: dict[str, Any] = {}
    for item in items:
        candidate_status = item.get("llm_status")
        if isinstance(candidate_status, dict) and candidate_status:
            status = candidate_status
            break
    if not status:
        return []
    parts = [
        f"source={status.get('analysis_source', 'fallback')}",
        f"model={status.get('model', 'unknown')}",
        f"api_key_present={str(bool(status.get('api_key_present'))).lower()}",
    ]
    if status.get("fallback_reason"):
        parts.append(f"fallback_reason={status.get('fallback_reason')}")
    lines = ["", f"Статус LLM: {', '.join(parts)}"]
    if status.get("fallback_reason"):
        lines.append(f"Пояснение fallback: {ru_fallback_reason(status.get('fallback_reason'))}")
    if status.get("fallback_detail"):
        lines.append(f"LLM fallback_detail: {status.get('fallback_detail')}")
    return lines


def send_initial_baseline_digest(items: list[dict[str, Any]], config: dict[str, Any]) -> bool:
    if not items:
        return False
    first_cfg = config.get("first_run_behavior", {})
    if not first_cfg.get("send_initial_baseline_digest", True):
        return False
    telegram_cfg = config.get("telegram", {})
    if not telegram_cfg.get("enabled", True):
        return False
    token = os.environ.get(telegram_cfg.get("bot_token_env", "TELEGRAM_BOT_TOKEN"))
    chat_id = os.environ.get(telegram_cfg.get("chat_id_env", "TELEGRAM_CHAT_ID"))
    if not token or not chat_id:
        return False
    send_message(
        token,
        chat_id,
        format_initial_baseline_digest_message(items),
        int(telegram_cfg.get("max_message_chars", 3900)),
    )
    return True


def format_run_summary_message(result: dict[str, Any]) -> str:
    baseline = "yes" if result.get("baseline_only") else "no"
    return (
        "Проверка AppStoreSpy завершена\n\n"
        f"Режим: {result.get('mode')}\n"
        f"Дата snapshot: {result.get('snapshot_date')}\n"
        "Охват: один запрос AppStoreSpy, без фильтра страны и языка\n"
        f"Проверено приложений: {result.get('apps_count')}\n"
        f"Сводок по нишам: {result.get('summaries_count')}\n\n"
        "Воронка:\n"
        f"- ALERT-кандидаты: {result.get('alerts_count')}\n"
        f"- STRONG_ALERT-кандидаты: {result.get('strong_alert_candidates_count', 0)}\n"
        f"- Финальные SENDABLE alerts: {result.get('sendable_alerts_count', result.get('sent_count', 0))}\n"
        f"- WATCH-кандидаты: {result.get('watch_count')}\n"
        f"- SINGLE_APP_WATCH-кандидаты: {result.get('single_app_watch_count', 0)}\n"
        f"- NEAR_MISS-кандидаты: {result.get('near_miss_count')}\n"
        f"- Отклонено: {result.get('rejected_count')}\n\n"
        "Дедупликация и лимиты:\n"
        f"- Кандидатов до market-signal dedupe: {result.get('candidates_before_market_signal_dedupe', 0)}\n"
        f"- Кандидатов после market-signal dedupe: {result.get('candidates_after_market_signal_dedupe', 0)}\n"
        f"- Status counts до dedupe: {format_compact_counts(result.get('status_counts_before_dedupe', {}))}\n"
        f"- Status counts после dedupe: {format_compact_counts(result.get('status_counts_after_dedupe', {}))}\n"
        f"- Подавлено дублей market-signal: {result.get('duplicate_market_signals_suppressed', 0)}\n"
        f"- Заблокировано cooldown: {result.get('cooldown_blocked_count', 0)}\n"
        f"- Заблокировано лимитом: {result.get('limit_blocked_count', 0)}\n\n"
        "SENDABLE-фильтр:\n"
        "- Прошли strict hard-filter: "
        f"{result.get('sendable_hard_filter_pass_count', 0)}/"
        f"{result.get('sendable_hard_filter_fail_count', 0)}\n"
        f"- Calibrated promotions: {result.get('calibrated_promotions_count', 0)}\n"
        f"- Основные блокеры: {format_top_counts(result.get('top_first_blocking_failures', {}), limit=10)}\n\n"
        "Unknown diagnostics:\n"
        f"- Mixed unknown clusters: {result.get('mixed_unknown_clusters_count', 0)}\n"
        f"- Unknown-dominant clusters: {result.get('unknown_dominant_clusters_count', 0)}\n"
        f"- Unknown blocker active: {result.get('unknown_blocker_active_count', 0)}\n"
        "- Заблокировано unknown_pattern_blocker_active: "
        f"{result.get('unknown_pattern_blocker_active_blocked_count', 0)}\n\n"
        "LLM:\n"
        f"{format_result_llm_status(result)}\n"
        f"- TEST-рекомендаций среди отправленных alerts: {result.get('llm_test_recommendations', 0)}\n"
        f"- Отдельных TEST-сообщений отправлено: {result.get('separate_test_messages_sent', 0)}\n\n"
        "Telegram:\n"
        f"- Обычных alert-сообщений отправлено: {result.get('telegram_regular_alerts_sent', result.get('sent_count', 0))}\n"
        f"- Baseline only: {baseline}"
    )


def format_result_llm_status(result: dict[str, Any]) -> str:
    llm_status = result.get("llm_status")
    if not isinstance(llm_status, dict) or not llm_status:
        return "- Источник: недоступно"
    source = llm_status.get("analysis_source", "fallback")
    lines = [
        f"- Источник: {ru_llm_source(source)}",
        f"- Модель: {llm_status.get('model', 'unknown')}",
    ]
    if llm_status.get("fallback_reason"):
        fallback_reason = llm_status.get("fallback_reason")
        lines.append(f"- fallback_reason: {fallback_reason} ({ru_fallback_reason(fallback_reason)})")
    return "\n".join(lines)


def format_compact_counts(value: Any) -> str:
    if not isinstance(value, dict) or not value:
        return "none"
    return ", ".join(f"{key}={value[key]}" for key in sorted(value))


def format_top_counts(value: Any, *, limit: int) -> str:
    if not isinstance(value, dict) or not value:
        return "none"
    items = sorted(value.items(), key=lambda item: (-int(item[1]), str(item[0])))[:limit]
    return ", ".join(f"{key}={count}" for key, count in items)


def send_run_summary(result: dict[str, Any], config: dict[str, Any]) -> bool:
    telegram_cfg = config.get("telegram", {})
    if not telegram_cfg.get("enabled", True):
        return False
    if not telegram_cfg.get("notify_on_completion", True):
        return False
    token = os.environ.get(telegram_cfg.get("bot_token_env", "TELEGRAM_BOT_TOKEN"))
    chat_id = os.environ.get(telegram_cfg.get("chat_id_env", "TELEGRAM_CHAT_ID"))
    if not token or not chat_id:
        raise RuntimeError("TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID are required to send notifications.")
    send_message(token, chat_id, format_run_summary_message(result), int(telegram_cfg.get("max_message_chars", 3900)))
    return True


def send_message(token: str, chat_id: str, text: str, max_chars: int = 3900) -> None:
    for chunk in chunk_text(text, max_chars):
        payload = urllib.parse.urlencode({"chat_id": chat_id, "text": chunk}).encode("utf-8")
        request = urllib.request.Request(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data=payload,
            method="POST",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8"))
            if not data.get("ok"):
                raise RuntimeError(f"Telegram sendMessage failed: {data}")


def chunk_text(text: str, max_chars: int) -> list[str]:
    if len(text) <= max_chars:
        return [text]
    chunks: list[str] = []
    remaining = text
    while remaining:
        chunks.append(remaining[:max_chars])
        remaining = remaining[max_chars:]
    return chunks


def format_list(items: Any, limit: int) -> str:
    if not isinstance(items, list):
        items = [items]
    clean_items = [str(item).strip() for item in items if str(item).strip()]
    if not clean_items:
        return "- Нет деталей."
    return "\n".join(f"- {item}" for item in clean_items[:limit])


def format_code_list(items: Any, formatter: Any = str, limit: int | None = None) -> str:
    if not isinstance(items, list):
        items = [items]
    clean_items = [formatter(item) for item in items if str(item).strip()]
    if limit is not None:
        clean_items = clean_items[:limit]
    if not clean_items:
        return "- none"
    return "\n".join(f"- {item}" for item in clean_items)
