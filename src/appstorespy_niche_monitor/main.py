from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .alert_filter import apply_cooldown_and_alert_limits, mark_sent, split_candidates
from .candidate_generator import generate_candidates
from .cleaner import clean_apps
from .collector import collect_apps
from .config import load_config
from .data_quality import enrich_data_quality
from .feedback import feedback_adjustments, load_feedback, migrate_legacy_feedback_to_jsonl_once, read_feedback
from .first_run_handler import FIRST_RUN_NO_HISTORY, apply_initial_baseline_rules, detect_history_state
from .llm_report import analyze_candidate_pack, render_alert_report
from .report_writer import write_daily_reports
from .niche_classifier import classify_apps
from .scorer import score_summaries
from .storage import (
    ensure_storage,
    load_history_summaries,
    read_json,
    save_history_summaries,
    save_processed,
    save_raw,
    write_alert_report,
    write_json,
    write_weekly_report,
)
from .telegram_notify import send_alerts, send_initial_baseline_digest, send_message, send_run_summary
from .trend_detector import detect_trends
from .utils import utc_today
from .aggregator import aggregate_apps
from .weekly_digest import generate_weekly_digest


def run_pipeline(
    config_path: str | Path = "config.yaml",
    *,
    mode: str | None = None,
    snapshot_date: str | None = None,
    notify: bool | None = None,
    use_llm: bool = True,
) -> dict[str, Any]:
    config, config_dir = load_config(config_path)
    paths = ensure_storage(config, config_dir)
    snapshot_date = snapshot_date or utc_today()
    mode = mode or config.get("app", {}).get("mode", "dry-run")
    notify = (mode != "dry-run") if notify is None else notify

    if config.get("feedback", {}).get("migration", {}).get("auto_migrate_legacy_json_to_jsonl", True):
        migrate_legacy_feedback_to_jsonl_once(config, config_dir)
    feedback_records = load_feedback(config, config_dir)
    config = {**config, "_feedback_adjustments": feedback_adjustments(feedback_records, config)}

    raw_records = collect_apps(config, config_dir, mode=mode, snapshot_date=snapshot_date)
    raw_path = save_raw(paths, raw_records, snapshot_date)
    coverage_summary = raw_records[0].get("coverage", {}) if raw_records else {}

    apps = classify_apps(clean_apps(raw_records, snapshot_date), config)
    save_processed(paths, "apps", apps, snapshot_date)

    clusters = aggregate_apps(apps, config, snapshot_date)
    history = load_history_summaries(paths)
    history_state = detect_history_state(history, config, snapshot_date)
    compatible_history = [
        item
        for item in history
        if item.get("score_version") == config.get("app", {}).get("score_version", "v1.3.2")
    ]
    summaries = detect_trends(clusters, compatible_history, snapshot_date)
    summaries = enrich_data_quality(summaries, apps, config)
    summaries = score_summaries(summaries, config)

    save_processed(paths, "clusters", summaries, snapshot_date)
    save_processed(paths, "summaries", summaries, snapshot_date)

    sent_alerts = read_json(paths["sent_alerts_path"], {})
    candidates = generate_candidates(summaries, config, snapshot_date)
    candidates = apply_initial_baseline_rules(candidates, config, history_state)
    candidates = apply_cooldown_and_alert_limits(
        candidates,
        config,
        sent_alerts if isinstance(sent_alerts, dict) else {},
        snapshot_date,
    )

    history_summary = {
        "history_state": history_state,
        "first_run_without_history": history_state == FIRST_RUN_NO_HISTORY,
        "history_records_count": len(history),
    }
    pack_analysis = analyze_candidate_pack(
        candidates,
        config,
        use_llm=use_llm,
        coverage_summary=coverage_summary,
        history_summary=history_summary,
    )
    candidate_analyses = pack_analysis.get("candidate_analyses", {})
    candidate_analysis_sources = pack_analysis.get("candidate_analysis_sources", {})
    llm_status = pack_analysis.get("llm_status", {})
    analysis_source = str(pack_analysis.get("analysis_source", "fallback"))
    for candidate in candidates:
        candidate_id = str(candidate.get("candidate_id"))
        analysis = candidate_analyses.get(candidate_id)
        if analysis:
            candidate["llm_analysis"] = analysis
            candidate_source = str(candidate_analysis_sources.get(candidate_id, analysis_source))
            candidate["llm_analysis_source"] = candidate_source
            if isinstance(llm_status, dict):
                candidate["llm_status"] = llm_status
                fallback_reason = llm_status.get("fallback_reason")
                if candidate_source == "fallback_missing_from_openai" and not fallback_reason:
                    fallback_reason = "missing_from_openai_response"
                if fallback_reason:
                    candidate["llm_fallback_reason"] = fallback_reason
                if llm_status.get("fallback_detail"):
                    candidate["llm_fallback_detail"] = llm_status.get("fallback_detail")
            candidate["llm_summary"] = analysis.get("mvp_hypothesis") or analysis.get("summary")

    urgent_alerts, watch, near_misses, rejected, alert_candidates = split_candidates(candidates)
    llm_test_recommendations = sum(
        1
        for alert in urgent_alerts
        if str((alert.get("llm_analysis") or {}).get("recommendation", "")).upper() == "TEST"
    )
    report_paths: list[str] = []
    report_paths.extend(write_daily_reports(paths, candidates, snapshot_date))
    for alert in urgent_alerts:
        analysis = alert.get("llm_analysis", {})
        markdown = render_alert_report(alert, analysis)
        report_paths.append(str(write_alert_report(paths, alert, markdown)))

    save_processed(paths, "candidates", candidates, snapshot_date)
    save_processed(paths, "alerts", alert_candidates, snapshot_date)
    save_processed(paths, "sendable_alerts", urgent_alerts, snapshot_date)
    save_processed(paths, "watch", watch, snapshot_date)
    save_processed(paths, "near_misses", near_misses, snapshot_date)
    save_processed(paths, "rejected", rejected, snapshot_date)
    alert_funnel = build_alert_funnel(candidates, urgent_alerts, watch, near_misses, rejected)
    write_json(paths["processed_dir"] / f"{snapshot_date}_alert_funnel.json", alert_funnel)

    sent_count = 0
    initial_digest_sent = False
    if urgent_alerts and notify:
        sent = send_alerts(urgent_alerts, config)
        sent_count = len(sent)
        updated_sent_alerts = mark_sent(sent_alerts if isinstance(sent_alerts, dict) else {}, sent, snapshot_date)
        write_json(paths["sent_alerts_path"], updated_sent_alerts)
    initial_digest_items = [item for item in candidates if item.get("initial_baseline_digest")]
    if notify and mode == "production" and initial_digest_items:
        initial_digest_sent = send_initial_baseline_digest(initial_digest_items, config)

    history_path = save_history_summaries(paths, summaries, snapshot_date)
    result = {
        "mode": mode,
        "snapshot_date": snapshot_date,
        "raw_path": str(raw_path),
        "history_path": str(history_path),
        "apps_count": len(apps),
        "summaries_count": len(summaries),
        "candidates_count": len(candidates),
        "alerts_count": len(alert_candidates),
        "alert_candidates_count": len(alert_candidates),
        "sendable_alerts_count": len(urgent_alerts),
        "watch_count": len(watch),
        "single_app_watch_count": sum(1 for item in candidates if item.get("status") == "SINGLE_APP_WATCH"),
        "near_miss_count": len(near_misses),
        "rejected_count": len(rejected),
        "sent_count": sent_count,
        "telegram_regular_alerts_sent": sent_count,
        "llm_candidates_sent": len(urgent_alerts),
        "llm_test_recommendations": llm_test_recommendations,
        "separate_test_messages_sent": 0,
        "duplicate_market_signals_suppressed": alert_funnel["duplicate_market_signals_suppressed"],
        "cooldown_blocked_count": alert_funnel["cooldown_blocked_count"],
        "limit_blocked_count": alert_funnel["limit_blocked_count"],
        "initial_baseline_digest_count": len(initial_digest_items),
        "initial_baseline_digest_sent": initial_digest_sent,
        "history_state": history_state,
        "report_paths": report_paths,
        "baseline_only": history_state == FIRST_RUN_NO_HISTORY,
        "llm_status": llm_status,
    }
    result["completion_notification_sent"] = send_run_summary(result, config) if notify else False
    return result


