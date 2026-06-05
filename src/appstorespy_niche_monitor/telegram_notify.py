from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
from typing import Any


def format_alert_message(alert: dict[str, Any]) -> str:
    analysis = alert.get("llm_analysis", {})
    evidence = format_list(analysis.get("why_interesting") or analysis.get("evidence") or alert.get("reason_codes", []), limit=3)
    risks = format_list(analysis.get("risk_notes") or analysis.get("risks") or alert.get("risk_tags", []), limit=2)
    recommendation = analysis.get("recommendation", alert.get("status", "WATCH"))
    mvp = analysis.get("mvp_hypothesis") or analysis.get("mvp") or "Validate the niche manually before starting production."
    competitors = format_competitors(alert.get("top_competitors") or alert.get("top_products") or alert.get("top_apps", []), limit=3)
    ai_status = format_alert_ai_status(alert, analysis)
    coverage = alert.get("coverage", {})
    coverage_status = "unknown"
    if isinstance(coverage, dict):
        coverage_status = str(coverage.get("sample_truncated", "unknown"))
    return (
        f"Fresh Game Niche Alert: {alert.get('normalized_niche', alert.get('niche'))}\n\n"
        "Platform: Google Play\n"
        "Scope: one AppStoreSpy query, no country/language filter\n"
        "Source: single AppStoreSpy query\n"
        f"Window: {alert.get('release_date_window', 'last_180d')}; sort: {alert.get('collection_sort', '-release_date')}\n"
        f"Min daily installs per app in source query: {alert.get('min_app_daily_installs', 500)}\n"
        f"Coverage: {coverage_status}\n"
        f"Score: {alert.get('opportunity_score')}/100\n"
        f"Sendable alert score: {alert.get('sendable_alert_score')}/100\n"
        f"Trend confidence: {alert.get('trend_confidence_score')}/100\n"
        f"Team fit: {alert.get('team_fit_score')}/100\n"
        f"Organic confidence: {alert.get('organic_confidence', 'unknown')}\n"
        f"Alert stage: {alert.get('alert_stage', 'unknown')}\n"
        f"Data quality: {alert.get('data_quality_score')}/100\n"
        f"MVP feasibility: {alert.get('mvp_feasibility_score')}/100\n"
        f"Apps in niche: {alert.get('app_count')}\n"
        f"Total daily installs: {alert.get('total_daily_installs')}\n"
        f"Top app share: {alert.get('top_app_share')}\n"
        f"Risk tags: {', '.join(alert.get('risk_tags', [])) or 'none'}\n\n"
        f"{ai_status}\n\n"
        "Why interesting:\n"
        f"{evidence}\n\n"
        "Why sent now:\n"
        f"{format_list(alert.get('sendable_alert_reasons', []), limit=4)}\n\n"
        "MVP:\n"
        f"{mvp}\n\n"
        "Top competitors:\n"
        f"{competitors}\n\n"
        "Risks:\n"
        f"{risks}\n\n"
        "Why this can be false positive:\n"
        f"{format_list(alert.get('sendable_alert_failures') or alert.get('risk_tags', []), limit=4)}\n\n"
        f"Recommendation: {recommendation}\n"
        f"Alert ID: {alert.get('alert_instance_id') or alert.get('alert_id')}"
    )


def format_alert_ai_status(alert: dict[str, Any], analysis: dict[str, Any]) -> str:
    source = str(alert.get("llm_analysis_source") or "")
    llm_status = alert.get("llm_status")
    if not source and isinstance(llm_status, dict):
        source = str(llm_status.get("analysis_source") or "")
    source = source or "fallback"
    parts = [f"source={source}"]
    if analysis.get("confidence"):
        parts.append(f"confidence={analysis.get('confidence')}")
    fallback_reason = alert.get("llm_fallback_reason")
    if source != "openai" and fallback_reason:
        parts.append(f"fallback_reason={fallback_reason}")
    return f"AI review: {', '.join(parts)}"


