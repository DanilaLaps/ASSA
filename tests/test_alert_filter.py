import unittest

from appstorespy_niche_monitor.alert_filter import alert_key, build_alert_id, filter_alerts, should_alert
from appstorespy_niche_monitor.config import load_config


def candidate(**overrides):
    row = {
        "snapshot_date": "2026-06-04",
        "platform": "google_play",
        "niche": "sort puzzle",
        "normalized_niche": "sort_puzzle",
        "market_category": "puzzle",
        "core_mechanic": "sort",
        "theme": "supermarket",
        "meta": "collection",
        "audience": "women_25_45",
        "production_complexity": "low",
        "full_product_complexity": "low",
        "mvp_complexity": "low",
        "mvp_feasibility_score": 85,
        "group_key": "google_play::sort puzzle::puzzle::sort::supermarket::collection::women_25_45::low",
        "release_date_window": "last_180d",
        "has_history": True,
        "opportunity_score": 92,
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
        "reason_codes": ["high_demand", "historical_growth"],
        "top_apps": [
            {"app_id": "b", "name": "B", "developer_name": "B Studio", "downloads_daily": 30000},
            {"app_id": "a", "name": "A", "developer_name": "A Studio", "downloads_daily": 40000},
            {"app_id": "c", "name": "C", "developer_name": "C Studio", "downloads_daily": 20000},
            {"app_id": "d", "name": "D", "developer_name": "D Studio", "downloads_daily": 5000},
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

    def test_top_app_dominance_blocks_sendable_alert(self):
        config, _ = load_config("config.yaml")

        passed, reasons = should_alert(candidate(top_app_share=0.9), config, {}, "2026-06-04")

        self.assertFalse(passed)
        self.assertIn("top_app_too_dominant", reasons)

    def test_max_alerts_are_applied_without_country_limit(self):
        config, _ = load_config("config.yaml")
        config["sendable_alert_rules"]["max_sendable_per_core_mechanic"] = 10
        rows = [
            candidate(normalized_niche="a", top_apps=[{"app_id": "a1"}], group_key="a", opportunity_score=90),
            candidate(normalized_niche="b", top_apps=[{"app_id": "b1"}], group_key="b", opportunity_score=89),
            candidate(normalized_niche="c", top_apps=[{"app_id": "c1"}], group_key="c", opportunity_score=88),
            candidate(normalized_niche="d", top_apps=[{"app_id": "d1"}], group_key="d", opportunity_score=87),
            candidate(normalized_niche="e", top_apps=[{"app_id": "e1"}], group_key="e", opportunity_score=86),
        ]

        alerts, _, _ = filter_alerts(rows, config, {}, "2026-06-04")

        self.assertEqual(len(alerts), 3)

    def test_alert_key_and_id_do_not_include_country(self):
        row = candidate()

        key = alert_key(row)
        alert_id = build_alert_id(row, "2026-06-04")

        self.assertEqual(len(key), 16)
        self.assertNotIn("2026-06-04", key)
        self.assertTrue(alert_id.startswith("2026-06-04:"))
        self.assertIn(key, alert_id)
        self.assertNotIn("BR", alert_id)

    def test_high_production_complexity_blocks_alert(self):
        config, _ = load_config("config.yaml")

        passed, reasons = should_alert(
            candidate(
                production_complexity="high",
                full_product_complexity="high",
                mvp_complexity="medium",
                mvp_feasibility_score=65,
                simplifiable=True,
            ),
            config,
            {},
            "2026-06-04",
        )

        self.assertFalse(passed)
        self.assertIn("below_team_fit_score", reasons)


if __name__ == "__main__":
    unittest.main()
