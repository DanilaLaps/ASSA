from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .alert_filter import filter_alerts, mark_sent
from .cleaner import clean_apps
from .collector import collect_apps
from .config import load_config
from .data_quality import enrich_data_quality
from .llm_report import generate_alert_report
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
)
from .telegram_notify import send_alerts, send_message
from .trend_detector import detect_trends
from .utils import utc_today
from .aggregator import aggregate_apps


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

    raw_records = collect_apps(config, config_dir, mode=mode, snapshot_date=snapshot_date)
    raw_path = save_raw(paths, raw_records, snapshot_date)

    apps = classify_apps(clean_apps(raw_records, snapshot_date), config)
    save_processed(paths, "apps", apps, snapshot_date)

    summaries = aggregate_apps(apps, config, snapshot_date)
    history = load_history_summaries(paths)
    summaries = detect_trends(summaries, history, snapshot_date)
    summaries = enrich_data_quality(summaries, apps, config)
    summaries = score_summaries(summaries, config)

    save_processed(paths, "summaries", summaries, snapshot_date)

    sent_alerts = read_json(paths["sent_alerts_path"], {})
    alerts, watch, rejected = filter_alerts(summaries, config, sent_alerts if isinstance(sent_alerts, dict) else {}, snapshot_date)
    save_processed(paths, "alerts", alerts, snapshot_date)
    save_processed(paths, "watch", watch, snapshot_date)
    save_processed(paths, "rejected", rejected, snapshot_date)

    report_paths: list[str] = []
    for alert in alerts:
        markdown = generate_alert_report(alert, config, use_llm=use_llm)
        report_paths.append(str(write_alert_report(paths, alert, markdown)))

    sent_count = 0
    if alerts and notify:
        sent = send_alerts(alerts, config)
        sent_count = len(sent)
        updated_sent_alerts = mark_sent(sent_alerts if isinstance(sent_alerts, dict) else {}, sent, snapshot_date)
        write_json(paths["sent_alerts_path"], updated_sent_alerts)

    history_path = save_history_summaries(paths, summaries, snapshot_date)
    return {
        "mode": mode,
        "snapshot_date": snapshot_date,
        "raw_path": str(raw_path),
        "history_path": str(history_path),
        "apps_count": len(apps),
        "summaries_count": len(summaries),
        "alerts_count": len(alerts),
        "watch_count": len(watch),
        "rejected_count": len(rejected),
        "sent_count": sent_count,
        "report_paths": report_paths,
        "baseline_only": not any(item.get("has_history") for item in summaries),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the AppStoreSpy niche monitor pipeline.")
    parser.add_argument("--config", default="config.yaml")
    parser.add_argument("--mode", choices=["dry-run", "production"], default=None)
    parser.add_argument("--snapshot-date", default=None)
    parser.add_argument("--notify", action="store_true", help="Send Telegram alerts if candidates pass filters.")
    parser.add_argument("--no-llm", action="store_true", help="Use deterministic markdown reports instead of OpenAI.")
    parser.add_argument("--test-telegram", action="store_true", help="Send a small Telegram test message and exit.")
    args = parser.parse_args(argv)

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
