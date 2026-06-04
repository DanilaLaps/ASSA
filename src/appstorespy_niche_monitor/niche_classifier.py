from __future__ import annotations

from typing import Any

from .utils import normalize_text


DIMENSION_DEFAULTS = {
    "market_category": "other",
    "core_mechanic": "other",
    "theme": "other",
    "meta": "none",
    "audience": "unknown",
}


def classify_niche(app: dict[str, Any], config: dict[str, Any]) -> str:
    text = searchable_text(app)
    best_niche = "other"
    best_length = 0
    for niche, rule in config.get("niche_rules", {}).items():
        for keyword in rule.get("keywords", []):
            normalized = normalize_text(keyword)
            if normalized and normalized in text and len(normalized) > best_length:
                best_niche = niche
                best_length = len(normalized)
    return best_niche


def searchable_text(app: dict[str, Any]) -> str:
    return normalize_text(
        " ".join(
            str(app.get(field, ""))
            for field in ("name", "developer_name", "category", "description")
        )
    )


def infer_dimension(app: dict[str, Any], config: dict[str, Any], dimension: str, niche: str) -> str:
    text = normalize_text(f"{searchable_text(app)} {niche}")
    rules = config.get("dimension_rules", {}).get(dimension, {})
    best_value = DIMENSION_DEFAULTS.get(dimension, "other")
    best_length = 0
    for value, keywords in rules.items():
        for keyword in keywords:
            normalized = normalize_text(keyword)
            if normalized and normalized in text and len(normalized) > best_length:
                best_value = value
                best_length = len(normalized)

    if dimension == "market_category":
        category = normalize_text(app.get("category"))
        if "word" in category:
            best_value = "word"
        elif "board" in category:
            best_value = "board"
        elif "card" in category:
            best_value = "card"
        elif "simulation" in category:
            best_value = "simulation"
        elif "arcade" in category:
            best_value = "arcade"
        elif "casual" in category:
            best_value = "casual"
        elif "puzzle" in category or niche.endswith("puzzle"):
            best_value = "puzzle"
    return validate_dimension(config, dimension, best_value)


def infer_production_complexity(niche: str, config: dict[str, Any]) -> str:
    score = config.get("production_scores", {}).get(niche, config.get("production_scores", {}).get("other", 3))
    if score >= 12:
        return "low"
    if score >= 7:
        return "medium"
    return "high"


def validate_dimension(config: dict[str, Any], dimension: str, value: str) -> str:
    allowed = config.get("classification_dimensions", {}).get(dimension)
    if allowed and value not in allowed:
        return DIMENSION_DEFAULTS.get(dimension, allowed[0])
    return value


def classify_app(app: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    classified = dict(app)
    niche = classify_niche(app, config)
    classified["niche"] = niche
    for dimension in ("market_category", "core_mechanic", "theme", "meta", "audience"):
        classified[dimension] = infer_dimension(app, config, dimension, niche)
    classified["production_complexity"] = infer_production_complexity(niche, config)
    return classified


def classify_apps(apps: list[dict[str, Any]], config: dict[str, Any]) -> list[dict[str, Any]]:
    return [classify_app(app, config) for app in apps]
