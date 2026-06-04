from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from .appstorespy_client import AppStoreSpyClient, AppStoreSpyError
from .config import resolve_path


DEFAULT_PLAY_APP_FIELDS = [
    "id",
    "name",
    "developer_name",
    "category",
    "category_type",
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
]

APPSTORESPY_ALLOWED_LANGUAGES = {
    "en_US",
    "ar",
    "en_GB",
    "fr_FR",
    "es_419",
    "de_DE",
    "pt_BR",
    "it_IT",
    "ja_JP",
    "ko_KR",
    "tr_TR",
    "ru_RU",
    "vi",
}

LANGUAGE_ALIASES = {
    "es_MX": "es_419",
    "es_ES": "es_419",
    "en_IN": "en_US",
    "en_PH": "en_US",
    "id_ID": "en_US",
    "th_TH": "en_US",
    "vi_VN": "vi",
}


def build_play_query(config: dict[str, Any], country: str, category: str, sort: str, page: int) -> dict[str, Any]:
    limits = config.get("collection_limits", {})
    configured_language = config.get("languages", {}).get(country, "en_US")
    payload: dict[str, Any] = {
        "limit": limits.get("apps_per_query", 200),
        "page": page,
        "sort": sort,
        "country": country,
        "language": normalize_appstorespy_language(configured_language),
        "fields": list(config.get("appstore_fields", DEFAULT_PLAY_APP_FIELDS)),
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
                    response = query_play_apps_with_field_fallback(api_client, query)
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


def query_play_apps_with_field_fallback(api_client: AppStoreSpyClient, query: dict[str, Any]) -> dict[str, Any]:
    try:
        return api_client.query_play_apps(query)
    except AppStoreSpyError as exc:
        unknown_fields = parse_unknown_fields(str(exc))
        fields = query.get("fields")
        if not unknown_fields or not isinstance(fields, list):
            raise
        filtered_fields = [field for field in fields if field not in unknown_fields]
        if len(filtered_fields) == len(fields):
            raise
        query["fields"] = filtered_fields
        query["removed_unknown_fields"] = unknown_fields
        return api_client.query_play_apps(query)


def parse_unknown_fields(error_text: str) -> list[str]:
    marker = "AppStoreSpy HTTP 400:"
    if marker not in error_text or "Unknown fields" not in error_text:
        return []
    detail = error_text.split(marker, 1)[1].strip()
    try:
        parsed = json.loads(detail)
    except json.JSONDecodeError:
        return []
    fields: list[str] = []
    for error in parsed.get("errors", []):
        if error.get("location") == "fields" and isinstance(error.get("value"), list):
            fields.extend(str(value) for value in error["value"])
    return sorted(set(fields))


def normalize_appstorespy_language(language: Any) -> str:
    value = str(language or "en_US")
    value = LANGUAGE_ALIASES.get(value, value)
    if value in APPSTORESPY_ALLOWED_LANGUAGES:
        return value
    if value.startswith("es_"):
        return "es_419"
    if value.startswith("pt_"):
        return "pt_BR"
    if value.startswith("tr_"):
        return "tr_TR"
    if value.startswith("vi"):
        return "vi"
    return "en_US"


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
