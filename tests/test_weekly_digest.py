import unittest

from appstorespy_niche_monitor.config import load_config
from appstorespy_niche_monitor.weekly_digest import generate_weekly_digest


class WeeklyDigestTests(unittest.TestCase):
    def test_digest_includes_feedback_and_calibration_recommendations(self):
        config, _ = load_config("config.yaml")
        summaries = [
            {
                "snapshot_date": "2026-06-04",
                "country": "BR",
                "niche": "other",
                "core_mechanic": "other",
                "theme": "other",
                "opportunity_score": 68,
                "data_quality_score": 71,
                "weekly_growth_percent": 30,
                "total_daily_installs": 70000,
                "growth_by_one_app_share": 0.7,
                "top_app_share": 0.8,
                "giant_developer_share": 0.0,
            }
        ]
        feedback = [{"status": "false_positive", "reason": "paid_spike"}]

        markdown = generate_weekly_digest(summaries, feedback, config, snapshot_date="2026-06-04")

        self.assertIn("Feedback summary", markdown)
        self.assertIn("false_positive", markdown)
        self.assertIn("Review max_growth_by_one_app_share", markdown)
        self.assertIn("Niches classified as other", markdown)


if __name__ == "__main__":
    unittest.main()
