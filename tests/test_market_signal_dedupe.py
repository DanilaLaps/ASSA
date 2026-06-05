import unittest

from appstorespy_niche_monitor.alert_filter import apply_cooldown_and_alert_limits, split_candidates
from appstorespy_niche_monitor.config import load_config
from appstorespy_niche_monitor.dedupe import dedupe_market_signals, top_app_overlap


def candidate(candidate_id: str, opportunity_score: float, group_key_type: str, **overrides):
    row = {
        "candidate_id": candidate_id,
        "status": "ALERT",
        "dedupe_key": candidate_id,
        "normalized_niche": "sort_puzzle",
        "market_category": "puzzle",
        "core_mechanic": "sort",
        "theme": "supermarket",
        "meta": "collection",
        "group_key_type": group_key_type,
        "production_complexity": "low",
        "full_product_complexity": "low",
        "mvp_complexity": "low",
        "mvp_feasibility_score": 85,
        "opportunity_score": opportunity_score,
        "total_daily_installs": 90000,
        "weekly_growth_percent": 40,
        "monthly_growth_percent": 80,
        "history_depth_days": 14,
        "app_count": 4,
        "successful_new_apps_count": 2,
        "unique_developer_count": 3,
        "giant_developer_share": 0.0,
        "single_developer_share": 0.4,
        "top_app_share": 0.42,
        "top3_app_share": 0.78,
        "growth_by_one_app_share": 0.3,
        "advertised_top_app_share": 0.1,
        "classification_confidence_avg": 0.82,
        "data_quality_score": 86,
        "risk_tags": [],
        "reason_codes": ["high_demand"],
        "top_apps": [
            {"app_id": "a", "developer_name": "A Studio", "downloads_daily": 40000},
            {"app_id": "b", "developer_name": "B Studio", "downloads_daily": 30000},
            {"app_id": "c", "developer_name": "C Studio", "downloads_daily": 20000},
        ],
    }
    row.update(overrides)
    return row


class MarketSignalDedupeTests(unittest.TestCase):
    def test_top_app_overlap_detects_duplicate_market_signal(self):
        left = candidate("left", 90, "normalized_niche")
        right = candidate(
            "right",
            88,
            "core_mechanic_theme_meta",
            top_apps=[
                {"app_id": "a", "developer_name": "A Studio", "downloads_daily": 40000},
                {"app_id": "b", "developer_name": "B Studio", "downloads_daily": 30000},
                {"app_id": "c", "developer_name": "C Studio", "downloads_daily": 20000},
            ],
        )

        self.assertGreaterEqual(top_app_overlap(left, right), 0.67)

    def test_duplicate_market_signal_cannot_take_second_sendable_slot(self):
        config, _ = load_config("config.yaml")
        config["alert_limits"]["max_alerts_per_run"] = 3
        stronger = candidate("stronger", 93, "normalized_niche")
        weaker_duplicate = candidate(
            "weaker",
            91,
            "core_mechanic_theme_meta",
            normalized_niche="sort_puzzle_variant",
            top_apps=[
                {"app_id": "a", "developer_name": "A Studio", "downloads_daily": 40000},
                {"app_id": "b", "developer_name": "B Studio", "downloads_daily": 30000},
                {"app_id": "c", "developer_name": "C Studio", "downloads_daily": 20000},
            ],
        )

        filtered = apply_cooldown_and_alert_limits(
            [stronger, weaker_duplicate],
            config,
            {},
            "2026-06-04",
        )
        urgent_alerts, *_ = split_candidates(filtered)
        duplicate = next(item for item in filtered if item["candidate_id"] == "weaker")

        self.assertEqual(len(urgent_alerts), 1)
        self.assertEqual(urgent_alerts[0]["candidate_id"], "stronger")
        self.assertEqual(duplicate["duplicate_of_candidate_id"], "stronger")
        self.assertIn("duplicate_market_signal", duplicate["sendable_alert_failures"])

    def test_dedupe_market_signals_marks_duplicate_candidate(self):
        config, _ = load_config("config.yaml")

        rows = dedupe_market_signals(
            [
                candidate("stronger", 93, "normalized_niche", sendable_alert_score=90),
                candidate("weaker", 91, "core_mechanic_theme_meta", sendable_alert_score=80),
            ],
            config,
        )

        duplicate = next(item for item in rows if item["candidate_id"] == "weaker")
        self.assertEqual(duplicate["duplicate_reason"], "market_signal_duplicate")


if __name__ == "__main__":
    unittest.main()
