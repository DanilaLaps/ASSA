import unittest

from appstorespy_niche_monitor.alert_filter import apply_cooldown_and_alert_limits
from appstorespy_niche_monitor.config import load_config
from appstorespy_niche_monitor.dedupe import make_alert_instance_id, make_dedupe_key


class AlertDedupeTests(unittest.TestCase):
    def test_dedupe_key_is_stable_and_date_free(self):
        key = make_dedupe_key("sort_puzzle", ["b", "a", "c"], "last_180d")
        same = make_dedupe_key("sort_puzzle", ["c", "b", "a"], "last_180d")
        alert_instance_id = make_alert_instance_id("2026-06-04", key)

        self.assertEqual(key, same)
        self.assertNotIn("2026-06-04", key)
        self.assertEqual(alert_instance_id, f"2026-06-04:{key}")

    def test_cooldown_uses_dedupe_key(self):
        config, _ = load_config("config.yaml")
        key = make_dedupe_key("sort_puzzle", ["a"], "last_180d")
        candidates = [
            {
                "status": "ALERT",
                "dedupe_key": key,
                "normalized_niche": "sort_puzzle",
                "market_category": "puzzle",
                "core_mechanic": "sort",
                "theme": "supermarket",
                "meta": "collection",
                "production_complexity": "low",
                "full_product_complexity": "low",
                "mvp_complexity": "low",
                "mvp_feasibility_score": 85,
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
                "reason_codes": [],
                "risk_tags": [],
                "top_apps": [
                    {"app_id": "a", "developer_name": "A Studio", "downloads_daily": 40000},
                    {"app_id": "b", "developer_name": "B Studio", "downloads_daily": 30000},
                    {"app_id": "c", "developer_name": "C Studio", "downloads_daily": 20000},
                ],
            }
        ]
        sent_alerts = {key: {"normalized_niche": "sort_puzzle", "last_sent_at": "2026-06-03"}}

        filtered = apply_cooldown_and_alert_limits(candidates, config, sent_alerts, "2026-06-04")

        self.assertFalse(filtered[0]["send_regular_alert"])
        self.assertIn("cooldown", filtered[0]["alert_filter_reasons"])
        self.assertIn("cooldown_exact_dedupe_key", filtered[0]["sendable_alert_failures"])


if __name__ == "__main__":
    unittest.main()
