from __future__ import annotations

from collections import Counter
from typing import Any

from .feedback import feedback_summary


def generate_weekly_digest(
    summaries: list[dict[str, Any]],
    feedback_records: list[dict[str, Any]],
    config: dict[str, Any],
    *,
    snapshot_date: str | None = None,
) -> str:
    latest_date = snapshot_date or latest_snapshot_date(summaries)
    latest = [row for row in summaries if row.get("snapshot_date") == latest_date] if latest_date else []
    ranked = sorted(latest, key=lambda row: float(row.get("opportunity_score", 0.0)), reverse=True)
    top_watch = [
        row
        for row in ranked
        if float(row.get("data_quality_score", 0.0)) >= 50
        and float(row.get("opportunity_score", 0.0)) >= float(config.get("alert_rules", {}).get("min_opportunity_score", 75)) - 20
    ][:10]
    other_rows = [row for row in ranked if row.get("niche") == "other"][:10]
    suspicious_rows = [
        row
        for row in ranked
        if float(row.get("growth_by_one_app_share", 0.0)) >= 0.6
        or float(row.get("top_app_share", 0.0)) >= 0.75
        or float(row.get("giant_developer_share", 0.0)) >= 0.7
    ][:10]
    reason_counts = Counter(str(row.get("reason", "unknown")) for row in feedback_records)
    recommendations = calibration_recommendations(feedback_records, other_rows, suspicious_rows)

    return (
        f"# Weekly AppStoreSpy Digest - {latest_date or 'no snapshot'}\n\n"
        "## Feedback summary\n"
        f"{format_mapping(feedback_summary(feedback_records))}\n\n"
        "## False-positive reasons\n"
        f"{format_mapping(dict(reason_counts))}\n\n"
        "## Top WATCH candidates\n"
        f"{format_summary_rows(top_watch)}\n\n"
        "## Niches classified as other\n"
        f"{format_summary_rows(other_rows)}\n\n"
        "## Suspicious paid-spike or concentration risks\n"
        f"{format_summary_rows(suspicious_rows)}\n\n"
        "## Calibration recommendations\n"
        f"{format_bullets(recommendations)}\n"
    )


def latest_snapshot_date(summaries: list[dict[str, Any]]) -> str:
    dates = sorted({str(row.get("snapshot_date")) for row in summaries if row.get("snapshot_date")})
    return dates[-1] if dates else ""


def calibration_recommendations(
    feedback_records: list[dict[str, Any]],
    other_rows: list[dict[str, Any]],
    suspicious_rows: list[dict[str, Any]],
) -> list[str]:
    reason_counts = Counter(str(row.get("reason", "")) for row in feedback_records)
    recommendations: list[str] = []
    if reason_counts.get("paid_spike", 0) or reason_counts.get("one_app_growth", 0) or suspicious_rows:
        recommendations.append("Review paid-spike penalties, data-quality reasons, and max_top_app_share before raising alert volume.")
    if reason_counts.get("giant_dominated", 0):
        recommendations.append("Expand giant_developers aliases and keep direct-competition alerts in AVOID/WATCH.")
    if reason_counts.get("weak_data_quality", 0):
        recommendations.append("Audit missing AppStoreSpy fields and keep min_data_quality_score at 65 or higher.")
    if other_rows:
        recommendations.append("Review top `other` rows and add niche_rules or dimension_rules for repeated patterns.")
    if not recommendations:
        recommendations.append("No calibration action yet; collect more feedback labels before tuning thresholds.")
    return recommendations


def format_summary_rows(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "- None."
    lines: list[str] = []
    for row in rows:
        lines.append(
            "- "
            f"{row.get('niche')} / {row.get('core_mechanic')} + {row.get('theme')}: "
            f"score {row.get('opportunity_score')}, quality {row.get('data_quality_score')}, "
            f"growth {row.get('weekly_growth_percent')}%, daily installs {row.get('total_daily_installs')}"
        )
    return "\n".join(lines)


def format_mapping(values: dict[str, int]) -> str:
    if not values:
        return "- None."
    return "\n".join(f"- {key}: {value}" for key, value in sorted(values.items()))


def format_bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- None."
