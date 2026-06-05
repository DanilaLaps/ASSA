from __future__ import annotations

from collections import Counter, defaultdict
from statistics import mean, median
from typing import Any

from .utils import age_days, safe_div


GROUP_FIELDS = (
    "platform",
    "normalized_niche",
    "market_category",
    "core_mechanic",
    "theme",
    "meta",
    "production_complexity",
)

GROUP_DEFINITIONS: dict[str, tuple[str, ...]] = {
    "normalized_niche": ("normalized_niche",),
    "core_mechanic": ("core_mechanic",),
    "core_mechanic_theme": ("core_mechanic", "theme"),
    "core_mechanic_theme_meta": ("core_mechanic", "theme", "meta"),
    "market_category_core_mechanic": ("market_category", "core_mechanic"),
}


def stable_key(item: dict[str, Any]) -> str:
    normalized = item.get("normalized_niche") or item.get("niche") or ""
    values = []
    for field in GROUP_FIELDS:
        if field == "normalized_niche":
            values.append(str(normalized))
        else:
            values.append(str(item.get(field, "")))
    return "::".join(values)


def signal_signature(item: dict[str, Any]) -> str:
    fields = ("normalized_niche", "market_category", "core_mechanic", "theme", "meta")
    return "::".join(str(item.get(field) or item.get("niche") or "") for field in fields)


def aggregate_apps(apps: list[dict[str, Any]], config: dict[str, Any], snapshot_date: str) -> list[dict[str, Any]]:
    aggregation_cfg = config.get("aggregation", {})
    group_keys = aggregation_cfg.get("group_keys") or list(GROUP_DEFINITIONS)
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for app in apps:
        for group_key_type in group_keys:
            fields = GROUP_DEFINITIONS.get(str(group_key_type))
            if not fields:
                continue
            value = group_key_value(app, fields)
            if value:
                grouped[(str(group_key_type), value)].append(app)

    summaries = [
        aggregate_group(group_apps, config, snapshot_date, group_key_type, group_key_value_text)
        for (group_key_type, group_key_value_text), group_apps in grouped.items()
        if group_apps
    ]
    return sorted(
        summaries,
        key=lambda row: (-row["total_daily_installs"], row["group_key_type"], row["group_key_value"]),
    )


def group_key_value(app: dict[str, Any], fields: tuple[str, ...]) -> str:
    values = []
    for field in fields:
        value = app.get(field)
        if field == "normalized_niche" and not value:
            value = app.get("niche")
        values.append(str(value or "other"))
    return "::".join(values)


