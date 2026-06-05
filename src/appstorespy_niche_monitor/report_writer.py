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
    summaries: list[dict[str, Any]] | None = None,
) -> list[str]:
    reports_dir = paths["reports_daily_dir"]
    reports_dir.mkdir(parents=True, exist_ok=True)
    report_paths: list[str] = []
    candidates_json = reports_dir / f"{snapshot_date}_candidates.json"
    candidates_md = reports_dir / f"{snapshot_date}_candidates.md"
    write_json(candidates_json, candidates)
    candidates_md.write_text(render_candidates_report(candidates, snapshot_date, summaries), encoding="utf-8")
    report_paths.extend([str(candidates_json), str(candidates_md)])

    sendable_path = reports_dir / f"{snapshot_date}_sendable_alerts.md"
    sendable_path.write_text(render_sendable_alerts_report(candidates, snapshot_date), encoding="utf-8")
    report_paths.append(str(sendable_path))

    funnel_path = reports_dir / f"{snapshot_date}_alert_funnel.md"
    funnel_path.write_text(render_alert_funnel_report(candidates, snapshot_date, summaries), encoding="utf-8")
    report_paths.append(str(funnel_path))

    unknown_path = reports_dir / f"{snapshot_date}_unknown_diagnostics.md"
    unknown_path.write_text(
        render_unknown_diagnostics_report(candidates, snapshot_date, summaries),
        encoding="utf-8",
    )
    report_paths.append(str(unknown_path))

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


def render_candidates_report(
    candidates: list[dict[str, Any]],
    snapshot_date: str,
    summaries: list[dict[str, Any]] | None = None,
) -> str:
    counts = Counter(str(item.get("status", "UNKNOWN")) for item in candidates)
    stage_counts = Counter(str(item.get("alert_stage", "NONE")) for item in candidates)
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
        "## Alert Stage Counts",
        format_counter(stage_counts),
        "",
        "## Coverage",
        format_bullets(coverage_warnings or ["coverage_ok"]),
        "",
        "## Unknown Diagnostics",
        format_unknown_counts(summaries or candidates),
        "",
        "## Top Candidates",
        format_candidate_rows([item for item in candidates if item.get("status") != "REJECT"][:20]),
        "",
        "## Rejected Reason Distribution",
        format_counter(rejected_reasons),
    ]
    return "\n".join(lines) + "\n"


def render_sendable_alerts_report(candidates: list[dict[str, Any]], snapshot_date: str) -> str:
    rows = [
        item
        for item in candidates
        if item.get("status") == "ALERT"
        and item.get("send_regular_alert") is True
        and item.get("alert_stage") == "SENDABLE_ALERT"
    ]
    return "\n".join(
        [
            f"# Sendable Alerts - {snapshot_date}",
            "",
            "Source: single AppStoreSpy query without country/language filters.",
            "",
            format_candidate_rows(rows),
        ]
    ) + "\n"


def render_alert_funnel_report(
    candidates: list[dict[str, Any]],
    snapshot_date: str,
    summaries: list[dict[str, Any]] | None = None,
) -> str:
    status_counts = Counter(str(item.get("status", "UNKNOWN")) for item in candidates)
    stage_counts = Counter(str(item.get("alert_stage", "NONE")) for item in candidates)
    failure_counts = Counter(
        failure
        for item in candidates
        for failure in item.get("sendable_alert_failures", [])
    )
    duplicate_count = sum(1 for item in candidates if item.get("duplicate_reason") == "market_signal_duplicate")
    cooldown_count = sum(
        1
        for item in candidates
        if "cooldown_exact_dedupe_key" in item.get("sendable_alert_failures", [])
        or "cooldown_normalized_niche" in item.get("sendable_alert_failures", [])
    )
    limit_count = sum(
        1
        for item in candidates
        if any(
            failure in item.get("sendable_alert_failures", [])
            for failure in (
                "per_niche_limit_blocked",
                "per_core_mechanic_limit_blocked",
                "max_alerts_per_run_blocked",
                "telegram_budget_blocked",
            )
        )
    )
    lines = [
        f"# Alert Funnel - {snapshot_date}",
        "",
        "Source: single AppStoreSpy query without country/language filters.",
        "",
        "## Status Counts",
        format_counter(status_counts),
        "",
        "## Alert Stage Counts",
        format_counter(stage_counts),
        "",
        "## Blocked Counts",
        format_counter(
            Counter(
                {
                    "duplicate_market_signals_suppressed": duplicate_count,
                    "cooldown_blocked": cooldown_count,
                    "limit_blocked": limit_count,
                }
            )
        ),
        "",
        "## Unknown Diagnostics",
        format_unknown_counts(summaries or candidates),
        "",
        "## Sendable Failure Distribution",
        format_counter(failure_counts),
        "",
        "## Top Qualified But Not Sent",
        format_candidate_rows(
            [
                item
                for item in candidates
                if item.get("status") == "ALERT" and item.get("alert_stage") != "SENDABLE_ALERT"
            ][:20]
        ),
    ]
    return "\n".join(lines) + "\n"


