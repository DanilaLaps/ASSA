from __future__ import annotations

import hashlib
from typing import Any


def stable_sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]


def make_dedupe_key(
    normalized_niche: str,
    top_app_ids: list[str],
    window: str = "last_180d",
) -> str:
    stable_apps = ",".join(sorted(str(app_id) for app_id in top_app_ids[:3] if app_id))
    raw = f"{normalized_niche}|{stable_apps}|{window}"
    return stable_sha256(raw)


def make_alert_instance_id(snapshot_date: str, dedupe_key: str) -> str:
    return f"{snapshot_date}:{dedupe_key}"


def top_app_ids(row: dict[str, Any], limit: int = 3) -> list[str]:
    ids = [
        str(app.get("app_id") or app.get("bundle") or app.get("name", ""))
        for app in row.get("top_apps", [])
        if app.get("app_id") or app.get("bundle") or app.get("name")
    ]
    return sorted(ids)[:limit]


def build_market_signal_key(candidate: dict[str, Any]) -> str:
    top3 = ",".join(top_app_ids(candidate, 3))
    top5 = ",".join(top_app_ids(candidate, 5))
    raw = "|".join(
        [
            str(candidate.get("normalized_niche") or candidate.get("niche") or "other"),
            str(candidate.get("core_mechanic") or "other"),
            str(candidate.get("theme") or "other"),
            str(candidate.get("meta") or "none"),
            top3,
            top5,
            str(candidate.get("release_date_window") or "last_180d"),
        ]
    )
    return stable_sha256(raw)


def build_market_signal_label(candidate: dict[str, Any]) -> str:
    values = [
        str(candidate.get("core_mechanic") or "other"),
        str(candidate.get("theme") or "other"),
        str(candidate.get("meta") or "none"),
    ]
    label = "/".join(value for value in values if value and value != "none")
    return label or str(candidate.get("normalized_niche") or candidate.get("niche") or "other")


def top_app_overlap(candidate_a: dict[str, Any], candidate_b: dict[str, Any], top_n: int = 5) -> float:
    left = set(top_app_ids(candidate_a, top_n))
    right = set(top_app_ids(candidate_b, top_n))
    if not left or not right:
        return 0.0
    return len(left & right) / min(len(left), len(right))


def is_duplicate_market_signal(
    candidate_a: dict[str, Any],
    candidate_b: dict[str, Any],
    threshold: float = 0.67,
) -> bool:
    if str(candidate_a.get("market_signal_key") or "") and candidate_a.get("market_signal_key") == candidate_b.get("market_signal_key"):
        return True
    return top_app_overlap(candidate_a, candidate_b) >= threshold


def dedupe_market_signals(candidates: list[dict[str, Any]], config: dict[str, Any]) -> list[dict[str, Any]]:
    rules = config.get("sendable_alert_rules", {})
    threshold = float(rules.get("market_signal_overlap_threshold", 0.67))
    ranked = sorted(
        [with_market_signal_defaults(candidate) for candidate in candidates],
        key=market_signal_rank,
        reverse=True,
    )
    primaries: list[dict[str, Any]] = []
    by_id: dict[str, dict[str, Any]] = {}
    for candidate in ranked:
        duplicate_of = next(
            (primary for primary in primaries if is_duplicate_market_signal(candidate, primary, threshold)),
            None,
        )
        item = dict(candidate)
        if duplicate_of is not None:
            item["duplicate_of_candidate_id"] = duplicate_of.get("candidate_id")
            item["duplicate_reason"] = "market_signal_duplicate"
            failures = list(item.get("sendable_alert_failures", []))
            if "duplicate_market_signal" not in failures:
                failures.append("duplicate_market_signal")
            item["sendable_alert_failures"] = sorted(set(failures))
        else:
            primaries.append(item)
        by_id[str(item.get("candidate_id"))] = item
    return [by_id.get(str(candidate.get("candidate_id")), with_market_signal_defaults(candidate)) for candidate in candidates]


def with_market_signal_defaults(candidate: dict[str, Any]) -> dict[str, Any]:
    item = dict(candidate)
    item["market_signal_key"] = item.get("market_signal_key") or build_market_signal_key(item)
    item["market_signal_label"] = item.get("market_signal_label") or build_market_signal_label(item)
    item.setdefault("duplicate_of_candidate_id", None)
    item.setdefault("duplicate_reason", None)
    return item


def market_signal_rank(candidate: dict[str, Any]) -> tuple[int, float, float, int, float, float, float, float, int, float, float]:
    status_rank = {"ALERT": 5, "WATCH": 4, "SINGLE_APP_WATCH": 3, "NEAR_MISS": 2, "REJECT": 1}
    specificity_rank = {
        "core_mechanic_theme_meta": 5,
        "normalized_niche": 4,
        "core_mechanic_theme": 3,
        "market_category_core_mechanic": 2,
        "core_mechanic": 1,
    }
    unknown_blocker_penalty = 10.0 if bool(candidate.get("unknown_pattern_blocker_active")) else 0.0
    opportunity_blocker_penalty = 5.0 if bool(candidate.get("unknown_pattern_blocker_active")) else 0.0
    return (
        status_rank.get(str(candidate.get("status")), 0),
        float(candidate.get("sendable_alert_score", 0.0)) - unknown_blocker_penalty,
        float(candidate.get("opportunity_score", 0.0)) - opportunity_blocker_penalty,
        specificity_rank.get(str(candidate.get("group_key_type")), 0),
        -float(candidate.get("unknown_app_share", 0.0)),
        -float(candidate.get("unknown_installs_share", 0.0)),
        float(candidate.get("classification_confidence_avg", 0.0)),
        float(candidate.get("data_quality_score", 0.0)),
        int(candidate.get("app_count", 0)),
        float(candidate.get("sendable_alert_score", 0.0)),
        float(candidate.get("opportunity_score", 0.0)),
    )
