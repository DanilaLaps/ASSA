from __future__ import annotations

from typing import Any, Iterable

from .utils import first_present, parse_date, to_float, to_int


APP_LIST_KEYS = ("apps", "items", "data", "results")


def iter_response_apps(response: Any) -> Iterable[dict[str, Any]]:
    if isinstance(response, list):
        for item in response:
            if isinstance(item, dict):
                yield item
        return
    if not isinstance(response, dict):
        return
    for key in APP_LIST_KEYS:
        value = response.get(key)
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    yield item
            return
    if all(key in response for key in ("id", "name")):
        yield response


def normalize_app(raw: dict[str, Any], meta: dict[str, Any], snapshot_date: str) -> dict[str, Any]:
    release_date = parse_date(first_present(raw, ["release_date", "released_at", "created_at"]))
    update_date = parse_date(first_present(raw, ["update_date", "updated_at", "last_update_date"]))
    app_id = str(first_present(raw, ["id", "app_id", "package_name", "package"], "unknown"))
    country = str(first_present(raw, ["country"], meta.get("country", "")))
    platform = str(first_present(raw, ["platform"], meta.get("platform", "google_play")))
    return {
        "snapshot_date": snapshot_date,
        "platform": platform,
        "country": country,
        "app_id": app_id,
        "name": str(first_present(raw, ["name", "title"], "")),
        "developer_name": str(first_present(raw, ["developer_name", "developer", "publisher"], "")),
        "category": str(first_present(raw, ["category", "category_id"], meta.get("category", ""))),
        "category_type": str(first_present(raw, ["category_type"], "GAME")),
        "description": str(first_present(raw, ["description", "short_description"], "")),
        "downloads_daily": to_int(first_present(raw, ["downloads_daily", "daily_downloads", "installs_daily"])),
        "downloads_month": to_int(first_present(raw, ["downloads_month", "monthly_downloads", "installs_month"])),
        "revenue_month": to_float(first_present(raw, ["revenue_month", "monthly_revenue", "revenue"])),
        "rating_avg": to_float(first_present(raw, ["rating_avg", "rating", "score"])),
        "rating_count": to_int(first_present(raw, ["rating_count", "ratings", "ratings_count"])),
        "review_count": to_int(first_present(raw, ["review_count", "reviews", "reviews_count"])),
        "release_date": release_date.isoformat() if release_date else "",
        "update_date": update_date.isoformat() if update_date else "",
        "iap": bool(first_present(raw, ["iap", "has_iap"], False)),
        "advertised": bool(first_present(raw, ["advertised", "ads", "has_ads"], False)),
        "icon": str(first_present(raw, ["icon", "icon_url"], "")),
        "screenshots": first_present(raw, ["screenshots", "screenshot_urls"], []),
        "url_appstorespy": str(first_present(raw, ["url_appstorespy", "url", "app_url"], "")),
    }


def clean_apps(raw_records: list[dict[str, Any]], snapshot_date: str) -> list[dict[str, Any]]:
    deduped: dict[tuple[str, str, str], dict[str, Any]] = {}
    for record in raw_records:
        meta = {
            "platform": record.get("platform", "google_play"),
            "country": record.get("country", ""),
            "category": record.get("category", ""),
        }
        for raw_app in iter_response_apps(record.get("response")):
            app = normalize_app(raw_app, meta, snapshot_date)
            key = (app["platform"], app["country"], app["app_id"])
            previous = deduped.get(key)
            if previous is None or app["downloads_daily"] >= previous["downloads_daily"]:
                deduped[key] = app
    return sorted(deduped.values(), key=lambda item: (item["country"], -item["downloads_daily"], item["name"]))
