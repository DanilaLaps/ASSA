from __future__ import annotations

import datetime as dt
from collections import Counter
from typing import Any

from .alert_ranker import enrich_sendable_alert_fields, passes_sendable_hard_filters, sendable_rules
from .candidate_generator import generate_candidates
from .dedupe import dedupe_market_signals, make_alert_instance_id, make_dedupe_key, top_app_ids
from .utils import parse_date, slugify


def apply_cooldown_and_alert_limits(
    candidates: list[dict[str, Any]],
    config: dict[str, Any],
    sent_alerts: dict[str, Any],
    snapshot_date: str,
) -> list[dict[str, Any]]:
    limits = config.get("alert_limits", {})
    max_alerts = int(limits.get("max_alerts_per_run", 3))
    cooldown_days = int(limits.get("cooldown_days", config.get("alert_rules", {}).get("cooldown_days", 7)))
    rules = sendable_rules(config)
    enriched = dedupe_market_signals(enrich_sendable_alert_fields(candidates, config), config)
    by_id = {str(item.get("candidate_id")): dict(item) for item in enriched}
    ranked_alerts = sorted(
        [item for item in enriched if item.get("status") == "ALERT"],
        key=lambda item: (
            -float(item.get("sendable_alert_score", 0.0)),
            -float(item.get("opportunity_score", 0.0)),
            str(item.get("normalized_niche", "")),
        ),
    )
    sent_count = 0
    normalized_niche_counts: Counter[str] = Counter()
    core_mechanic_counts: Counter[str] = Counter()
    market_signal_counts: Counter[str] = Counter()
    max_per_niche = int(rules.get("max_sendable_per_normalized_niche", 1))
    max_per_mechanic = int(rules.get("max_sendable_per_core_mechanic", 2))
    max_per_market_signal = int(rules.get("max_sendable_per_market_signal_key", 1))

    for rank, candidate in enumerate(ranked_alerts, start=1):
        item = by_id[str(candidate.get("candidate_id"))]
        item["sendable_alert_rank"] = rank
        item["send_regular_alert"] = False
        item["telegram_delivery_channel"] = "daily_digest_only"
        item["alert_stage"] = "QUALIFIED_CANDIDATE_ONLY"
        item.setdefault("alert_filter_reasons", [])
        item.setdefault("sendable_alert_failures", [])
        item.setdefault("sendable_alert_reasons", [])

        if item.get("exclude_from_cooldown"):
            item["alert_stage"] = "INITIAL_BASELINE_DIGEST" if item.get("initial_baseline_digest") else "EXCLUDED_FROM_COOLDOWN"
            item["telegram_delivery_channel"] = "initial_baseline_digest" if item.get("initial_baseline_digest") else "none"
            add_filter_reasons(item, ["excluded_from_cooldown"])
            add_sendable_failures(item, ["excluded_from_cooldown"])
            continue

        hard_passed, hard_failures = passes_sendable_hard_filters(item, config)
        if item.get("duplicate_reason") == "market_signal_duplicate":
            hard_failures = append_reason(hard_failures, "duplicate_market_signal")
            hard_failures = append_reason(hard_failures, "market_signal_duplicate")
        if not hard_passed or hard_failures:
            add_filter_reasons(item, hard_failures or ["sendable_hard_filter_failed"])
            add_sendable_failures(item, hard_failures or ["sendable_hard_filter_failed"])
            continue

        cooldown_failures = cooldown_failure_reasons(
            str(item.get("dedupe_key")),
            str(item.get("normalized_niche")),
            sent_alerts,
            cooldown_days,
            snapshot_date,
        )
        if cooldown_failures:
            item["alert_stage"] = "COOLDOWN_BLOCKED"
            item["telegram_delivery_channel"] = "none"
            add_filter_reasons(item, ["cooldown", *cooldown_failures])
            add_sendable_failures(item, cooldown_failures)
            continue

        normalized_niche = str(item.get("normalized_niche") or "")
        core_mechanic = str(item.get("core_mechanic") or "")
        market_signal_key = str(item.get("market_signal_key") or "")
        limit_failures: list[str] = []
        if max_per_niche > 0 and normalized_niche_counts[normalized_niche] >= max_per_niche:
            limit_failures.append("per_niche_limit_blocked")
        if max_per_mechanic > 0 and core_mechanic_counts[core_mechanic] >= max_per_mechanic:
            limit_failures.append("per_core_mechanic_limit_blocked")
        if max_per_market_signal > 0 and market_signal_counts[market_signal_key] >= max_per_market_signal:
            limit_failures.append("duplicate_market_signal")
        if sent_count >= max_alerts:
            limit_failures.extend(["max_alerts_per_run_blocked", "telegram_budget_blocked"])
        if limit_failures:
            add_filter_reasons(item, ["alert_limit", *limit_failures])
            add_sendable_failures(item, limit_failures)
            continue

        item["send_regular_alert"] = True
        item["alert_stage"] = "SENDABLE_ALERT"
        item["telegram_delivery_channel"] = "regular_alert"
        item["first_blocking_failure"] = None
        add_filter_reasons(item, ["passed"])
        add_sendable_reasons(item, ["sendable_alert_selected", "telegram_budget_available"])
        sent_count += 1
        normalized_niche_counts[normalized_niche] += 1
        core_mechanic_counts[core_mechanic] += 1
        market_signal_counts[market_signal_key] += 1

    for item in by_id.values():
        if item.get("status") != "ALERT":
            item["send_regular_alert"] = False
            item.setdefault("alert_stage", "NONE")
            if item.get("status") in {"WATCH", "SINGLE_APP_WATCH", "NEAR_MISS"}:
                item.setdefault("telegram_delivery_channel", "daily_digest_only")
            else:
                item.setdefault("telegram_delivery_channel", "none")
    return sort_candidates(list(by_id.values()))


