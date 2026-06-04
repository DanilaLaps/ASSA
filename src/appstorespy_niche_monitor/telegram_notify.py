from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
from typing import Any


def format_alert_message(alert: dict[str, Any]) -> str:
    return (
        f"AppStoreSpy alert: {alert.get('niche')} / {alert.get('country')}\n"
        f"Score: {alert.get('opportunity_score')} | Quality: {alert.get('data_quality_score')}\n"
        f"Growth: {alert.get('weekly_growth_percent')}% | Daily installs: {alert.get('total_daily_installs')}\n"
        f"Mechanic: {alert.get('core_mechanic')} | Theme: {alert.get('theme')} | Audience: {alert.get('audience')}\n"
        f"Reasons: {', '.join(alert.get('reason_codes', [])) or 'none'}\n"
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
