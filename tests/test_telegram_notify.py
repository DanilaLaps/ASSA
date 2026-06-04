import unittest

from appstorespy_niche_monitor.telegram_notify import chunk_text, format_alert_message, format_run_summary_message


class TelegramNotifyTests(unittest.TestCase):
    def test_format_alert_message_uses_analysis_template(self):
        message = format_alert_message(
            {
                "alert_id": "2026-06-04:sort:abc:last_180d",
                "niche": "sort puzzle",
                "opportunity_score": 88,
                "data_quality_score": 82,
                "release_date_window": "last_180d",
                "collection_sort": "-release_date",
                "min_app_daily_installs": 500,
                "total_daily_installs": 90000,
                "app_count": 3,
                "successful_new_apps_count": 1,
                "llm_analysis": {
                    "evidence": ["Strong demand", "Fresh apps"],
                    "mvp": "Build a goods sort MVP.",
                    "risks": ["Paid spike risk"],
                    "recommendation": "TEST",
                },
            }
        )

        self.assertIn("Fresh Game Niche Alert: sort puzzle", message)
        self.assertIn("Scope: one AppStoreSpy query, no country/language filter", message)
        self.assertNotIn("Country:", message)
        self.assertIn("MVP:", message)
        self.assertIn("Recommendation: TEST", message)

    def test_chunk_text_splits_long_messages(self):
        chunks = chunk_text("abcdef", 2)

        self.assertEqual(chunks, ["ab", "cd", "ef"])

    def test_format_run_summary_message_reports_no_alerts(self):
        message = format_run_summary_message(
            {
                "mode": "production",
                "snapshot_date": "2026-06-04",
                "apps_count": 250,
                "summaries_count": 37,
                "alerts_count": 0,
                "watch_count": 4,
                "rejected_count": 33,
                "baseline_only": False,
            }
        )

        self.assertIn("AppStoreSpy check completed", message)
        self.assertIn("TEST alerts: 0", message)
        self.assertIn("No TEST alerts passed filters", message)
        self.assertIn("Scope: one AppStoreSpy query, no country/language filter", message)


if __name__ == "__main__":
    unittest.main()