def split_candidates(
    candidates: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    alerts = [item for item in candidates if item.get("status") == "ALERT"]
    watch = [item for item in candidates if item.get("status") in {"WATCH", "SINGLE_APP_WATCH"}]
    near_misses = [item for item in candidates if item.get("status") == "NEAR_MISS"]
    rejected = [item for item in candidates if item.get("status") == "REJECT"]
    urgent_alerts = [
        item
        for item in alerts
        if item.get("send_regular_alert") is True and item.get("alert_stage") == "SENDABLE_ALERT"
    ]
    return urgent_alerts, watch, near_misses, rejected, alerts


def sort_candidates(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    status_rank = {"ALERT": 4, "SINGLE_APP_WATCH": 3, "NEAR_MISS": 2, "WATCH": 1, "REJECT": 0}
    return sorted(
        candidates,
        key=lambda item: (
            -status_rank.get(str(item.get("status")), 0),
            -float(item.get("sendable_alert_score", 0.0)),
            -float(item.get("opportunity_score", 0.0)),
            str(item.get("normalized_niche", "")),
        ),
    )


def append_reason(reasons: Any, reason: str) -> list[str]:
    values = list(reasons) if isinstance(reasons, list) else []
    if reason not in values:
        values.append(reason)
    return values


def add_filter_reasons(item: dict[str, Any], reasons: list[str]) -> None:
    values = list(item.get("alert_filter_reasons", []))
    for reason in reasons:
        values = append_reason(values, reason)
    item["alert_filter_reasons"] = values


def add_sendable_failures(item: dict[str, Any], failures: list[str]) -> None:
    values = list(item.get("sendable_alert_failures", []))
    for failure in failures:
        if failure and not item.get("first_blocking_failure"):
            item["first_blocking_failure"] = failure
        values = append_reason(values, failure)
    item["sendable_alert_failures"] = sorted(set(values))


def add_sendable_reasons(item: dict[str, Any], reasons: list[str]) -> None:
    values = list(item.get("sendable_alert_reasons", []))
    for reason in reasons:
        values = append_reason(values, reason)
    item["sendable_alert_reasons"] = sorted(set(values))


def should_alert(
    row: dict[str, Any],
    config: dict[str, Any],
    sent_alerts: dict[str, Any],
    snapshot_date: str,
) -> tuple[bool, list[str]]:
    candidate = generate_candidates([row], config, snapshot_date)[0]
    filtered = apply_cooldown_and_alert_limits([candidate], config, sent_alerts, snapshot_date)[0]
    reasons = filtered.get("failed_alert_conditions", []) or filtered.get("alert_filter_reasons", [])
    return bool(filtered.get("send_regular_alert")), reasons or ["passed"]


def filter_alerts(
    summaries: list[dict[str, Any]],
    config: dict[str, Any],
    sent_alerts: dict[str, Any],
    snapshot_date: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    candidates = generate_candidates(summaries, config, snapshot_date)
    candidates = apply_cooldown_and_alert_limits(candidates, config, sent_alerts, snapshot_date)
    urgent_alerts, watch, near_misses, rejected, _alerts = split_candidates(candidates)
    return urgent_alerts, watch + near_misses, rejected


def alert_key(row: dict[str, Any]) -> str:
    return str(row.get("dedupe_key") or make_dedupe_key(normalized_niche(row), top_app_ids(row), release_date_window(row)))


def build_alert_id(row: dict[str, Any], snapshot_date: str) -> str:
    return str(row.get("alert_instance_id") or make_alert_instance_id(snapshot_date, alert_key(row)))


def normalized_niche(row: dict[str, Any]) -> str:
    value = row.get("normalized_niche")
    if value:
        return str(value)
    return slugify(
        "_".join(
            str(row.get(field, ""))
            for field in ("niche", "core_mechanic", "theme", "meta")
            if row.get(field)
        )
    )


def release_date_window(row: dict[str, Any]) -> str:
    return str(row.get("release_date_window") or "last_180d")


def was_sent_recently(
    dedupe_key: str,
    normalized_niche_value: str,
    sent_alerts: dict[str, Any],
    cooldown_days: int,
    snapshot_date: str,
) -> bool:
    current = parse_date(snapshot_date)
    if current is None:
        return False
    for key, item in sent_alerts.items():
        if not isinstance(item, dict):
            item = {"last_sent_at": item}
        if key != dedupe_key and item.get("normalized_niche") != normalized_niche_value:
            continue
        last_sent = parse_date(item.get("last_sent_at"))
        if last_sent is not None and (current - last_sent).days < cooldown_days:
            return True
    return False


def cooldown_failure_reasons(
    dedupe_key: str,
    normalized_niche_value: str,
    sent_alerts: dict[str, Any],
    cooldown_days: int,
    snapshot_date: str,
) -> list[str]:
    current = parse_date(snapshot_date)
    if current is None:
        return []
    failures: list[str] = []
    for key, item in sent_alerts.items():
        if not isinstance(item, dict):
            item = {"last_sent_at": item}
        key_matches = key == dedupe_key
        niche_matches = item.get("normalized_niche") == normalized_niche_value
        if not key_matches and not niche_matches:
            continue
        last_sent = parse_date(item.get("last_sent_at"))
        if last_sent is None or (current - last_sent).days >= cooldown_days:
            continue
        if key_matches:
            failures.append("cooldown_exact_dedupe_key")
        if niche_matches:
            failures.append("cooldown_normalized_niche")
    return sorted(set(failures))


def mark_sent(sent_alerts: dict[str, Any], alerts: list[dict[str, Any]], snapshot_date: str) -> dict[str, Any]:
    updated = dict(sent_alerts)
    now = dt.datetime.now(dt.UTC).isoformat()
    for alert in alerts:
        if (
            alert.get("exclude_from_cooldown")
            or alert.get("send_regular_alert") is not True
            or alert.get("alert_stage") != "SENDABLE_ALERT"
        ):
            continue
        key = str(alert.get("dedupe_key") or alert_key(alert))
        updated[key] = {
            "normalized_niche": alert.get("normalized_niche"),
            "last_sent_at": now if "T" in now else snapshot_date,
            "last_alert_instance_id": alert.get("alert_instance_id") or build_alert_id(alert, snapshot_date),
            "top_app_ids": top_app_ids(alert),
            "last_status": alert.get("status", "ALERT"),
            "opportunity_score": alert.get("opportunity_score"),
            "updated_at": now,
        }
    return updated
