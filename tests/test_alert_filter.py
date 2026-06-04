import unittest

from appstorespy_niche_monitor.alert_filter import filter_alerts, should_alert
from appstorespy_niche_monitor.config import load_config


def candidate(**overrides):
    row = {
        "snapshot_date": "2026-06-04",
        "platform": "google_play",
        "country": "BR",
        "niche": "sort puzzle",
        "market_category": "puzzle",
        "core_mechanic": "sort",
        "theme": "supermarket",
        "meta": "collection",
        "audience": "women_25_45",
        "production_complexity": "low",
        "group_key": "google_play::BR::sort puzzle::puzzle::sort::supermarket::collection::women_25_45::low",
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
        "reason_codes": ["high_demand", "strong_growth"],
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

    def test_max_alerts_and_country_limit_are_applied(self):
        config, _ = load_config("config.yaml")
        rows = [
            candidate(country="BR", group_key="a", opportunity_score=90),
            candidate(country="BR", group_key="b", opportunity_score=89),
            candidate(country="US", group_key="c", opportunity_score=88),
            candidate(country="MX", group_key="d", opportunity_score=87),
            candidate(country="IN", group_key="e", opportunity_score=86),
        ]

        alerts, _, _ = filter_alerts(rows, config, {}, "2026-06-04")

        self.assertEqual(len(alerts), 3)
        self.assertEqual(len([row for row in alerts if row["country"] == "BR"]), 1)


if __name__ == "__main__":
    unittest.main()
