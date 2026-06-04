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
                "opportunity_score": 90,
                "reason_codes": [],
                "risk_tags": [],
            }
        ]
        sent_alerts = {key: {"normalized_niche": "sort_puzzle", "last_sent_at": "2026-06-03"}}

        filtered = apply_cooldown_and_alert_limits(candidates, config, sent_alerts, "2026-06-04")

        self.assertFalse(filtered[0]["send_regular_alert"])
        self.assertIn("cooldown", filtered[0]["alert_filter_reasons"])


if __name__ == "__main__":
    unittest.main()
