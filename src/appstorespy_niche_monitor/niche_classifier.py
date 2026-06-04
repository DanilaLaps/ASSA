from __future__ import annotations

from typing import Any

from .utils import clamp, normalize_text, slugify


DIMENSION_DEFAULTS = {
    "market_category": "other",
    "core_mechanic": "other",
    "theme": "other",
    "meta": "none",
    "audience": "unknown",
}


def classify_niche(app: dict[str, Any], config: dict[str, Any]) -> str:
    return match_niche(app, config)[0]


def match_niche(app: dict[str, Any], config: dict[str, Any]) -> tuple[str, float, list[str], str | None]:
    text = searchable_text(app)
    best_niche = "other"
    best_length = 0
    best_keyword: str | None = None
    for niche, rule in config.get("niche_rules", {}).items():
        for keyword in rule.get("keywords", []):
            normalized = normalize_text(keyword)
            if normalized and normalized in text and len(normalized) > best_length:
                best_niche = niche
                best_length = len(normalized)
                best_keyword = keyword
    aliases = niche_aliases(best_niche, config)
    confidence = confidence_from_match(best_length)
    return best_niche, confidence, aliases, best_keyword


def searchable_text(app: dict[str, Any]) -> str:
    return normalize_text(
        " ".join(
            str(app.get(field, ""))
            for field in ("name", "developer_name", "category", "description", "description_short", "description_full")
        )
    )


def infer_dimension(app: dict[str, Any], config: dict[str, Any], dimension: str, niche: str) -> str:
    return infer_dimension_with_confidence(app, config, dimension, niche)[0]


def infer_dimension_with_confidence(
    app: dict[str, Any],
    config: dict[str, Any],
    dimension: str,
    niche: str,
) -> tuple[str, float]:
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
            best_length = max(best_length, len("puzzle"))
    return validate_dimension(config, dimension, best_value), confidence_from_match(best_length)


def infer_production_complexity(niche: str, config: dict[str, Any]) -> str:
    score = config.get("production_scores", {}).get(niche, config.get("production_scores", {}).get("other", 3))
    if score >= 12:
        return "low"
    if score >= 7:
        return "medium"
    return "high"


def niche_aliases(niche: str, config: dict[str, Any]) -> list[str]:
    aliases: list[str] = []
    for alias_config in config.get("classification", {}).get("aliases", {}).values():
        if alias_config.get("niche") == niche:
            aliases.extend(str(item) for item in alias_config.get("aliases", []))
    aliases.extend(str(item) for item in config.get("niche_rules", {}).get(niche, {}).get("keywords", []))
    return sorted(set(item for item in aliases if item))


def confidence_from_match(match_length: int) -> float:
    if match_length <= 0:
        return 0.35
    return round(clamp(0.45 + match_length / 30.0, 0.0, 0.95), 2)


def infer_mvp_fields(
    niche: str,
    dimensions: dict[str, str],
    production_complexity: str,
) -> dict[str, Any]:
    core = dimensions.get("core_mechanic", "other")
    theme = dimensions.get("theme", "other")
    simplifiable_mechanics = {"sort", "merge", "match", "search", "decorate", "collect", "idle", "trivia"}
    if production_complexity == "low":
        mvp_complexity = "low"
        feasibility = 85
        simplifiable = True
    elif production_complexity == "medium":
        mvp_complexity = "medium"
        feasibility = 65
        simplifiable = True
    elif core in simplifiable_mechanics:
        mvp_complexity = "medium"
        feasibility = 58
        simplifiable = True
    else:
        mvp_complexity = "high"
        feasibility = 35
        simplifiable = False
    idea = None
    if simplifiable:
        idea = f"Focus the MVP on {core} gameplay with a narrow {theme} theme and one progression loop."
    return {
        "full_product_complexity": production_complexity,
        "mvp_complexity": mvp_complexity,
        "mvp_feasibility_score": feasibility,
        "simplifiable": simplifiable,
        "simplification_idea": idea,
    }


def is_unknown_or_new_pattern(
    niche: str,
    dimensions: dict[str, str],
    confidences: dict[str, float],
    config: dict[str, Any],
) -> bool:
    min_confidence = float(config.get("classification", {}).get("min_confidence_for_hard_label", 0.7))
    mechanic = dimensions.get("core_mechanic", "other")
    theme = dimensions.get("theme", "other")
    meta = dimensions.get("meta", "none")
    unknown_combo = mechanic == "other" or theme == "other" or niche == "other"
    low_confidence = min(confidences.values() or [1.0]) < min_confidence
    new_combo = (mechanic, theme, meta) not in {
        ("sort", "supermarket", "collection"),
        ("sort", "abstract", "levels"),
        ("match", "abstract", "levels"),
        ("merge", "home", "renovation"),
        ("search", "home", "levels"),
        ("idle", "food", "levels"),
    }
    return bool(config.get("classification", {}).get("unknown_pattern_enabled", True)) and (
        unknown_combo or low_confidence or new_combo
    )


def validate_dimension(config: dict[str, Any], dimension: str, value: str) -> str:
    allowed = config.get("classification_dimensions", {}).get(dimension)
    if allowed and value not in allowed:
        return DIMENSION_DEFAULTS.get(dimension, allowed[0])
    return value


def classify_app(app: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    classified = dict(app)
    niche, niche_confidence, aliases, matched_keyword = match_niche(app, config)
    classified["niche"] = niche
    classified["normalized_niche"] = slugify(niche)
    classified["niche_aliases"] = aliases
    dimensions: dict[str, str] = {}
    confidences: dict[str, float] = {"niche_confidence": niche_confidence}
    for dimension in ("market_category", "core_mechanic", "theme", "meta", "audience"):
        value, confidence = infer_dimension_with_confidence(app, config, dimension, niche)
        classified[dimension] = value
        dimensions[dimension] = value
        confidences[f"{dimension}_confidence"] = confidence
    production_complexity = infer_production_complexity(niche, config)
    classified["production_complexity"] = production_complexity
    classified.update(infer_mvp_fields(niche, dimensions, production_complexity))
    classified["niche_confidence"] = niche_confidence
    classified["mechanic_confidence"] = confidences.get("core_mechanic_confidence", 0.35)
    classified["theme_confidence"] = confidences.get("theme_confidence", 0.35)
    classified["audience_confidence"] = confidences.get("audience_confidence", 0.35)
    classified["complexity_confidence"] = 0.8 if production_complexity != "high" else 0.6
    classified["is_unknown_or_new_pattern"] = is_unknown_or_new_pattern(niche, dimensions, confidences, config)
    classified["classification_reason"] = (
        f"matched keyword '{matched_keyword}'" if matched_keyword else "no strong rule-based niche match"
    )
    return classified


def classify_apps(apps: list[dict[str, Any]], config: dict[str, Any]) -> list[dict[str, Any]]:
    return [classify_app(app, config) for app in apps]
