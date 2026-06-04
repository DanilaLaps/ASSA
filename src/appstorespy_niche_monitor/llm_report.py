from __future__ import annotations

import json
import os
import urllib.request
from typing import Any


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
        "Ты - аналитик рынка мобильных игр для маленькой команды.\n"
        "Не предлагай конкурировать напрямую с гигантами. Не делай вывод только по installs.\n"
        "Отделяй большой рынок от реалистичного входа. Если сигнал слабый или похож на paid traffic spike, "
        "честно выбери WATCH или AVOID.\n\n"
        "Проанализируй alert-кандидата из AppStoreSpy и верни только JSON object без markdown.\n"
        "JSON schema:\n"
        "{\n"
        '  "summary": "краткий вывод",\n'
        '  "signal": "почему это сигнал",\n'
        '  "evidence": ["факт 1", "факт 2"],\n'
        '  "entry_realism": "почему вход реалистичен или нереалистичен",\n'
        '  "mvp": "MVP-концепт на 4-8 недель",\n'
        '  "monetization": "монетизация",\n'
        '  "risks": ["риск 1", "риск 2"],\n'
        '  "checks": ["что проверить 1", "что проверить 2"],\n'
        '  "recommendation": "TEST|WATCH|AVOID"\n'
        "}\n"
        "Не выдумывай метрики. Используй только JSON facts. Учитывай data_quality_score и false-positive risk.\n\n"
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
    return analysis


def generate_fallback_analysis(alert: dict[str, Any]) -> dict[str, Any]:
    quality = float(alert.get("data_quality_score", 0.0))
    score = float(alert.get("opportunity_score", 0.0))
    filter_reasons = set(alert.get("alert_filter_reasons", []))
    reason_codes = set(alert.get("reason_codes", []))
    if alert.get("alert_tier") == "TEST" and quality >= 70 and score >= 75:
        recommendation = "TEST"
    elif "giant_dominated" in reason_codes or "top_app_concentration" in reason_codes:
        recommendation = "AVOID"
    elif filter_reasons and filter_reasons != {"passed"}:
        recommendation = "WATCH"
    else:
        recommendation = "WATCH"

    top_apps = [str(app.get("name", "")) for app in alert.get("top_apps", []) if app.get("name")]
    evidence = [
        f"Daily installs: {alert.get('total_daily_installs')}; app count: {alert.get('app_count')}.",
        f"Weekly growth: {alert.get('weekly_growth_percent')}%; data quality: {alert.get('data_quality_score')}.",
    ]
    if top_apps:
        evidence.append(f"Top confirming apps: {', '.join(top_apps[:3])}.")
    risks = list_risks(alert)
    return {
        "summary": (
            f"{alert.get('niche')} in {alert.get('country')} looks like a {recommendation} candidate "
            f"with score {alert.get('opportunity_score')} and quality {alert.get('data_quality_score')}."
        ),
        "signal": (
            f"The signal combines demand, growth, fresh app activity, and the micro-niche dimensions "
            f"{alert.get('core_mechanic')} + {alert.get('theme')} + {alert.get('meta')}."
        ),
        "evidence": evidence,
        "entry_realism": (
            f"Production complexity is {alert.get('production_complexity')}; this is most realistic for a small team "
            "when top-app concentration and giant share stay below the configured limits."
        ),
        "mvp": (
            f"Build a 4-8 week MVP around {alert.get('core_mechanic')} gameplay, {alert.get('theme')} theme, "
            f"and {alert.get('meta')} progression for {alert.get('audience')}."
        ),
        "monetization": "Test rewarded ads, interstitial pacing, and light IAP bundles after retention is validated.",
        "risks": risks,
        "checks": [
            "Verify whether growth is organic or paid user acquisition.",
            "Check the top apps manually in AppStoreSpy and stores.",
            "Confirm monetization per install before starting production.",
        ],
        "recommendation": recommendation,
    }


def list_risks(alert: dict[str, Any]) -> list[str]:
    risks: list[str] = []
    if float(alert.get("growth_by_one_app_share", 0.0)) >= 0.6:
        risks.append("Growth may be driven by one app or paid spike.")
    if float(alert.get("top_app_share", 0.0)) >= 0.75:
        risks.append("Top app concentration is high.")
    if float(alert.get("giant_developer_share", 0.0)) >= 0.7:
        risks.append("Giant developer share is too high for direct competition.")
    if float(alert.get("data_quality_score", 0.0)) < 70:
        risks.append("Data quality is below the alert threshold.")
    if not risks:
        risks.append("Need manual validation of store creatives, UA pressure, and retention assumptions.")
    return risks


def render_alert_report(alert: dict[str, Any], analysis: dict[str, Any]) -> str:
    top_apps = "\n".join(
        f"- {app.get('name')} ({app.get('developer_name')}): {app.get('downloads_daily')} daily installs"
        for app in alert.get("top_apps", [])
    )
    components = json.dumps(alert.get("score_components", {}), ensure_ascii=False, indent=2)
    analysis_json = json.dumps(analysis, ensure_ascii=False, indent=2)
    return (
        f"# Alert: {alert.get('alert_id')}\n\n"
        f"Recommendation: {analysis.get('recommendation')}\n\n"
        f"Tier: {alert.get('alert_tier', 'WATCH')}\n\n"
        "## Summary\n"
        f"{analysis.get('summary')}\n\n"
        "## Signal\n"
        f"{analysis.get('signal')}\n\n"
        "## Classification\n"
        f"Market: {alert.get('market_category')}; mechanic: {alert.get('core_mechanic')}; "
        f"theme: {alert.get('theme')}; meta: {alert.get('meta')}; audience: {alert.get('audience')}; "
        f"complexity: {alert.get('production_complexity')}.\n\n"
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
