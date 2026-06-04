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

PACK_ANALYSIS_FIELDS = (
    "recommendation",
    "confidence",
    "why_interesting",
    "why_might_be_false_positive",
    "mvp_hypothesis",
    "simplified_mvp_scope",
    "validation_steps",
    "risk_notes",
    "missing_data",
    "manual_review_needed",
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
    return fallback


def build_llm_status(pack_input: dict[str, Any], config: dict[str, Any], *, use_llm: bool) -> dict[str, Any]:
    llm_cfg = config.get("llm", {})
    enabled = bool(llm_cfg.get("enabled", True))
    model_env = str(llm_cfg.get("model_env", "OPENAI_MODEL"))
    model = os.environ.get(model_env) or llm_cfg.get("default_model", "gpt-4.1-mini")
    api_key_present = bool(os.environ.get("OPENAI_API_KEY"))
    if not use_llm:
        source = "fallback"
        reason = "disabled_by_cli"
    elif not enabled:
        source = "fallback"
        reason = "disabled_in_config"
    elif not api_key_present:
        source = "fallback"
        reason = "missing_openai_api_key"
    else:
        source = "openai_pending"
        reason = None
    counts = {
        "alerts": len(pack_input.get("alerts", [])),
        "watch": len(pack_input.get("watch", [])),
        "near_misses": len(pack_input.get("near_misses", [])),
        "initial_baseline_digest": len(pack_input.get("initial_baseline_digest", [])),
    }
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
    alerts = [item for item in candidates if item.get("status") == "ALERT"][: int(limits.get("max_alerts_per_run", 3))]
    watch = [
        item
        for item in candidates
        if item.get("status") in {"WATCH", "SINGLE_APP_WATCH"}
    ][: int(limits.get("max_watch_items_per_digest", 10))]
    near_misses = [
        item for item in candidates if item.get("status") == "NEAR_MISS"
    ][: int(limits.get("max_near_misses_in_report", 10))]
    initial = [
        item for item in candidates if item.get("initial_baseline_digest")
    ][: int(config.get("first_run_behavior", {}).get("max_initial_digest_items", 10))]
    return {
        "alerts": [compact_candidate_for_llm(item) for item in alerts],
        "watch": [compact_candidate_for_llm(item) for item in watch],
        "near_misses": [compact_candidate_for_llm(item) for item in near_misses],
        "initial_baseline_digest": [compact_candidate_for_llm(item) for item in initial],
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


def compact_candidate_for_llm(candidate: dict[str, Any]) -> dict[str, Any]:
    fields = (
        "candidate_id",
        "dedupe_key",
        "status",
        "would_be_status",
        "normalized_niche",
        "group_key_type",
        "group_key_value",
        "market_category",
        "core_mechanic",
        "theme",
        "meta",
        "audience_summary",
        "app_count",
        "total_daily_installs",
        "opportunity_score",
        "score_components",
        "data_quality_score",
        "mvp_feasibility_score",
        "risk_tags",
        "reason_codes",
        "failed_alert_conditions",
        "confidence_level",
        "first_run_without_history",
    )
    compact = {field: candidate.get(field) for field in fields if field in candidate}
    compact["top_apps"] = [
        {
            "app_id": app.get("app_id"),
            "name": app.get("name"),
            "developer_name": app.get("developer_name"),
            "downloads_daily": app.get("downloads_daily"),
            "release_date": app.get("release_date"),
            "advertised": app.get("advertised"),
            "ads": app.get("ads"),
            "iap": app.get("iap"),
        }
        for app in candidate.get("top_apps", [])[:5]
    ]
    return compact


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
    why_interesting = candidate.get("reason_codes", [])[:3]
    risk_notes = candidate.get("risk_tags", [])
    mvp_hypothesis = f"Test a scoped {candidate.get('core_mechanic')} game with {candidate.get('theme')} presentation."
    return {
        "recommendation": recommendation,
        "confidence": confidence,
        "why_interesting": why_interesting,
        "why_might_be_false_positive": risk_notes[:4],
        "mvp_hypothesis": mvp_hypothesis,
        "simplified_mvp_scope": "One core loop, one content theme, lightweight meta progression.",
        "validation_steps": [
            "Check top apps manually in AppStoreSpy and stores.",
            "Separate organic traction from paid acquisition.",
            "Review creatives and monetization signals before production.",
        ],
        "risk_notes": risk_notes,
        "missing_data": candidate.get("failed_alert_conditions", []),
        "manual_review_needed": status in {"WATCH", "SINGLE_APP_WATCH", "NEAR_MISS"} or first_run,
        "summary": (
            f"{candidate.get('normalized_niche')} is a {recommendation} candidate in this single-query AppStoreSpy slice."
        ),
        "signal": ", ".join(why_interesting) or "Candidate passed deterministic scoring signals.",
        "evidence": why_interesting,
        "entry_realism": f"MVP feasibility score is {candidate.get('mvp_feasibility_score')}.",
        "mvp": mvp_hypothesis,
        "monetization": "Validate ads/IAP/revenue signals before production.",
        "risks": risk_notes or ["Need manual validation."],
        "checks": [
            "Check top apps manually in AppStoreSpy and stores.",
            "Confirm the signal is not paid traffic.",
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
        candidate_analyses[candidate_key] = normalize_pack_item_analysis(
            analysis,
            fallback_analyses.get(candidate_key, {}),
        )
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


def build_pack_prompt(pack_input: dict[str, Any]) -> str:
    compact = json.dumps(pack_input, ensure_ascii=False, indent=2)
    return (
        "You are a mobile-game niche analyst for a small team.\n"
        "Evaluate fresh Google Play games found by exactly one single-query AppStoreSpy request.\n"
        "The source query has no country, language, or active_countries filters. Do not call the slice global "
        "and do not make country-specific claims.\n"
        "Separate fresh demand from paid traffic spikes. Do not recommend direct competition with giant developers.\n"
        "Do not reject early single-app breakouts automatically; mark them as WATCH/manual validation when appropriate.\n"
        "If this is the first run without compatible history, do not call candidates confirmed alerts. Treat them as "
        "INITIAL_BASELINE_NO_HISTORY and cap confidence at medium.\n"
        "Return only a JSON object with key candidate_analyses. Its keys must be candidate_id values. Each value must contain "
        "recommendation TEST/WATCH/AVOID, confidence, why_interesting, why_might_be_false_positive, "
        "mvp_hypothesis, simplified_mvp_scope, validation_steps, risk_notes, missing_data, manual_review_needed.\n\n"
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
        "You are a mobile-game niche analyst for a small team.\n"
        "The candidate below comes from exactly one AppStoreSpy Google Play /play/apps/query request.\n"
        "The request intentionally has no country, language, or active_countries filters. Do not call this a global market "
        "and do not make country-specific claims.\n"
        "Do not recommend competing directly with giant developers. Do not infer opportunity from installs alone.\n"
        "Separate a large noisy market from a realistic small-team entry. If the signal is weak, concentrated, "
        "or resembles a paid traffic spike, choose WATCH or AVOID honestly.\n\n"
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
        "Do not invent metrics. Use only the JSON facts. Consider data_quality_score and false-positive risk.\n\n"
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
            "Source scope: one AppStoreSpy Google Play query, no country/language filters, "
            f"release window {alert.get('release_date_window', 'last_180d')}."
        ),
        (
            f"Daily installs: {alert.get('total_daily_installs')}; app count: {alert.get('app_count')}; "
            f"data quality: {alert.get('data_quality_score')}."
        ),
    ]
    if top_apps:
        evidence.append(f"Top confirming apps: {', '.join(top_apps[:3])}.")
    risks = list_risks(alert)
    return {
        "summary": (
            f"{alert.get('niche')} looks like a {recommendation} candidate in this single-query AppStoreSpy slice "
            f"with score {alert.get('opportunity_score')} and quality {alert.get('data_quality_score')}."
        ),
        "signal": (
            f"The signal combines demand, fresh app activity, monetization, data quality, and the micro-niche dimensions "
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
            "Do not treat the single-query slice as a country-specific or global market estimate.",
            "Confirm monetization per install before starting production.",
        ],
        "recommendation": recommendation,
    }


def list_risks(alert: dict[str, Any]) -> list[str]:
    risks: list[str] = []
    if float(alert.get("growth_by_one_app_share", 0.0)) >= 0.7 or float(alert.get("advertised_top_app_share", 0.0)) >= 0.7:
        risks.append("Growth or demand may be driven by one app or paid user acquisition.")
    if float(alert.get("top_app_share", 0.0)) >= 0.75:
        risks.append("Top app concentration is high.")
    if float(alert.get("giant_developer_share", 0.0)) >= 0.7:
        risks.append("Giant developer share is too high for direct competition.")
    if float(alert.get("data_quality_score", 0.0)) < 65:
        risks.append("Data quality is below the alert threshold.")
    if alert.get("production_complexity") == "high":
        risks.append("Production complexity is too high for the target small-team entry.")
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
