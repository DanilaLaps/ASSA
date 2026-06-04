from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
from typing import Any

from .appstorespy_client import AppStoreSpyClient
from .config import resolve_path
from .coverage import build_coverage_metadata, build_source_query_metadata
from .utils import parse_date


DEFAULT_SINGLE_QUERY_FIELDS = [
    "id",
    "name",
    "bundle",
    "developer_name",
    "developer_id",
    "category",
    "category_type",
    "downloads_daily",
    "downloads_month",
    "revenue_month",
    "downloads_exact",
    "downloads_mark",
    "rating_avg",
    "rating_count",
    "review_count",
    "release_date",
    "update_date",
    "iap",
    "advertised",
    "ads",
    "icon",
    "screenshots",
    "description_short",
    "description_full",
    "url_appstorespy",
    "url",
    "website",
]


FORBIDDEN_SINGLE_QUERY_KEYS = {"country", "language", "active_countries"}


def build_single_query_payload(config: dict[str, Any], today: str | dt.date) -> dict[str, Any]:
    collection = config.get("collection", {})
    filters = config.get("filters", {})
    today_date = parse_date(today)
    if today_date is None:
        raise ValueError(f"Invalid snapshot date for single query payload: {today}")
    days_back = int(collection.get("release_date_days_back", 180))
    release_date_gte = (today_date - dt.timedelta(days=days_back)).isoformat()

    payload: dict[str, Any] = {
        "limit": int(collection.get("limit", 250)),
        "page": int(collection.get("page", 1)),
        "sort": collection.get("sort", "-release_date"),
        "fields": list(collection.get("fields", DEFAULT_SINGLE_QUERY_FIELDS)),
        "filter": {
            "published": bool(filters.get("published", True)),
            "category_type": filters.get("category_type", "GAME"),
            "release_date": {"gte": release_date_gte},
            "downloads_daily": {"gte": int(collection.get("min_downloads_daily", 500))},
        },
    }
    validate_single_query_payload(payload, config)
    return payload


def validate_single_query_payload(payload: dict[str, Any], config: dict[str, Any]) -> None:
    collection = config.get("collection", {})
    forbidden_present = sorted(key for key in FORBIDDEN_SINGLE_QUERY_KEYS if key in payload)
    filter_forbidden_present = sorted(
        key for key in FORBIDDEN_SINGLE_QUERY_KEYS if key in payload.get("filter", {})
    )
    field_forbidden_present = sorted(
        key for key in FORBIDDEN_SINGLE_QUERY_KEYS if key in payload.get("fields", [])
    )
    if forbidden_present or filter_forbidden_present or field_forbidden_present:
        raise ValueError(
            "Single-query payload must not contain "
            f"{forbidden_present + [f'filter.{key}' for key in filter_forbidden_present] + [f'fields.{key}' for key in field_forbidden_present]}"
        )
    if collection.get("mode", "single_query") != "single_query":
        raise ValueError("Single-query mode requires collection.mode=single_query.")
    if collection.get("include_country", False):
        raise ValueError("Single-query mode requires include_country=false.")
    if collection.get("include_language", False):
        raise ValueError("Single-query mode requires include_language=false.")
    if collection.get("include_active_countries", False):
        raise ValueError("Single-query mode requires include_active_countries=false.")
    if payload.get("page") != 1:
        raise ValueError("Single-query payload must use page=1.")
    if payload.get("sort") != "-release_date":
        raise ValueError("Single-query payload must use sort=-release_date.")
    if collection.get("allow_pagination", False):
        raise ValueError("Single-query mode forbids pagination.")
    if int(collection.get("max_api_requests_per_run", 1)) != 1:
        raise ValueError("Single-query mode requires max_api_requests_per_run=1.")
    filter_payload = payload.get("filter", {})
    if filter_payload.get("published") is not True:
        raise ValueError("Single-query payload must filter published=true.")
    if filter_payload.get("category_type") != "GAME":
        raise ValueError("Single-query payload must filter category_type=GAME.")
    if "gte" not in filter_payload.get("release_date", {}):
        raise ValueError("Single-query payload must include filter.release_date.gte.")
    if int(filter_payload.get("downloads_daily", {}).get("gte", 0)) < 500:
        raise ValueError("Single-query payload must include filter.downloads_daily.gte >= 500.")


def collect_apps(
    config: dict[str, Any],
    config_dir: Path,
    *,
    mode: str,
    snapshot_date: str,
    client: AppStoreSpyClient | None = None,
) -> list[dict[str, Any]]:
    if mode == "dry-run":
        return collect_sample(config, config_dir, snapshot_date=snapshot_date)
    return [collect_once(client or AppStoreSpyClient(), config, snapshot_date)]


def collect_once(api_client: AppStoreSpyClient, config: dict[str, Any], snapshot_date: str) -> dict[str, Any]:
    payload = build_single_query_payload(config, snapshot_date)
    timeout = int(config.get("collection", {}).get("request_timeout_seconds", 60))
    response = api_client.query_play_apps(payload, timeout=timeout)
    source_query = build_source_query_metadata(payload, config)
    coverage = build_coverage_metadata(response, payload, config)
    return {
        "snapshot_date": snapshot_date,
        "platform": config.get("collection", {}).get("platform", "google_play"),
        "collection_mode": "single_query",
        "endpoint": config.get("collection", {}).get("endpoint", "/play/apps/query"),
        "api_request_index": 1,
        "api_requests_count": 1,
        "query": payload,
        "source_query": source_query,
        "coverage": coverage,
        "response": response,
    }


def collect_sample(config: dict[str, Any], config_dir: Path, *, snapshot_date: str) -> list[dict[str, Any]]:
    sample_path = resolve_path(config_dir, config.get("app", {}).get("sample_data_path", "data/sample/sample_apps.json"))
    data = json.loads(sample_path.read_text(encoding="utf-8"))
    apps = data.get("apps", data) if isinstance(data, dict) else data
    if not isinstance(apps, list):
        raise ValueError(f"Sample data must contain a list of apps: {sample_path}")
    payload = build_single_query_payload(config, snapshot_date)
    response = {"data": apps, "total_count": len(apps)}
    return [
        {
            "snapshot_date": snapshot_date,
            "platform": config.get("collection", {}).get("platform", "google_play"),
            "collection_mode": "single_query_dry_run",
            "endpoint": config.get("collection", {}).get("endpoint", "/play/apps/query"),
            "api_request_index": 0,
            "api_requests_count": 0,
            "query": {**payload, "dry_run_source": str(sample_path)},
            "source_query": build_source_query_metadata(payload, config),
            "coverage": build_coverage_metadata(response, payload, config),
            "response": response,
        }
    ]
