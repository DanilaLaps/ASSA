from __future__ import annotations

import datetime as dt
import math
import re
import unicodedata
from typing import Any


DATE_FORMAT = "%Y-%m-%d"


def utc_today() -> str:
    return dt.datetime.now(dt.UTC).date().isoformat()


def parse_date(value: Any) -> dt.date | None:
    if value in (None, ""):
        return None
    if isinstance(value, dt.date) and not isinstance(value, dt.datetime):
        return value
    if isinstance(value, dt.datetime):
        return value.date()
    text = str(value).strip()
    if not text:
        return None
    for pattern in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%SZ"):
        try:
            return dt.datetime.strptime(text[: len(pattern)], pattern).date()
        except ValueError:
            continue
    try:
        return dt.datetime.fromisoformat(text.replace("Z", "+00:00")).date()
    except ValueError:
        return None


def date_distance_days(left: str | dt.date, right: str | dt.date) -> int | None:
    left_date = parse_date(left)
    right_date = parse_date(right)
    if left_date is None or right_date is None:
        return None
    return abs((left_date - right_date).days)


def age_days(value: Any, today: str | dt.date) -> int | None:
    parsed = parse_date(value)
    today_date = parse_date(today)
    if parsed is None or today_date is None:
        return None
    return (today_date - parsed).days


def to_int(value: Any, default: int = 0) -> int:
    if value in (None, ""):
        return default
    try:
        return int(float(str(value).replace(",", "")))
    except (TypeError, ValueError):
        return default


def to_float(value: Any, default: float = 0.0) -> float:
    if value in (None, ""):
        return default
    try:
        return float(str(value).replace(",", ""))
    except (TypeError, ValueError):
        return default


def safe_div(numerator: float, denominator: float, default: float = 0.0) -> float:
    if denominator == 0:
        return default
    return numerator / denominator


def clamp(value: float, minimum: float = 0.0, maximum: float = 100.0) -> float:
    return max(minimum, min(maximum, value))


def log_score(value: float, multiplier: float, maximum: float) -> float:
    return min(math.log10(max(value, 0.0) + 1.0) * multiplier, maximum)


def normalize_text(value: Any) -> str:
    text = "" if value is None else str(value)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", text.lower()).strip()


def slugify(value: Any, max_length: int = 80) -> str:
    text = normalize_text(value)
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return (text or "item")[:max_length].strip("_")


def first_present(mapping: dict[str, Any], keys: list[str], default: Any = None) -> Any:
    for key in keys:
        if key in mapping and mapping[key] not in (None, ""):
            return mapping[key]
    return default


def percent_change(current: float, previous: float) -> float:
    if previous <= 0 and current > 0:
        return 100.0
    if previous <= 0:
        return 0.0
    return ((current - previous) / previous) * 100.0
