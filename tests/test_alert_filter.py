import unittest

from appstorespy_niche_monitor.alert_filter import alert_key, build_alert_id, filter_alerts, should_alert
from appstorespy_niche_monitor.config import load_config


def candidate(**overrides):
    row = {
        "snapshot_date": "2026-06-04",
        "platform": "google_play",
        "niche": "sort puzzle",
        "market_category": "puzzle",
        "core_mechanic": "sort",
        "theme": "supermarket",
        "meta": "collection",
        "audience": "women_25_45",
        "production_complexity": "low",
        "group_key": "google_play::sort puzzle::puzzle::sort::supermarket::collection::women_25_45::low",
        "release_date_window": "last_180d",
        "has_history": True,
        "opportunity_score": 88,
        "total_daily_installs": 90000,
        "weekly_growth_percent": 40,
        "app_count": 3,
        "successful_new_apps_count": 1,
        "giant_developer_share": 0.0,
        "top_app_share": 0.45,
        "growth_by_one_app_share": 0.4,
        "data_quality_score": 82,
        "reason_codes": ["high_demand", "historical_growth"],
        "top_apps": [
            {"app_id": "b", "name": "B"},
            {"app_id": "a", "name": "A"},
            {"app_id": "c", "name": "C"},
        ],
    }
    row.update(overrides)
    return row


class AlertFilterTests(unittest.TestCase):
    def test_candidate_passes_alert_rules(self):
        config, _ = load_config("config.yaml")

        passed, reasons = should_alert(candidate(), config, {}, "2026-06-04")

        self.assertTrue(passed)
        self.assertEqual(reasons, ["passed"])

    def test_top_app_dominance_blocks_alert(self):
        config, _ = load_config("config.yaml")

        passed, reasons = should_alert(candidate(top_app_share=0.9), config, {}, "2026-06-04")

        self.assertFalse(passed)
        self.assertIn("top_app_dominance", reasons)

    def test_max_alerts_are_applied_without_country_limit(self):
        config, _ = load_config("config.yaml")
        rows = [
            candidate(group_key="a", opportunity_score=90),
            candidate(group_key="b", opportunity_score=89),
            candidate(group_key="c", opportunity_score=88),
            candidate(group_key="d", opportunity_score=87),
            candidate(group_key="e", opportunity_score=86),
        ]

        alerts, _, _ = filter_alerts(rows, config, {}, "2026-06-04")

        self.assertEqual(len(alerts), 3)

    def test_alert_key_and_id_do_not_include_country(self):
        row = candidate()

        key = alert_key(row)
        alert_id = build_alert_id(row, "2026-06-04")

        self.assertIn("sort_puzzle_sort_supermarket_collection_women_25_45", key)
        self.assertIn("last_180d", key)
        self.assertEqual(key.split(":")[1], "a,b,c")
        self.assertTrue(alert_id.startswith("2026-06-04:sort_puzzle_sort_supermarket_collection_women_25_45:"))
        self.assertTrue(alert_id.endswith(":last_180d"))
        self.assertNotIn("BR", alert_id)

    def test_high_production_complexity_blocks_alert(self):
        config, _ = load_config("config.yaml")

        passed, reasons = should_alert(candidate(production_complexity="high"), config, {}, "2026-06-04")

        self.assertFalse(passed)
        self.assertIn("high_production_complexity", reasons)


if __name__ == "__main__":
    unittest.main()