def render_unknown_diagnostics_report(
    candidates: list[dict[str, Any]],
    snapshot_date: str,
    summaries: list[dict[str, Any]] | None = None,
) -> str:
    summary_rows = summaries or candidates
    blocked = [
        item
        for item in candidates
        if (
            item.get("unknown_pattern_blocker_active")
            or "unknown_pattern_blocker_active" in item.get("sendable_alert_failures", [])
            or "unknown_pattern_blocker_active" in item.get("failed_alert_conditions", [])
        )
    ]
    return "\n".join(
        [
            f"# Unknown Diagnostics - {snapshot_date}",
            "",
            "Source: single AppStoreSpy query without country/language filters.",
            "",
            "## Summary Counts",
            format_unknown_counts(summary_rows),
            "",
            "## Top Blocked By Unknown App Share",
            format_candidate_rows(
                sorted(blocked, key=lambda item: float(item.get("unknown_app_share", 0.0)), reverse=True)[:20]
            ),
            "",
            "## Top Blocked By Unknown Installs Share",
            format_candidate_rows(
                sorted(blocked, key=lambda item: float(item.get("unknown_installs_share", 0.0)), reverse=True)[:20]
            ),
        ]
    ) + "\n"


def write_no_sendable_diagnostics(
    paths: dict[str, Path],
    candidates: list[dict[str, Any]],
    snapshot_date: str,
) -> list[str]:
    diagnostics = build_no_sendable_diagnostics(candidates)
    json_path = paths["processed_dir"] / f"{snapshot_date}_no_sendable_diagnostics.json"
    markdown_path = paths["reports_daily_dir"] / f"{snapshot_date}_no_sendable_diagnostics.md"
    write_json(json_path, diagnostics)
    markdown_path.write_text(render_no_sendable_diagnostics_report(diagnostics, snapshot_date), encoding="utf-8")
    return [str(json_path), str(markdown_path)]


def write_manual_review_digest(
    paths: dict[str, Path],
    candidates: list[dict[str, Any]],
    snapshot_date: str,
) -> str:
    diagnostics = build_no_sendable_diagnostics(candidates)
    path = paths["reports_daily_dir"] / f"{snapshot_date}_manual_review_digest.md"
    path.write_text(render_manual_review_digest(diagnostics, snapshot_date), encoding="utf-8")
    return str(path)


def build_no_sendable_diagnostics(candidates: list[dict[str, Any]], limit: int = 20) -> dict[str, Any]:
    non_sendable_alerts = [
        item
        for item in candidates
        if item.get("status") == "ALERT"
        and not (item.get("send_regular_alert") is True and item.get("alert_stage") == "SENDABLE_ALERT")
    ]
    watch_candidates = [item for item in candidates if item.get("status") == "WATCH"]
    blocked_by_one = [
        item
        for item in candidates
        if not (item.get("send_regular_alert") is True and item.get("alert_stage") == "SENDABLE_ALERT")
        and int(item.get("hard_blockers_count", 0)) + int(item.get("soft_blockers_count", 0)) == 1
    ]
    return {
        "top_alert_candidates_closest_to_sendable": [
            compact_no_sendable_candidate(item)
            for item in sorted(
                non_sendable_alerts,
                key=lambda row: (
                    int(row.get("hard_blockers_count", 0)),
                    -float(row.get("sendable_alert_score", 0.0)),
                    -float(row.get("opportunity_score", 0.0)),
                ),
            )[:limit]
        ],
        "top_watch_candidates_closest_to_alert_or_sendable": [
            compact_no_sendable_candidate(item)
            for item in sorted(
                watch_candidates,
                key=lambda row: (
                    -float(row.get("opportunity_score", 0.0)),
                    -float(row.get("sendable_alert_score", 0.0)),
                ),
            )[:limit]
        ],
        "top_candidates_blocked_by_exactly_one_condition": [
            compact_no_sendable_candidate(item)
            for item in sorted(
                blocked_by_one,
                key=lambda row: (
                    int(row.get("hard_blockers_count", 0)),
                    -float(row.get("sendable_alert_score", 0.0)),
                    -float(row.get("opportunity_score", 0.0)),
                ),
            )[:limit]
        ],
    }


