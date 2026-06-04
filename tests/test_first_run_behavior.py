import unittest

from appstorespy_niche_monitor.config import load_config
from appstorespy_niche_monitor.first_run_handler import (
    FIRST_RUN_NO_HISTORY,
    HISTORY_AVAILABLE,
    apply_initial_baseline_rules,
    detect_history_state,
)


def candidate(**overrides):
    row = {
        "candidate_id": "2026-06-04:abc:normalized_niche",
        "status": "ALERT",
        "reason_codes": ["strong_daily_installs"],
        "data_quality_score": 90,
        "opportunity_score": 85,
        "dedupe_key": "abc",
    }
    row.update(overrides)
    return row


class FirstRunBehaviorTests(unittest.TestCase):
    def test_detects_first_run_when_no_compatible_history(self):
        config, _ = load_config("config.yaml")

        state = detect_history_state([{"snapshot_date": "2026-06-03", "score_version": "v1.2"}], config, "2026-06-04")

        self.assertEqual(state, FIRST_RUN_NO_HISTORY)

    def test_detects_history_when_score_version_matches(self):
        config, _ = load_config("config.yaml")

        state = detect_history_state([{"snapshot_date": "2026-06-03", "score_version": "v1.3.2"}], config, "2026-06-04")

        self.assertEqual(state, HISTORY_AVAILABLE)

    def test_first_run_blocks_regular_alert_and_cooldown(self):
        config, _ = load_config("config.yaml")

        items = apply_initial_baseline_rules([candidate()], config, FIRST_RUN_NO_HISTORY)

        self.assertEqual(items[0]["status"], "ALERT")
        self.assertEqual(items[0]["would_be_status"], "ALERT")
        self.assertFalse(items[0]["send_regular_alert"])
        self.assertTrue(items[0]["exclude_from_cooldown"])
        self.assertTrue(items[0]["initial_baseline_digest"])
        self.assertIn("INITIAL_BASELINE_NO_HISTORY", items[0]["reason_codes"])
        self.assertEqual(items[0]["confidence_level"], "MEDIUM")


if __name__ == "__main__":
    unittest.main()
