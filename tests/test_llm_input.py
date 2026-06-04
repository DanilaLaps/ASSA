import unittest

from appstorespy_niche_monitor.config import load_config
from appstorespy_niche_monitor.llm_report import build_candidate_pack_input


def candidate(status, **overrides):
    row = {
        "candidate_id": f"id-{status}",
        "status": status,
        "normalized_niche": f"niche-{status}",
        "top_apps": [{"app_id": "a", "name": "A", "raw_source_fields_json": {"secret": "raw"}}],
        "raw_source_fields_json": {"secret": "raw"},
        "reason_codes": ["strong_daily_installs"],
        "risk_tags": [],
    }
    row.update(overrides)
    return row


class LlmInputTests(unittest.TestCase):
    def test_pack_contains_candidate_status_groups_without_raw_apps(self):
        config, _ = load_config("config.yaml")

        pack = build_candidate_pack_input(
            [
                candidate("ALERT"),
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
        self.assertEqual(len(pack["watch"]), 2)
        self.assertEqual(len(pack["near_misses"]), 1)
        self.assertEqual(pack["coverage_summary"]["sample_truncated"], False)
        self.assertEqual(pack["history_summary"]["history_state"], "HISTORY_AVAILABLE")
        serialized = str(pack)
        self.assertNotIn("raw_source_fields_json", serialized)


if __name__ == "__main__":
    unittest.main()
