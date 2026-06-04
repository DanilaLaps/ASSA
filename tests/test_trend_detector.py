import unittest

from appstorespy_niche_monitor.trend_detector import detect_trends


class TrendDetectorTests(unittest.TestCase):
    def test_growth_and_one_app_share_are_calculated_from_history(self):
        current = [
            {
                "snapshot_date": "2026-06-04",
                "group_key": "google_play::BR::sort puzzle::puzzle::sort::supermarket::collection::women_25_45::low",
                "total_daily_installs": 90000,
                "top_apps": [
                    {"app_id": "a", "downloads_daily": 40000},
                    {"app_id": "b", "downloads_daily": 30000},
                    {"app_id": "c", "downloads_daily": 20000},
                ],
            }
        ]
        history = [
            {
                "snapshot_date": "2026-05-28",
                "group_key": "google_play::BR::sort puzzle::puzzle::sort::supermarket::collection::women_25_45::low",
                "total_daily_installs": 60000,
                "top_apps": [
                    {"app_id": "a", "downloads_daily": 25000},
                    {"app_id": "b", "downloads_daily": 25000},
                    {"app_id": "c", "downloads_daily": 10000},
                ],
            }
        ]

        result = detect_trends(current, history, "2026-06-04")[0]

        self.assertEqual(result["weekly_growth_percent"], 50.0)
        self.assertAlmostEqual(result["growth_by_one_app_share"], 0.5)
        self.assertTrue(result["has_history"])
        self.assertEqual(result["history_depth_days"], 7)


if __name__ == "__main__":
    unittest.main()
