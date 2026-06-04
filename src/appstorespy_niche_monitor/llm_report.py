from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any


def generate_alert_report(alert: dict[str, Any], config: dict[str, Any], *, use_llm: bool = True) -> str:
    if use_llm and config.get("llm", {}).get("enabled", True) and os.environ.get("OPENAI_API_KEY"):
        try:
            return generate_openai_report(alert, config)
        except Exception as exc:  # pragma: no cover - network fallback
            fallback = generate_fallback_report(alert)
            return f"{fallback}\n\nLLM fallback note: {exc}\n"
    return generate_fallback_report(alert)


def generate_openai_report(alert: dict[str, Any], config: dict[str, Any]) -> str:
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
        "Write a concise Russian product-analysis report for this mobile-game niche alert.\n"
        "Use these sections: signal, evidence, 4-8 week MVP, monetization, risks, what to verify next.\n"
        "Do not invent metrics. Use only the JSON facts. Mention data quality and false-positive risk.\n\n"
        f"Alert JSON:\n{compact}"
    )


def generate_fallback_report(alert: dict[str, Any]) -> str:
    top_apps = "\n".join(
        f"- {app.get('name')} ({app.get('developer_name')}): {app.get('downloads_daily')} daily installs"
        for app in alert.get("top_apps", [])
    )
    components = json.dumps(alert.get("score_components", {}), ensure_ascii=False, indent=2)
    return (
        f"# Alert: {alert.get('alert_id')}\n\n"
        f"Tier: {alert.get('alert_tier', 'WATCH')}\n\n"
        "## Signal\n"
        f"Niche `{alert.get('niche')}` in {alert.get('country')} scored {alert.get('opportunity_score')} "
        f"with weekly growth {alert.get('weekly_growth_percent')}% and data quality "
        f"{alert.get('data_quality_score')}.\n\n"
        "## Classification\n"
        f"Market: {alert.get('market_category')}; mechanic: {alert.get('core_mechanic')}; "
        f"theme: {alert.get('theme')}; meta: {alert.get('meta')}; audience: {alert.get('audience')}; "
        f"complexity: {alert.get('production_complexity')}.\n\n"
        "## Evidence\n"
        f"Total daily installs: {alert.get('total_daily_installs')}; monthly revenue: "
        f"{alert.get('total_monthly_revenue')}; app count: {alert.get('app_count')}; "
        f"successful new apps: {alert.get('successful_new_apps_count')}.\n\n"
        "## Top apps\n"
        f"{top_apps or '- No top apps captured'}\n\n"
        "## Score components\n"
        f"```json\n{components}\n```\n\n"
        "## Risks\n"
        f"Reason codes: {', '.join(alert.get('reason_codes', [])) or 'none'}.\n"
        f"Filter notes: {', '.join(alert.get('alert_filter_reasons', [])) or 'none'}.\n"
    )
