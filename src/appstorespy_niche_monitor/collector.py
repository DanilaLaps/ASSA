from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from .appstorespy_client import AppStoreSpyClient
from .config import resolve_path


def build_play_query(config: dict[str, Any], country: str, category: str, sort: str, page: int) -> dict[str, Any]:
    limits = config.get("collection_limits", {})
    payload: dict[str, Any] = {
        "limit": limits.get("apps_per_query", 200),
        "page": page,
        "sort": sort,
        "country": country,
        "language": config.get("languages", {}).get(country, "en_US"),
        "fields": [
            "id",
            "name",
            "developer_name",
            "category",
            "category_type",
            "description",
            "downloads_daily",
            "downloads_month",
            "revenue_month",
            "downloads_exact",
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
            "url_appstorespy",
        ],
        "filter": {"published": True, "category_type": "GAME"},
    }
    if category != "GAME":
        payload["filter"]["category"] = category
    return payload


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

    api_client = client or AppStoreSpyClient()
    limits = config.get("collection_limits", {})
    pause_seconds = float(limits.get("request_pause_seconds", 0.5))
    max_pages = int(limits.get("max_pages_per_query", 1))
    records: list[dict[str, Any]] = []

    for country in config.get("countries", []):
        for category in config.get("categories", []):
            for sort in config.get("sorts", []):
                for page in range(1, max_pages + 1):
                    query = build_play_query(config, country, category, sort, page)
                    response = api_client.query_play_apps(query)
                    records.append(
                        {
                            "snapshot_date": snapshot_date,
                            "platform": "google_play",
                            "country": country,
                            "category": category,
                            "sort": sort,
                            "page": page,
                            "query": query,
                            "response": response,
                        }
                    )
                    time.sleep(pause_seconds)
    return records


def collect_sample(config: dict[str, Any], config_dir: Path, *, snapshot_date: str) -> list[dict[str, Any]]:
    sample_path = resolve_path(config_dir, config.get("app", {}).get("sample_data_path", "data/sample/sample_apps.json"))
    data = json.loads(sample_path.read_text(encoding="utf-8"))
    apps = data.get("apps", data) if isinstance(data, dict) else data
    if not isinstance(apps, list):
        raise ValueError(f"Sample data must contain a list of apps: {sample_path}")
    return [
        {
            "snapshot_date": snapshot_date,
            "platform": "google_play",
            "country": "sample",
            "category": "sample",
            "sort": "sample",
            "page": 1,
            "query": {"mode": "dry-run", "source": str(sample_path)},
            "response": {"apps": apps},
        }
    ]
