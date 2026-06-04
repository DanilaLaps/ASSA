from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

from .storage import write_json


def write_daily_reports(
    paths: dict[str, Path],
    candidates: list[dict[str, Any]],
    snapshot_date: str,
) -> list[str]:
    reports_dir = paths["reports_daily_dir"]
    reports_dir.mkdir(parents=True, exist_ok=True)
    report_paths: list[str] = []
    candidates_json = reports_dir / f"{snapshot_date}_candidates.json"
    candidates_md = reports_dir / f"{snapshot_date}_candidates.md"
    write_json(candidates_json, candidates)
    candidates_md.write_text(render_candidates_report(candidates, snapshot_date), encoding="utf-8")
    report_paths.extend([str(candidates_json), str(candidates_md)])

    status_files = {
        "watch": [item for item in candidates if item.get("status") in {"WATCH", "SINGLE_APP_WATCH"}],
        "near_misses": [item for item in candidates if item.get("status") == "NEAR_MISS"],
        "rejected_summary": [item for item in candidates if item.get("status") == "REJECT"],
    }
    for name, rows in status_files.items():
        path = reports_dir / f"{snapshot_date}_{name}.md"
        path.write_text(render_status_report(name, rows, snapshot_date), encoding="utf-8")
        report_paths.append(str(path))

    initial_items = [item for item in candidates if item.get("initial_baseline_digest")]
    if initial_items:
        path = reports_dir / f"{snapshot_date}_initial_baseline_digest.md"
        path.write_text(render_initial_baseline_report(initial_items, snapshot_date), encoding="utf-8")
        report_paths.append(str(path))
    return report_paths


def render_candidates_report(candidates: list[dict[str, Any]], snapshot_date: str) -> str:
    counts = Counter(str(item.get("status", "UNKNOWN")) for item in candidates)
    rejected_reasons = Counter(
        reason
        for item in candidates
        if item.get("status") == "REJECT"
        for reason in item.get("failed_alert_conditions", [])
    )
    coverage_warnings = sorted(
        {
            tag
            for item in candidates
            for tag in item.get("risk_tags", [])
            if tag in {"sample_truncated", "unknown_coverage"}
        }
    )
    lines = [
        f"# Daily Candidates - {snapshot_date}",
        "",
        "Source: single AppStoreSpy query without country/language filters.",
        "",
        "## Status Counts",
        format_counter(counts),
        "",
        "## Coverage",
        format_bullets(coverage_warnings or ["coverage_ok"]),
        "",
        "## Top Candidates",
        format_candidate_rows([item for item in candidates if item.get("status") != "REJECT"][:20]),
        "",
        "## Rejected Reason Distribution",
        format_counter(rejected_reasons),
    ]
    return "\n".join(lines) + "\n"


def render_status_report(name: str, rows: list[dict[str, Any]], snapshot_date: str) -> str:
    return "\n".join(
        [
            f"# {name.replace('_', ' ').title()} - {snapshot_date}",
            "",
            format_candidate_rows(rows),
        ]
    ) + "\n"


def render_initial_baseline_report(rows: list[dict[str, Any]], snapshot_date: str) -> str:
    lines = [
        f"# Initial Baseline Discovery Report - {snapshot_date}",
        "",
        "Source: single AppStoreSpy query",
        "Window: releases from last 180 days",
        "History: no previous compatible snapshot",
        "Important: this is not a regular ALERT; confidence is capped at MEDIUM.",
    ]
    lines.extend(format_initial_llm_status(rows))
    lines.extend(["", "## Top Baseline Candidates"])
    for index, row in enumerate(rows, start=1):
        reason_codes = ", ".join(row.get("reason_codes", []))
        lines.append(
            f"{index}. {row.get('normalized_niche')} - would_be_status={row.get('would_be_status')}, "
            f"score={row.get('opportunity_score')}, installs={row.get('total_daily_installs')}, "
            f"reason_codes={reason_codes}"
        )
        lines.extend(format_initial_candidate_analysis(row))
    lines.extend(
        [
            "",
            "## Limitations",
            "- No historical growth confirmation.",
            "- Paid-spike risk is based only on the current slice.",
            "- These items were not written to sent_alerts and do not start cooldown.",
        ]
    )
    return "\n".join(lines) + "\n"


def format_initial_candidate_analysis(row: dict[str, Any]) -> list[str]:
    analysis = row.get("llm_analysis")
    if not isinstance(analysis, dict) or not analysis:
        return []
    source = str(row.get("llm_analysis_source") or "fallback")
    title = "AI Review" if source == "openai" else "Automated Review"
    recommendation = analysis.get("recommendation", "WATCH")
    confidence = analysis.get("confidence", row.get("confidence_level", "MEDIUM"))
    fallback_reason = row.get("llm_fallback_reason")
    fallback_detail = row.get("llm_fallback_detail")
    review_parts = [
        f"recommendation={recommendation}",
        f"confidence={confidence}",
        f"source={source}",
    ]
    if source != "openai" and fallback_reason:
        review_parts.append(f"fallback_reason={fallback_reason}")
    lines = [
        f"   - {title}: {', '.join(review_parts)}",
    ]
    if source != "openai" and fallback_detail:
        lines.append(f"     - fallback_detail: {fallback_detail}")
    lines.extend(format_indented_list("why_interesting", analysis.get("why_interesting"), indent="     "))
    lines.extend(
        format_indented_list(
            "false_positive_risks",
            analysis.get("why_might_be_false_positive") or analysis.get("risk_notes"),
            indent="     ",
        )
    )
    if analysis.get("mvp_hypothesis"):
        lines.append(f"     - mvp_hypothesis: {analysis.get('mvp_hypothesis')}")
    if analysis.get("simplified_mvp_scope"):
        lines.append(f"     - simplified_mvp_scope: {analysis.get('simplified_mvp_scope')}")
    lines.extend(format_indented_list("validation_steps", analysis.get("validation_steps"), indent="     "))
    missing_data = analysis.get("missing_data")
    if missing_data:
        lines.extend(format_indented_list("missing_data", missing_data, indent="     "))
    return lines


def format_initial_llm_status(rows: list[dict[str, Any]]) -> list[str]:
    status: dict[str, Any] = {}
    for row in rows:
        candidate_status = row.get("llm_status")
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


def format_indented_list(label: str, items: Any, *, indent: str) -> list[str]:
    if not items:
        return []
    values = items if isinstance(items, list) else [items]
    clean_values = [str(item).strip() for item in values if str(item).strip()]
    if not clean_values:
        return []
    lines = [f"{indent}- {label}:"]
    lines.extend(f"{indent}  - {item}" for item in clean_values[:4])
    return lines


def format_candidate_rows(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "- None."
    lines = []
    for row in rows:
        lines.append(
            "- "
            f"{row.get('status')} {row.get('normalized_niche')} "
            f"score={row.get('opportunity_score')} quality={row.get('data_quality_score')} "
            f"mvp={row.get('mvp_feasibility_score')} installs={row.get('total_daily_installs')} "
            f"risks={', '.join(row.get('risk_tags', [])) or 'none'}"
        )
    return "\n".join(lines)


def format_counter(counter: Counter[str]) -> str:
    if not counter:
        return "- None."
    return "\n".join(f"- {key}: {value}" for key, value in sorted(counter.items()))


def format_bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- None."


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
