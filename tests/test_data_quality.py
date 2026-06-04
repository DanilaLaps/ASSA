import unittest

from appstorespy_niche_monitor.config import load_config
from appstorespy_niche_monitor.data_quality import calculate_data_quality


class DataQualityTests(unittest.TestCase):
    def test_penalizes_missing_history_and_small_sample(self):
        config, _ = load_config("config.yaml")
        summary = {
            "app_count": 1,
            "top_app_share": 1.0,
            "total_monthly_revenue": 0,
            "history_depth_days": 0,
            "growth_by_one_app_share": 0.8,
        }
        apps = [
            {
                "downloads_daily": 20000,
                "downloads_month": 100000,
                "release_date": "",
                "update_date": "",
                "developer_name": "",
            }
        ]

        quality = calculate_data_quality(summary, apps, config, countries_with_signal=1)

        self.assertLess(quality["data_quality_score"], 70)
        self.assertIn("no_history", quality["data_quality_reasons"])
        self.assertIn("low_sample_size", quality["data_quality_reasons"])
        self.assertIn("one_app_growth", quality["data_quality_reasons"])


if __name__ == "__main__":
    unittest.main()
