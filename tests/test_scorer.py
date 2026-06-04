import unittest

from appstorespy_niche_monitor.config import load_config
from appstorespy_niche_monitor.scorer import score_summary


class ScorerTests(unittest.TestCase):
    def test_high_quality_growing_small_team_niche_scores_high(self):
        config, _ = load_config("config.yaml")
        summary = {
            "niche": "sort puzzle",
            "production_complexity": "low",
            "total_daily_installs": 90000,
            "weekly_growth_percent": 55,
            "successful_new_apps_count": 2,
            "total_monthly_revenue": 55000,
            "avg_rating": 4.4,
            "app_count": 4,
            "top_app_share": 0.42,
            "growth_by_one_app_share": 0.35,
            "giant_developer_share": 0.0,
            "data_quality_score": 85,
        }

        scored = score_summary(summary, config)

        self.assertGreaterEqual(scored["opportunity_score"], 75)
        self.assertIn("strong_growth", scored["reason_codes"])
        self.assertIn("small_team_fit", scored["reason_codes"])
        self.assertIn("score_components", scored)


if __name__ == "__main__":
    unittest.main()