def aggregate_group(
    apps: list[dict[str, Any]],
    config: dict[str, Any],
    snapshot_date: str,
    group_key_type: str,
    group_key_value_text: str,
) -> dict[str, Any]:
    thresholds = config.get("thresholds", {})
    collection = config.get("collection", {})
    new_app_days = int(thresholds.get("new_app_days", 180))
    traction_days = 60
    successful_new_install_threshold = int(thresholds.get("successful_new_app_daily_installs", 500))
    release_date_window = f"last_{int(collection.get('release_date_days_back', 180))}d"

    total_daily = sum(int(app.get("downloads_daily", 0)) for app in apps)
    daily_values = [int(app.get("downloads_daily", 0)) for app in apps]
    total_monthly = sum(int(app.get("downloads_month", 0)) for app in apps)
    total_revenue = sum(float(app.get("revenue_month", 0.0)) for app in apps)
    ratings = [float(app.get("rating_avg", 0.0)) for app in apps if float(app.get("rating_avg", 0.0)) > 0]
    rating_counts = [int(app.get("rating_count", 0)) for app in apps if int(app.get("rating_count", 0)) > 0]
    top_apps = sorted(apps, key=lambda app: int(app.get("downloads_daily", 0)), reverse=True)[:5]
    developer_ids = {
        str(app.get("developer_id") or app.get("developer_name"))
        for app in apps
        if app.get("developer_id") or app.get("developer_name")
    }
    unique_developer_count = len(developer_ids)
    top3_daily = sum(int(app.get("downloads_daily", 0)) for app in top_apps[:3])

    successful_new_apps_count = 0
    traction_fresh_apps_count = 0
    for app in apps:
        release_age = age_days(app.get("release_date"), snapshot_date)
        daily = int(app.get("downloads_daily", 0))
        if release_age is not None and 0 <= release_age <= new_app_days and daily >= successful_new_install_threshold:
            successful_new_apps_count += 1
        if release_age is not None and 0 <= release_age <= traction_days and daily >= 1000:
            traction_fresh_apps_count += 1

    dominant = dominant_app(apps)
    coverage = dominant.get("coverage", {}) if dominant else {}
    source_query = dominant.get("source_query", {}) if dominant else {}
    dimensions = dominant_dimensions(apps)
    classification_confidences = [
        mean(
            [
                float(app.get("niche_confidence", 0.0)),
                float(app.get("mechanic_confidence", 0.0)),
                float(app.get("theme_confidence", 0.0)),
                float(app.get("audience_confidence", 0.0)),
                float(app.get("complexity_confidence", 0.0)),
            ]
        )
        for app in apps
    ]
    mvp_scores = [float(app.get("mvp_feasibility_score", 50.0)) for app in apps]
    summary = {
        "snapshot_date": snapshot_date,
        "score_version": config.get("app", {}).get("score_version", "v1.3.2"),
        "platform": dimensions.get("platform", "google_play"),
        "niche": dimensions.get("niche", group_key_value_text),
        "normalized_niche": dimensions.get("normalized_niche", group_key_value_text.replace("::", "_")),
        "market_category": dimensions.get("market_category", "other"),
        "core_mechanic": dimensions.get("core_mechanic", "other"),
        "theme": dimensions.get("theme", "other"),
        "meta": dimensions.get("meta", "none"),
        "audience": dimensions.get("audience", "unknown"),
        "audience_summary": audience_summary(apps),
        "production_complexity": dimensions.get("production_complexity", "unknown"),
        "full_product_complexity": dimensions.get("full_product_complexity", dimensions.get("production_complexity", "unknown")),
        "mvp_complexity": dimensions.get("mvp_complexity", "unknown"),
        "mvp_feasibility_score": round(mean(mvp_scores), 2) if mvp_scores else 50.0,
        "simplifiable": any(bool(app.get("simplifiable")) for app in apps),
        "simplification_idea": first_non_empty(apps, "simplification_idea"),
        "group_key_type": group_key_type,
        "group_key_value": group_key_value_text,
        "group_key": f"{group_key_type}::{group_key_value_text}",
        "signal_signature": signal_signature(dimensions),
        "release_date_window": release_date_window,
        "source_scope": "single_appstorespy_query_no_country_language",
        "collection_sort": collection.get("sort", "-release_date"),
        "min_app_daily_installs": int(collection.get("min_downloads_daily", 500)),
        "source_query": source_query,
        "coverage": coverage,
        "app_count": len(apps),
        "app_ids": sorted(str(app.get("app_id") or app.get("bundle") or app.get("name", "")) for app in apps),
        "total_daily_installs": total_daily,
        "avg_daily_installs": round(safe_div(total_daily, len(apps)), 2),
        "median_daily_installs": round(float(median(daily_values)), 2) if daily_values else 0.0,
        "total_monthly_downloads": total_monthly,
        "total_monthly_revenue": round(total_revenue, 2),
        "avg_rating": round(mean(ratings), 2) if ratings else 0.0,
        "rating_count_total": sum(rating_counts),
        "rating_confidence": rating_confidence(sum(rating_counts)),
        "successful_new_apps_count": successful_new_apps_count,
        "traction_fresh_apps_count": traction_fresh_apps_count,
        "top_app_share": round(safe_div(int(top_apps[0].get("downloads_daily", 0)) if top_apps else 0, total_daily), 4),
        "top3_app_share": round(safe_div(top3_daily, total_daily), 4),
        "growth_by_one_app_share": 0.0,
        "advertised_top_app_share": round(advertised_top_app_share(top_apps, total_daily), 4),
        "giant_developer_share": round(calculate_giant_developer_share(apps, config), 4),
        "single_developer_share": round(single_developer_share(apps, total_daily), 4),
        "unique_developer_count": unique_developer_count,
        "developer_diversity_score": round(min(safe_div(unique_developer_count, len(apps)), 1.0), 4),
        "fresh_success_ratio": round(safe_div(successful_new_apps_count, len(apps)), 4),
        "cluster_diversity_score": round(
            (
                min(safe_div(unique_developer_count, len(apps)), 1.0)
                + max(1.0 - safe_div(int(top_apps[0].get("downloads_daily", 0)) if top_apps else 0, total_daily), 0.0)
            )
            / 2.0,
            4,
        ),
        "classification_confidence_avg": round(mean(classification_confidences), 4) if classification_confidences else 0.0,
        "unknown_or_new_pattern_cluster": any(bool(app.get("is_unknown_or_new_pattern")) for app in apps),
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
        "category": app.get("category", ""),
        "category_type": app.get("category_type", ""),
        "downloads_daily": int(app.get("downloads_daily", 0)),
        "downloads_month": int(app.get("downloads_month", 0)),
        "downloads_exact": int(app.get("downloads_exact", 0)),
        "downloads_mark": app.get("downloads_mark", ""),
        "revenue_month": float(app.get("revenue_month", 0.0)),
        "rating_avg": float(app.get("rating_avg", 0.0)),
        "rating_count": int(app.get("rating_count", 0)),
        "review_count": int(app.get("review_count", 0)),
        "release_date": app.get("release_date", ""),
        "update_date": app.get("update_date", ""),
        "iap": app.get("iap"),
        "advertised": bool(app.get("advertised", False)),
        "ads": app.get("ads"),
        "icon": app.get("icon", ""),
        "screenshots": list(app.get("screenshots", [])[:3]) if isinstance(app.get("screenshots"), list) else [],
        "description_short": truncate_text(app.get("description_short", ""), 500),
        "description_excerpt": truncate_text(app.get("description_full") or app.get("description", ""), 1200),
        "url_appstorespy": app.get("url_appstorespy", ""),
        "url": app.get("url", ""),
        "website": app.get("website", ""),
    }


