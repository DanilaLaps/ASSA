from __future__ import annotations

import datetime as dt
import json
import shutil
from pathlib import Path
from typing import Any

from .config import resolve_path
from .dedupe import stable_sha256


def feedback_paths(config: dict[str, Any], config_dir: Path) -> dict[str, Path]:
    feedback_cfg = config.get("feedback", {})
    migration_cfg = feedback_cfg.get("migration", {})
    return {
        "jsonl": resolve_path(config_dir, feedback_cfg.get("path", "data/feedback.jsonl")),
        "legacy": resolve_path(config_dir, feedback_cfg.get("legacy_path", "data/feedback.json")),
        "state": resolve_path(config_dir, migration_cfg.get("migration_state_path", "data/feedback_migration_state.json")),
        "backup_template": resolve_path(
            config_dir,
            migration_cfg.get("backup_path_template", "data/feedback.migrated.{timestamp}.json"),
        ),
    }


def migrate_legacy_feedback_to_jsonl_once(
    config: dict[str, Any],
    config_dir: Path,
) -> dict[str, Any]:
    feedback_cfg = config.get("feedback", {})
    migration_cfg = feedback_cfg.get("migration", {})
    paths = feedback_paths(config, config_dir)
    jsonl_path = paths["jsonl"]
    legacy_path = paths["legacy"]
    jsonl_path.parent.mkdir(parents=True, exist_ok=True)
    if not jsonl_path.exists():
        jsonl_path.write_text("", encoding="utf-8")
    if not legacy_path.exists():
        return {
            "migration": "skipped",
            "reason": "legacy_missing",
            "jsonl_path": str(jsonl_path),
            "legacy_path": str(legacy_path),
        }

    migrated_at = dt.datetime.now(dt.UTC).isoformat()
    source_text = legacy_path.read_text(encoding="utf-8")
    source_sha = stable_sha256(source_text)
    try:
        legacy_records = parse_legacy_feedback(source_text)
    except json.JSONDecodeError as exc:
        warning = f"Invalid legacy feedback JSON: {exc}"
        if migration_cfg.get("fail_on_invalid_legacy_json", False):
            raise
        return write_migration_state(
            paths["state"],
            {
                "migration": "skipped",
                "warning": warning,
                "source_sha256": source_sha,
                "migrated_count": 0,
                "skipped_duplicates_count": 0,
                "backup_path": None,
                "migrated_at": migrated_at,
            },
        )

    existing = load_feedback(config, config_dir)
    existing_ids = {feedback_event_id(item) for item in existing}
    normalized_records = [normalize_feedback_entry(record, migrated_at=migrated_at) for record in legacy_records]
    records_to_write: list[dict[str, Any]] = []
    skipped_count = 0
    for normalized in normalized_records:
        event_id = feedback_event_id(normalized)
        if event_id in existing_ids:
            skipped_count += 1
            continue
        existing_ids.add(event_id)
        records_to_write.append(normalized)

    if not records_to_write:
        return write_migration_state(
            paths["state"],
            {
                "migration": "completed",
                "source_sha256": source_sha,
                "migrated_count": 0,
                "skipped_duplicates_count": skipped_count,
                "backup_path": None,
                "migrated_at": migrated_at,
                "jsonl_path": str(jsonl_path),
                "legacy_path": str(legacy_path),
            },
        )

    backup_path = None
    if migration_cfg.get("create_backup_before_migration", True):
        timestamp = migrated_at.replace(":", "").replace("-", "").replace(".", "")
        backup_path = Path(str(paths["backup_template"]).replace("{timestamp}", timestamp))
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(legacy_path, backup_path)

    with jsonl_path.open("a", encoding="utf-8") as handle:
        for normalized in records_to_write:
            handle.write(json.dumps(normalized, ensure_ascii=False, separators=(",", ":")) + "\n")

    return write_migration_state(
        paths["state"],
        {
            "migration": "completed",
            "source_sha256": source_sha,
            "migrated_count": len(records_to_write),
            "skipped_duplicates_count": skipped_count,
            "backup_path": str(backup_path) if backup_path else None,
            "migrated_at": migrated_at,
            "jsonl_path": str(jsonl_path),
            "legacy_path": str(legacy_path),
        },
    )


def write_migration_state(path: Path, state: dict[str, Any]) -> dict[str, Any]:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    return state


def parse_legacy_feedback(text: str) -> list[dict[str, Any]]:
    data = json.loads(text)
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if isinstance(data, dict) and isinstance(data.get("items"), list):
        return [item for item in data["items"] if isinstance(item, dict)]
    if isinstance(data, dict):
        return [data]
    return []


def normalize_feedback_entry(record: dict[str, Any], *, migrated_at: str | None = None) -> dict[str, Any]:
    item = dict(record)
    if "verdict" not in item and "status" in item:
        item["verdict"] = item.pop("status")
    if "status" not in item and "verdict" in item:
        item["status"] = item["verdict"]
    if not item.get("created_at"):
        item["created_at"] = migrated_at or dt.datetime.now(dt.UTC).isoformat()
        item["created_at_inferred"] = True
    item.setdefault("false_positive_reasons", [])
    item.setdefault("notes", "")
    item.setdefault("source_format", "jsonl")
    item.setdefault("schema_version", "v1.3.2")
    if migrated_at is not None:
        item["migrated_from"] = "data/feedback.json"
        item["migrated_at"] = migrated_at
        item["source_format"] = "legacy_json"
        item["schema_version"] = "v1.3.2"
    item["feedback_id"] = item.get("feedback_id") or feedback_event_id(item)
    return item


