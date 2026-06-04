from __future__ import annotations

from typing import Any

from .utils import safe_div


APP_LIST_KEYS = ("apps", "items", "data", "results")
TOTAL_COUNT_KEYS = ("total_count", "total", "count")


def extract_response_apps(response: Any) -> list[dict[str, Any]]:
    if isinstance(response, list):
        return [item for item in response if isinstance(item, dict)]
    if not isinstance(response, dict):
        return []
    for key in APP_LIST_KEYS:
        value = response.get(key)
        if isinstance(value, list):
            return [item for item in value if isinstance(item, dict)]
    if all(key in response for key in ("id", "name")):
        return [response]
    return []


def extract_total_count(response: Any) -> int | None:
    if not isinstance(response, dict):
        return None
    for key in TOTAL_COUNT_KEYS:
        value = response.get(key)
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
    for container_key in ("meta", "pagination"):
        container = response.get(container_key)
        if isinstance(container, dict):
            nested = extract_total_count(container)
            if nested is not None:
                return nested
    return None


def build_source_query_metadata(payload: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    collection = config.get("collection", {})
    filters = payload.get("filter", {})
    return {
        "limit": int(payload.get("limit", collection.get("limit", 10000))),
        "page": int(payload.get("page", collection.get("page", 1))),
        "sort": payload.get("sort", collection.get("sort", "-release_date")),
        "release_date_days_back": int(collection.get("release_date_days_back", 180)),
        "min_downloads_daily": int(
            filters.get("downloads_daily", {}).get("gte", collection.get("min_downloads_daily", 500))
        ),
        "requested_country": payload.get("country"),
        "requested_language": payload.get("language"),
        "requested_active_countries": payload.get("active_countries"),
    }


def build_coverage_metadata(
    response: Any,
    payload: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, Any]:
    limit = int(payload.get("limit", config.get("collection", {}).get("limit", 10000)))
    result_count = len(extract_response_apps(response))
    total_count = extract_total_count(response)
    if total_count is None:
        sample_truncated: bool | str = "unknown"
        coverage_ratio = None
        full_window_claim_allowed = False
    elif total_count <= limit:
        sample_truncated = False
        coverage_ratio = round(safe_div(result_count, total_count), 4) if total_count else 1.0
        full_window_claim_allowed = True
    else:
        sample_truncated = True
        coverage_ratio = round(safe_div(result_count, total_count), 4)
        full_window_claim_allowed = False
    return {
        "total_count": total_count,
        "result_count": result_count,
        "sample_truncated": sample_truncated,
        "coverage_ratio": coverage_ratio,
        "full_window_claim_allowed": full_window_claim_allowed,
    }


def coverage_risk_tags(coverage: dict[str, Any]) -> list[str]:
    if coverage.get("sample_truncated") is True:
        return ["sample_truncated"]
    if coverage.get("sample_truncated") == "unknown":
        return ["unknown_coverage"]
    return []
