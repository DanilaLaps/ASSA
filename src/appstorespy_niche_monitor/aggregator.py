from __future__ import annotations

from collections import defaultdict
from statistics import mean
from typing import Any

from .utils import age_days, safe_div


GROUP_FIELDS = (
    "platform",
    "niche",
    "market_category",
    "core_mechanic",
    "theme",
    "meta",
    "audience",
    "production_complexity",
)


def stable_key(item: dict[str, Any]) -> str:
    return "::".join(str(item.get(field, "")) for field in GROUP_FIELDS)


def signal_signature(item: dict[str, Any]) -> str:
    fields = ("niche", "market_category", "core_mechanic", "theme", "meta", "audience")
    return "::".join(str(item.get(field, "")) for field in fields)


def aggregate_apps(apps: list[dict[str, Any]], config: dict[str, Any], snapshot_date: str) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for app in apps:
        grouped[stable_key(app)].append(app)

    summaries = [
        aggregate_group(group_apps, config, snapshot_date)
        for group_apps in grouped.values()
        if group_apps
    ]
    return sorted(summaries, key=lambda row: (-row["total_daily_installs"], row["niche"], row["group_key"]))


def aggregate_group(apps: list[dict[str, Any]], config: dict[str, Any], snapshot_date: str) -> dict[str, Any]:
    first = apps[0]
    thresholds = config.get("thresholds", {})
    new_app_days = int(thresholds.get("new_app_days", 180))
    recently_updated_days = int(thresholds.get("recently_updated_days", 90))
    successful_new_install_threshold = int(thresholds.get("successful_new_app_daily_installs", 10000))
    total_daily = sum(int(app.get("downloads_daily", 0)) for app in apps)
    total_monthly = sum(int(app.get("downloads_month", 0)) for app in apps)
    total_revenue = sum(float(app.get("revenue_month", 0.0)) for app in apps)
    ratings = [float(app.get("rating_avg", 0.0)) for app in apps if float(app.get("rating_avg", 0.0)) > 0]
    top_apps = sorted(apps, key=lambda app: int(app.get("downloads_daily", 0)), reverse=True)[:5]
    giant_share = calculate_giant_developer_share(apps, config)
    collection = config.get("collection", {})
    release_date_window = f"last_{int(collection.get('release_date_days_back', 180))}d"

    new_apps_count = 0
    recently_updated_count = 0
    successful_new_apps_count = 0
    for app in apps:
        release_age = age_days(app.get("release_date"), snapshot_date)
        update_age = age_days(app.get("update_date"), snapshot_date)
        if release_age is not None and 0 <= release_age <= new_app_days:
            new_apps_count += 1
            if int(app.get("downloads_daily", 0)) >= successful_new_install_threshold:
                successful_new_apps_count += 1
        if update_age is not None and 0 <= update_age <= recently_updated_days:
            recently_updated_count += 1

    summary = {
        "snapshot_date": snapshot_date,
        **{field: first.get(field, "") for field in GROUP_FIELDS},
        "group_key": stable_key(first),
        "signal_signature": signal_signature(first),
        "release_date_window": release_date_window,
        "source_scope": "single_appstorespy_query_no_country_language",
        "collection_sort": collection.get("sort", "-release_date"),
        "min_app_daily_installs": int(collection.get("min_downloads_daily", 500)),
        "app_count": len(apps),
        "total_daily_installs": total_daily,
        "avg_daily_installs": round(safe_div(total_daily, len(apps)), 2),
        "total_monthly_downloads": total_monthly,
        "total_monthly_revenue": round(total_revenue, 2),
        "avg_rating": round(mean(ratings), 2) if ratings else 0.0,
        "new_apps_count": new_apps_count,
        "recently_updated_count": recently_updated_count,
        "successful_new_apps_count": successful_new_apps_count,
        "top_app_share": round(safe_div(int(top_apps[0].get("downloads_daily", 0)) if top_apps else 0, total_daily), 4),
        "growth_by_one_app_share": 0.0,
        "advertised_top_app_share": round(advertised_top_app_share(top_apps, total_daily), 4),
        "giant_developer_share": round(giant_share, 4),
        "top_apps": [compact_app(app) for app in top_apps],
    }
    return summary


def compact_app(app: dict[str, Any]) -> dict[str, Any]:
    return {
        "app_id": app.get("app_id", ""),
        "bundle": app.get("bundle", ""),
        "name": app.get("name", ""),
        "developer_name": app.get("developer_name", ""),
        "developer_id": app.get("developer_id", ""),
        "downloads_daily": int(app.get("downloads_daily", 0)),
        "downloads_month": int(app.get("downloads_month", 0)),
        "revenue_month": float(app.get("revenue_month", 0.0)),
        "release_date": app.get("release_date", ""),
        "update_date": app.get("update_date", ""),
        "advertised": bool(app.get("advertised", False)),
        "ads": bool(app.get("ads", False)),
        "url_appstorespy": app.get("url_appstorespy", ""),
        "url": app.get("url", ""),
        "website": app.get("website", ""),
    }


def calculate_giant_developer_share(apps: list[dict[str, Any]], config: dict[str, Any]) -> float:
    giants = [name.lower() for name in config.get("giant_developers", [])]
    total_daily = sum(int(app.get("downloads_daily", 0)) for app in apps)
    if total_daily <= 0:
        return 0.0
    giant_daily = 0
    for app in apps:
        developer = str(app.get("developer_name", "")).lower()
        if any(giant in developer for giant in giants):
            giant_daily += int(app.get("downloads_daily", 0))
    return safe_div(giant_daily, total_daily)


def advertised_top_app_share(top_apps: list[dict[str, Any]], total_daily: int) -> float:
    if total_daily <= 0:
        return 0.0
    advertised_daily = sum(
        int(app.get("downloads_daily", 0))
        for app in top_apps
        if bool(app.get("advertised", False))
    )
    return safe_div(advertised_daily, total_daily)
