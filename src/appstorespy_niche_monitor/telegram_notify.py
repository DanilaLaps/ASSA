from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
from typing import Any


def format_alert_message(alert: dict[str, Any]) -> str:
    analysis = alert.get("llm_analysis", {})
    evidence = format_list(analysis.get("evidence") or alert.get("reason_codes", []), limit=3)
    risks = format_list(analysis.get("risks") or alert.get("data_quality_reasons", []), limit=2)
    recommendation = analysis.get("recommendation", alert.get("alert_tier", "WATCH"))
    mvp = analysis.get("mvp", "Validate the niche manually before starting production.")
    return (
        f"Fresh Game Niche Alert: {alert.get('niche')}\n\n"
        "Platform: Google Play\n"
        "Scope: one AppStoreSpy query, no country/language filter\n"
        f"Window: {alert.get('release_date_window', 'last_180d')}; sort: {alert.get('collection_sort', '-release_date')}\n"
        f"Min daily installs per app in source query: {alert.get('min_app_daily_installs', 500)}\n"
        f"Score: {alert.get('opportunity_score')}/100\n"
        f"Data quality: {alert.get('data_quality_score')}/100\n"
        f"Daily installs: {alert.get('total_daily_installs')}\n"
        f"Apps in niche: {alert.get('app_count')}\n"
        f"New successful apps: {alert.get('successful_new_apps_count')}\n\n"
        "Why interesting:\n"
        f"{evidence}\n\n"
        "MVP:\n"
        f"{mvp}\n\n"
        "Risks:\n"
        f"{risks}\n\n"
        f"Recommendation: {recommendation}\n"
        f"Alert ID: {alert.get('alert_id')}"
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
        send_message(token, chat_id, format_alert_message(alert), int(telegram_cfg.get("max_message_chars", 3900)))
        sent.append(alert)
    return sent


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