def feedback_event_id(record: dict[str, Any]) -> str:
    if record.get("feedback_id"):
        return str(record["feedback_id"])
    raw = "|".join(
        str(record.get(field, ""))
        for field in ("created_at", "dedupe_key", "normalized_niche", "verdict", "reason")
    )
    return stable_sha256(raw)


def load_feedback(config: dict[str, Any], config_dir: Path) -> list[dict[str, Any]]:
    path = feedback_paths(config, config_dir)["jsonl"]
    if not path.exists():
        return []
    records: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict):
            records.append(normalize_feedback_entry(data))
    return records


def append_feedback(entry: dict[str, Any], config: dict[str, Any], config_dir: Path) -> None:
    path = feedback_paths(config, config_dir)["jsonl"]
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = normalize_feedback_entry(entry)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(normalized, ensure_ascii=False, separators=(",", ":")) + "\n")


def read_feedback(path: str | Path) -> list[dict[str, Any]]:
    feedback_path = Path(path)
    if not feedback_path.exists():
        return []
    if feedback_path.suffix == ".jsonl":
        records: list[dict[str, Any]] = []
        for line in feedback_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            data = json.loads(line)
            if isinstance(data, dict):
                records.append(normalize_feedback_entry(data))
        return records
    data = json.loads(feedback_path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if isinstance(data, dict) and isinstance(data.get("items"), list):
        return [item for item in data["items"] if isinstance(item, dict)]
    if isinstance(data, dict):
        return [data]
    return []


def write_feedback(path: str | Path, records: list[dict[str, Any]]) -> None:
    feedback_path = Path(path)
    feedback_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        json.dumps(normalize_feedback_entry(record), ensure_ascii=False, separators=(",", ":"))
        for record in records
    ]
    feedback_path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def add_feedback(
    path: str | Path,
    config: dict[str, Any],
    *,
    alert_id: str | None = None,
    dedupe_key: str | None = None,
    normalized_niche: str | None = None,
    status: str | None = None,
    verdict: str | None = None,
    reason: str,
    notes: str = "",
    reviewed_at: str | None = None,
) -> dict[str, Any]:
    feedback_cfg = config.get("feedback", {})
    final_verdict = verdict or status
    if final_verdict not in feedback_cfg.get("allowed_verdicts", feedback_cfg.get("allowed_statuses", [])):
        raise ValueError(f"Unsupported feedback verdict: {final_verdict}")
    record = normalize_feedback_entry(
        {
            "created_at": reviewed_at or dt.datetime.now(dt.UTC).isoformat(),
            "alert_id": alert_id,
            "dedupe_key": dedupe_key or alert_id,
            "normalized_niche": normalized_niche or "",
            "verdict": final_verdict,
            "reason": reason,
            "notes": notes,
            "source_format": "jsonl",
            "schema_version": "v1.3.2",
        }
    )
    feedback_path = Path(path)
    feedback_path.parent.mkdir(parents=True, exist_ok=True)
    with feedback_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
    return record


def feedback_summary(records: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for record in records:
        verdict = str(record.get("verdict", record.get("status", "unknown")))
        counts[verdict] = counts.get(verdict, 0) + 1
    return counts


def feedback_adjustments(records: list[dict[str, Any]], config: dict[str, Any]) -> dict[str, float]:
    if not config.get("feedback", {}).get("apply_weight_adjustments", True):
        return {}
    max_abs = float(config.get("feedback", {}).get("max_weight_adjustment_abs", 0.2))
    adjustments = {
        "paid_spike_penalty_multiplier": 1.0,
        "competition_penalty_multiplier": 1.0,
        "watch_threshold_delta": 0.0,
        "mvp_feasibility_delta": 0.0,
    }
    for record in records:
        verdict = record.get("verdict")
        reasons = set(record.get("false_positive_reasons") or [])
        reason = str(record.get("reason", ""))
        if verdict == "false_positive" and ("paid_spike" in reasons or reason == "paid_spike"):
            adjustments["paid_spike_penalty_multiplier"] += 0.05
        if verdict == "false_positive" and ("too_competitive" in reasons or reason in {"too_competitive", "giant_dominated"}):
            adjustments["competition_penalty_multiplier"] += 0.05
        if verdict == "good":
            adjustments["watch_threshold_delta"] -= 0.5
        if verdict == "too_complex":
            adjustments["mvp_feasibility_delta"] -= 1.0
    for key, value in list(adjustments.items()):
        if key.endswith("_multiplier"):
            adjustments[key] = max(1.0 - max_abs, min(1.0 + max_abs, value))
        else:
            adjustments[key] = max(-max_abs * 100, min(max_abs * 100, value))
    return adjustments