def truncate_text(value: Any, max_chars: int) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 3].rstrip() + "..."


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


def single_developer_share(apps: list[dict[str, Any]], total_daily: int) -> float:
    if total_daily <= 0:
        return 0.0
    daily_by_developer: Counter[str] = Counter()
    for app in apps:
        developer = str(app.get("developer_id") or app.get("developer_name") or "unknown")
        daily_by_developer[developer] += int(app.get("downloads_daily", 0))
    return safe_div(max(daily_by_developer.values() or [0]), total_daily)


def rating_confidence(rating_count: int | None) -> float:
    if not rating_count:
        return 0.0
    import math

    return round(min(math.log10(rating_count + 1) / 4, 1.0), 4)


def dominant_app(apps: list[dict[str, Any]]) -> dict[str, Any]:
    return max(apps, key=lambda app: int(app.get("downloads_daily", 0))) if apps else {}


def dominant_dimensions(apps: list[dict[str, Any]]) -> dict[str, str]:
    fields = (
        "platform",
        "niche",
        "normalized_niche",
        "market_category",
        "core_mechanic",
        "theme",
        "meta",
        "audience",
        "production_complexity",
        "full_product_complexity",
        "mvp_complexity",
    )
    result: dict[str, str] = {}
    for field in fields:
        weights: Counter[str] = Counter()
        for app in apps:
            value = str(app.get(field) or "")
            if value:
                weights[value] += int(app.get("downloads_daily", 0))
        result[field] = weights.most_common(1)[0][0] if weights else ""
    return result


def audience_summary(apps: list[dict[str, Any]]) -> str:
    counts: Counter[str] = Counter(str(app.get("audience") or "unknown") for app in apps)
    return ", ".join(f"{value}:{count}" for value, count in counts.most_common(3))


def first_non_empty(apps: list[dict[str, Any]], field: str) -> Any:
    for app in apps:
        if app.get(field):
            return app[field]
    return None