def compact_no_sendable_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    fields = (
        "candidate_id",
        "normalized_niche",
        "group_key_type",
        "market_signal_key",
        "status",
        "alert_strength",
        "opportunity_score",
        "sendable_alert_score",
        "trend_confidence_score",
        "team_fit_score",
        "data_quality_score",
        "classification_confidence_avg",
        "mvp_feasibility_score",
        "organic_confidence",
        "app_count",
        "successful_new_apps_count",
        "unique_developer_count",
        "total_daily_installs",
        "top_app_share",
        "top3_app_share",
        "growth_by_one_app_share",
        "advertised_top_app_share",
        "giant_developer_share",
        "single_developer_share",
        "unknown_app_share",
        "unknown_installs_share",
        "unknown_pattern_blocker_active",
        "risk_tags",
        "reason_codes",
        "first_blocking_failure",
        "sendable_alert_failures",
        "sendable_threshold_margins",
        "hard_blockers",
        "soft_blockers",
        "hard_blockers_count",
        "soft_blockers_count",
        "calibrated_promotion",
    )
    compact = {field: candidate.get(field) for field in fields if field in candidate}
    compact["top_apps"] = [
        {
            "name": app.get("name"),
            "developer": app.get("developer_name"),
            "downloads_daily": app.get("downloads_daily"),
            "rating": app.get("rating_avg"),
            "advertised": app.get("advertised"),
            "release_date": app.get("release_date"),
        }
        for app in candidate.get("top_apps", [])[:5]
        if isinstance(app, dict)
    ]
    return compact


def render_no_sendable_diagnostics_report(diagnostics: dict[str, Any], snapshot_date: str) -> str:
    return "\n".join(
        [
            f"# No Sendable Diagnostics - {snapshot_date}",
            "",
            "Source: single AppStoreSpy query without country/language filters.",
            "",
            "## Top ALERT Candidates Closest To SENDABLE",
            format_no_sendable_rows(diagnostics.get("top_alert_candidates_closest_to_sendable", [])),
            "",
            "## Top WATCH Candidates Closest To ALERT/SENDABLE",
            format_no_sendable_rows(diagnostics.get("top_watch_candidates_closest_to_alert_or_sendable", [])),
            "",
            "## Top Candidates Blocked By Exactly One Condition",
            format_no_sendable_rows(diagnostics.get("top_candidates_blocked_by_exactly_one_condition", [])),
        ]
    ) + "\n"


def render_manual_review_digest(diagnostics: dict[str, Any], snapshot_date: str) -> str:
    return "\n".join(
        [
            f"# No strong SENDABLE alerts today. Closest candidates for manual review only. - {snapshot_date}",
            "",
            "These candidates are not regular Telegram alerts and must not be written to sent_alerts.",
            "",
            "## Closest ALERT Candidates",
            format_no_sendable_rows(diagnostics.get("top_alert_candidates_closest_to_sendable", [])[:10]),
            "",
            "## One-Condition Calibration Set",
            format_no_sendable_rows(diagnostics.get("top_candidates_blocked_by_exactly_one_condition", [])[:10]),
        ]
    ) + "\n"


def format_no_sendable_rows(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "- None."
    lines: list[str] = []
    for row in rows:
        lines.append(
            "- "
            f"{row.get('status')} {row.get('normalized_niche')} "
            f"strength={row.get('alert_strength')} "
            f"sendable={row.get('sendable_alert_score')} "
            f"opportunity={row.get('opportunity_score')} "
            f"hard={row.get('hard_blockers_count', 0)} "
            f"soft={row.get('soft_blockers_count', 0)} "
            f"first_blocking={row.get('first_blocking_failure') or 'none'} "
            f"organic={row.get('organic_confidence')}"
        )
        blockers = row.get("hard_blockers") or row.get("soft_blockers") or row.get("sendable_alert_failures") or []
        if blockers:
            lines.append(f"  - blockers: {', '.join(str(item) for item in blockers)}")
        top_apps = row.get("top_apps") or []
        if top_apps:
            app_bits = [
                f"{app.get('name')} ({app.get('developer')}): {app.get('downloads_daily')}"
                for app in top_apps[:3]
            ]
            lines.append(f"  - top_apps: {'; '.join(app_bits)}")
    return "\n".join(lines)


def format_unknown_counts(rows: list[dict[str, Any]]) -> str:
    counter = Counter(
        {
            "mixed_unknown_cluster": sum(1 for item in rows if item.get("mixed_unknown_cluster")),
            "unknown_dominant_cluster": sum(1 for item in rows if item.get("unknown_dominant_cluster")),
            "unknown_pattern_blocker_active": sum(1 for item in rows if item.get("unknown_pattern_blocker_active")),
        }
    )
    return format_counter(counter)


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
            f"score={row.get('opportunity_score')} sendable={row.get('sendable_alert_score')} "
            f"stage={row.get('alert_stage')} quality={row.get('data_quality_score')} "
            f"mvp={row.get('mvp_feasibility_score')} installs={row.get('total_daily_installs')} "
            f"unknown_app_share={row.get('unknown_app_share', 0)} "
            f"unknown_installs_share={row.get('unknown_installs_share', 0)} "
            f"first_blocking={row.get('first_blocking_failure') or 'none'} "
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