def format_competitors(apps: Any, limit: int = 3) -> str:
    if not isinstance(apps, list):
        return "- No top competitors captured."
    lines: list[str] = []
    for index, app in enumerate([item for item in apps if isinstance(item, dict)][:limit], start=1):
        name = app.get("name") or app.get("bundle") or app.get("app_id") or "Unknown app"
        developer = app.get("developer_name") or "unknown developer"
        daily = app.get("downloads_daily", "unknown")
        revenue = app.get("revenue_month")
        rating = app.get("rating_avg")
        details = [f"{index}. {name} - {developer}; daily installs: {daily}"]
        if revenue not in (None, ""):
            details.append(f"monthly revenue: {revenue}")
        if rating not in (None, ""):
            details.append(f"rating: {rating}")
        lines.append("; ".join(str(part) for part in details))
        appstorespy_url = app.get("url_appstorespy") or app.get("appstorespy_url")
        if appstorespy_url:
            lines.append(f"   AppStoreSpy: {appstorespy_url}")
        elif app.get("url"):
            lines.append(f"   Store: {app.get('url')}")
    return "\n".join(lines) if lines else "- No top competitors captured."


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
        "Initial Baseline Discovery Report",
        "",
        "Source: single AppStoreSpy query",
        "Window: releases from last 180 days",
        "History: no previous compatible snapshot",
        "Important: this is not a regular ALERT; confidence is capped at MEDIUM.",
    ]
    lines.extend(format_initial_llm_status(items))
    lines.extend(["", "Top baseline candidates:"])
    for index, item in enumerate(items, start=1):
        lines.append(
            f"{index}. {item.get('normalized_niche')} - would_be_status={item.get('would_be_status')}, "
            f"score={item.get('opportunity_score')}, installs={item.get('total_daily_installs')}, "
            f"reason_codes={', '.join(item.get('reason_codes', []))}"
        )
        analysis = item.get("llm_analysis")
        if isinstance(analysis, dict) and analysis:
            source = item.get("llm_analysis_source", "fallback")
            fallback_reason = item.get("llm_fallback_reason")
            review_parts = [
                f"recommendation={analysis.get('recommendation', 'WATCH')}",
                f"confidence={analysis.get('confidence', item.get('confidence_level', 'MEDIUM'))}",
                f"source={source}",
            ]
            if source != "openai" and fallback_reason:
                review_parts.append(f"fallback_reason={fallback_reason}")
            lines.append(
                f"   Review: {', '.join(review_parts)}"
            )
            if analysis.get("mvp_hypothesis"):
                lines.append(f"   MVP: {analysis.get('mvp_hypothesis')}")
            risks = analysis.get("why_might_be_false_positive") or analysis.get("risk_notes") or []
            if risks:
                risk_text = "; ".join(str(risk) for risk in risks[:3])
                lines.append(f"   Risks: {risk_text}")
    lines.extend(
        [
            "",
            "Limitations:",
            "- No historical growth confirmation.",
            "- Paid-spike risk is based only on the current slice.",
            "- These items were not written to sent_alerts and do not start cooldown.",
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
    lines = ["", f"LLM: {', '.join(parts)}"]
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
    llm_line = format_result_llm_status(result)
    status = (
        f"LLM TEST recommendations among sendable alerts: {result.get('llm_test_recommendations', 0)}\n"
        f"Separate TEST messages sent: {result.get('separate_test_messages_sent', 0)}\n"
        f"Regular Telegram alerts sent: {result.get('telegram_regular_alerts_sent', result.get('sent_count', 0))}"
    )
    return (
        "AppStoreSpy check completed\n\n"
        f"Mode: {result.get('mode')}\n"
        f"Snapshot date: {result.get('snapshot_date')}\n"
        "Scope: one AppStoreSpy query, no country/language filter\n"
        f"Apps checked: {result.get('apps_count')}\n"
        f"Niche summaries: {result.get('summaries_count')}\n"
        f"ALERT candidates: {result.get('alerts_count')}\n"
        f"STRONG_ALERT candidates: {result.get('strong_alert_candidates_count', 0)}\n"
        f"SENDABLE alerts: {result.get('sendable_alerts_count', result.get('sent_count', 0))}\n"
        f"WATCH candidates: {result.get('watch_count')}\n"
        f"SINGLE_APP_WATCH candidates: {result.get('single_app_watch_count', 0)}\n"
        f"NEAR_MISS candidates: {result.get('near_miss_count')}\n"
        f"Rejected candidates: {result.get('rejected_count')}\n"
        f"Candidates before market-signal dedupe: {result.get('candidates_before_market_signal_dedupe', 0)}\n"
        f"Candidates after market-signal dedupe: {result.get('candidates_after_market_signal_dedupe', 0)}\n"
        f"Status counts before dedupe: {format_compact_counts(result.get('status_counts_before_dedupe', {}))}\n"
        f"Status counts after dedupe: {format_compact_counts(result.get('status_counts_after_dedupe', {}))}\n"
        f"Duplicate market signals suppressed: {result.get('duplicate_market_signals_suppressed', 0)}\n"
        f"Cooldown blocked: {result.get('cooldown_blocked_count', 0)}\n"
        f"Limit blocked: {result.get('limit_blocked_count', 0)}\n"
        "Sendable hard-filter pass/fail: "
        f"{result.get('sendable_hard_filter_pass_count', 0)}/"
        f"{result.get('sendable_hard_filter_fail_count', 0)}\n"
        f"Calibrated promotions: {result.get('calibrated_promotions_count', 0)}\n"
        f"Mixed unknown clusters: {result.get('mixed_unknown_clusters_count', 0)}\n"
        f"Unknown-dominant clusters: {result.get('unknown_dominant_clusters_count', 0)}\n"
        f"Unknown blocker active: {result.get('unknown_blocker_active_count', 0)}\n"
        "Candidates blocked by unknown_pattern_blocker_active: "
        f"{result.get('unknown_pattern_blocker_active_blocked_count', 0)}\n"
        f"Sendable blockers: {format_top_counts(result.get('top_first_blocking_failures', {}), limit=10)}\n"
        f"Baseline only: {baseline}\n"
        f"{llm_line}\n\n"
        f"{status}"
    )


def format_result_llm_status(result: dict[str, Any]) -> str:
    llm_status = result.get("llm_status")
    if not isinstance(llm_status, dict) or not llm_status:
        return "LLM review: unavailable"
    parts = [
        f"source={llm_status.get('analysis_source', 'fallback')}",
        f"model={llm_status.get('model', 'unknown')}",
    ]
    if llm_status.get("fallback_reason"):
        parts.append(f"fallback_reason={llm_status.get('fallback_reason')}")
    return f"LLM review: {', '.join(parts)}"


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
        return "- No details."
    return "\n".join(f"- {item}" for item in clean_items[:limit])