def build_alert_funnel(
    candidates: list[dict[str, Any]],
    urgent_alerts: list[dict[str, Any]],
    watch: list[dict[str, Any]],
    near_misses: list[dict[str, Any]],
    rejected: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "candidates_count": len(candidates),
        "alert_candidates_count": sum(1 for item in candidates if item.get("status") == "ALERT"),
        "sendable_alerts_count": len(urgent_alerts),
        "watch_count": len(watch),
        "single_app_watch_count": sum(1 for item in candidates if item.get("status") == "SINGLE_APP_WATCH"),
        "near_miss_count": len(near_misses),
        "rejected_count": len(rejected),
        "duplicate_market_signals_suppressed": sum(
            1 for item in candidates if item.get("duplicate_reason") == "market_signal_duplicate"
        ),
        "cooldown_blocked_count": sum(
            1
            for item in candidates
            if "cooldown_exact_dedupe_key" in item.get("sendable_alert_failures", [])
            or "cooldown_normalized_niche" in item.get("sendable_alert_failures", [])
        ),
        "limit_blocked_count": sum(
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
        ),
        "failure_counts": count_sendable_failures(candidates),
    }


def count_sendable_failures(candidates: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for candidate in candidates:
        for failure in candidate.get("sendable_alert_failures", []):
            counts[str(failure)] = counts.get(str(failure), 0) + 1
    return dict(sorted(counts.items()))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the AppStoreSpy niche monitor pipeline.")
    parser.add_argument("--config", default="config.yaml")
    parser.add_argument("--mode", choices=["dry-run", "production"], default=None)
    parser.add_argument("--snapshot-date", default=None)
    parser.add_argument("--notify", action="store_true", help="Send Telegram alerts if candidates pass filters.")
    parser.add_argument("--no-llm", action="store_true", help="Use deterministic markdown reports instead of OpenAI.")
    parser.add_argument("--test-telegram", action="store_true", help="Send a small Telegram test message and exit.")
    parser.add_argument("--weekly-digest", action="store_true", help="Generate a weekly digest from history and feedback.")
    parser.add_argument(
        "--migrate-feedback",
        action="store_true",
        help="One-time migrate data/feedback.json to data/feedback.jsonl and exit.",
    )
    args = parser.parse_args(argv)

    if args.migrate_feedback:
        config, config_dir = load_config(args.config)
        result = migrate_legacy_feedback_to_jsonl_once(config, config_dir)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    if args.weekly_digest:
        config, config_dir = load_config(args.config)
        paths = ensure_storage(config, config_dir)
        snapshot_date = args.snapshot_date or utc_today()
        markdown = generate_weekly_digest(
            load_history_summaries(paths),
            read_feedback(paths["feedback_path"]),
            config,
            snapshot_date=snapshot_date,
        )
        path = write_weekly_report(paths, snapshot_date, markdown)
        print(json.dumps({"weekly_digest_path": str(path)}, ensure_ascii=False, indent=2))
        return 0

    if args.test_telegram:
        config, _ = load_config(args.config)
        telegram = config.get("telegram", {})
        import os

        token = os.environ.get(telegram.get("bot_token_env", "TELEGRAM_BOT_TOKEN"))
        chat_id = os.environ.get(telegram.get("chat_id_env", "TELEGRAM_CHAT_ID"))
        if not token or not chat_id:
            raise RuntimeError("Telegram token/chat env vars are required for --test-telegram.")
        send_message(token, chat_id, "AppStoreSpy Niche Monitor test alert.")
        print(json.dumps({"test_telegram": "sent"}, indent=2))
        return 0

    result = run_pipeline(
        args.config,
        mode=args.mode,
        snapshot_date=args.snapshot_date,
        notify=args.notify,
        use_llm=not args.no_llm,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
