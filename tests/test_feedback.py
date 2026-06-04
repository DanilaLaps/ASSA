import tempfile
import unittest
from pathlib import Path

from appstorespy_niche_monitor.config import load_config
from appstorespy_niche_monitor.feedback import add_feedback, feedback_summary, read_feedback


class FeedbackTests(unittest.TestCase):
    def test_feedback_record_round_trip(self):
        config, _ = load_config("config.yaml")
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "feedback.json"

            add_feedback(
                path,
                config,
                alert_id="2026-06-04_BR_sort",
                status="false_positive",
                reason="paid_spike",
                notes="Growth came from one app.",
                reviewed_at="2026-06-04",
            )
            records = read_feedback(path)

            self.assertEqual(len(records), 1)
            self.assertEqual(records[0]["status"], "false_positive")
            self.assertEqual(feedback_summary(records), {"false_positive": 1})


if __name__ == "__main__":
    unittest.main()
