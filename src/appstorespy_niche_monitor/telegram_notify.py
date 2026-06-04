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
        f"Data quality: {alert.get('data_quality_score')}/100\n"
        f"MVP feasibility: {alert.get('mvp_feasibility_score')}/100\n"
        f"Apps in niche: {alert.get('app_count')}\n"
        f"Total daily installs: {alert.get('total_daily_installs')}\n"
        f"Top app share: {alert.get('top_app_share')}\n"
        f"Risk tags: {', '.join(alert.get('risk_tags', [])) or 'none'}\n\n"
        "Why interesting:\n"
        f"{evidence}\n\n"
        "MVP:\n"
        f"{mvp}\n\n"
        "Risks:\n"
        f"{risks}\n\n"
        f"Recommendation: {recommendation}\n"
        f"Alert ID: {alert.get('alert_instance_id') or alert.get('alert_id')}"
    )


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
        if alert.get("status") != "ALERT" or not alert.get("send_regular_alert", True):
            continue
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
        "",
        "Top baseline candidates:",
    ]
    for index, item in enumerate(items, start=1):
        lines.append(
            f"{index}. {item.get('normalized_niche')} - would_be_status={item.get('would_be_status')}, "
            f"score={item.get('opportunity_score')}, installs={item.get('total_daily_installs')}, "
            f"reason_codes={', '.join(item.get('reason_codes', []))}"
        )
        analysis = item.get("llm_analysis")
        if isinstance(analysis, dict) and analysis:
            source = item.get("llm_analysis_source", "fallback")
            lines.append(
                f"   Review: recommendation={analysis.get('recommendation', 'WATCH')}, "
                f"confidence={analysis.get('confidence', item.get('confidence_level', 'MEDIUM'))}, source={source}"
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
    if int(result.get("sent_count", 0)) > 0:
        status = "TEST alerts passed filters and were sent separately."
    else:
        status = "No TEST alerts passed filters in this run. No regular ALERT messages were sent."
    return (
        "AppStoreSpy check completed\n\n"
        f"Mode: {result.get('mode')}\n"
        f"Snapshot date: {result.get('snapshot_date')}\n"
        "Scope: one AppStoreSpy query, no country/language filter\n"
        f"Apps checked: {result.get('apps_count')}\n"
        f"Niche summaries: {result.get('summaries_count')}\n"
        f"TEST alerts: {result.get('alerts_count')}\n"
        f"ALERT candidates: {result.get('alerts_count')}\n"
        f"WATCH candidates: {result.get('watch_count')}\n"
        f"NEAR_MISS candidates: {result.get('near_miss_count')}\n"
        f"Rejected candidates: {result.get('rejected_count')}\n"
        f"Baseline only: {baseline}\n\n"
        f"{status}"
    )


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
