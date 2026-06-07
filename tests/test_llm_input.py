import unittest

from appstorespy_niche_monitor.config import load_config
from appstorespy_niche_monitor.llm_report import build_candidate_pack_input


def candidate(status, **overrides):
    row = {
        "candidate_id": f"id-{status}",
        "status": status,
        "normalized_niche": f"niche-{status}",
        "top_apps": [
            {
                "app_id": "a",
                "bundle": "com.example.a",
                "name": "A",
                "developer_name": "Tiny Team",
                "downloads_daily": 5000,
                "downloads_month": 150000,
                "revenue_month": 1000,
                "rating_avg": 4.4,
                "rating_count": 200,
                "release_date": "2026-05-01",
                "update_date": "2026-05-15",
                "description_short": "Sort products quickly.",
                "description_excerpt": "Arrange products into shelves with simple sorting rules.",
                "screenshots": ["one.png", "two.png", "three.png", "four.png"],
                "url_appstorespy": "https://appstorespy.example/apps/com.example.a",
                "raw_source_fields_json": {"secret": "raw"},
            }
        ],
        "raw_source_fields_json": {"secret": "raw"},
        "reason_codes": ["strong_daily_installs"],
        "risk_tags": [],
    }
    row.update(overrides)
    return row


class LlmInputTests(unittest.TestCase):
    def test_pack_contains_only_sendable_alerts_without_raw_apps(self):
        config, _ = load_config("config.yaml")

        pack = build_candidate_pack_input(
            [
                candidate("ALERT", send_regular_alert=True, alert_stage="SENDABLE_ALERT"),
                candidate("WATCH"),
                candidate("SINGLE_APP_WATCH"),
                candidate("NEAR_MISS"),
                candidate("REJECT"),
            ],
            config,
            {"sample_truncated": False},
            {"history_state": "HISTORY_AVAILABLE"},
        )

        self.assertEqual(len(pack["alerts"]), 1)
        self.assertEqual(len(pack["watch"]), 0)
        self.assertEqual(len(pack["near_misses"]), 0)
        self.assertEqual(len(pack["initial_baseline_digest"]), 0)
        self.assertEqual(pack["coverage_summary"]["sample_truncated"], False)
        self.assertEqual(pack["history_summary"]["history_state"], "HISTORY_AVAILABLE")
        self.assertEqual(pack["alerts"][0]["top_products"][0]["url_appstorespy"], "https://appstorespy.example/apps/com.example.a")
        self.assertEqual(pack["alerts"][0]["top_products"][0]["screenshots"], ["one.png", "two.png", "three.png"])
        self.assertEqual(pack["alerts"][0]["top_competitors"][0]["description_short"], "Sort products quickly.")
        serialized = str(pack)
        self.assertNotIn("raw_source_fields_json", serialized)

    def test_sendable_alerts_are_prioritized_for_llm_pack(self):
        config, _ = load_config("config.yaml")
        config["alert_limits"]["max_alerts_per_run"] = 1

        pack = build_candidate_pack_input(
            [
                candidate("ALERT", candidate_id="cooldown-alert", send_regular_alert=False),
                candidate("ALERT", candidate_id="sendable-alert", send_regular_alert=True, alert_stage="SENDABLE_ALERT"),
            ],
            config,
        )

        self.assertEqual(len(pack["alerts"]), 1)
        self.assertEqual(pack["alerts"][0]["candidate_id"], "sendable-alert")

    def test_non_sendable_alerts_are_excluded_from_llm_pack(self):
        config, _ = load_config("config.yaml")

        pack = build_candidate_pack_input(
            [
                candidate("ALERT", candidate_id="cooldown-alert", send_regular_alert=False),
                candidate("ALERT", candidate_id="unset-alert"),
            ],
            config,
        )

        self.assertEqual(pack["alerts"], [])

    def test_llm_pack_source_scope_preserved_with_russian_output_config(self):
        config, _ = load_config("config.yaml")

        pack = build_candidate_pack_input(
            [
                candidate(
                    "ALERT",
                    candidate_id="sendable-alert",
                    send_regular_alert=True,
                    alert_stage="SENDABLE_ALERT",
                    source_scope="single_appstorespy_query_no_country_language",
                )
            ],
            config,
        )

        self.assertEqual(config["language"]["telegram_language"], "ru")
        self.assertEqual(config["llm"]["output_language"], "ru")
        self.assertEqual(pack["alerts"][0]["source_scope"], "single_appstorespy_query_no_country_language")
        serialized = str(pack)
        self.assertNotIn("raw_source_fields_json", serialized)


if __name__ == "__main__":
    unittest.main()
