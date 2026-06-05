import unittest
from unittest.mock import patch

from appstorespy_niche_monitor.telegram_notify import (
    chunk_text,
    format_alert_message,
    format_initial_baseline_digest_message,
    format_run_summary_message,
    send_alerts,
)


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
                "top_apps": [
                    {
                        "name": "Goods Sort",
                        "developer_name": "Tiny Team",
                        "downloads_daily": 40000,
                        "revenue_month": 1200,
                        "rating_avg": 4.5,
                        "url_appstorespy": "https://appstorespy.example/apps/goods-sort",
                    },
                    {
                        "name": "Shelf Match",
                        "developer_name": "Small Studio",
                        "downloads_daily": 30000,
                        "url_appstorespy": "https://appstorespy.example/apps/shelf-match",
                    },
                    {
                        "name": "Market Sort",
                        "developer_name": "Indie Lab",
                        "downloads_daily": 20000,
                        "url_appstorespy": "https://appstorespy.example/apps/market-sort",
                    },
                    {
                        "name": "Fourth Competitor",
                        "developer_name": "Extra Studio",
                        "downloads_daily": 10000,
                        "url_appstorespy": "https://appstorespy.example/apps/fourth",
                    },
                ],
                "llm_analysis_source": "openai",
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
        self.assertIn("AI review: source=openai", message)
        self.assertIn("Top competitors:", message)
        self.assertIn("https://appstorespy.example/apps/goods-sort", message)
        self.assertIn("https://appstorespy.example/apps/shelf-match", message)
        self.assertIn("https://appstorespy.example/apps/market-sort", message)
        self.assertNotIn("Fourth Competitor", message)
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
                "sendable_alerts_count": 0,
                "watch_count": 4,
                "near_miss_count": 0,
                "rejected_count": 33,
                "mixed_unknown_clusters_count": 5,
                "unknown_dominant_clusters_count": 2,
                "unknown_blocker_active_count": 1,
                "unknown_pattern_blocker_active_blocked_count": 1,
                "baseline_only": False,
                "llm_status": {
                    "analysis_source": "openai",
                    "model": "gpt-4.1-mini",
                },
            }
        )

        self.assertIn("AppStoreSpy check completed", message)
        self.assertIn("SENDABLE alerts: 0", message)
        self.assertIn("LLM TEST recommendations among sendable alerts: 0", message)
        self.assertIn("Separate TEST messages sent: 0", message)
        self.assertIn("Scope: one AppStoreSpy query, no country/language filter", message)
        self.assertIn("LLM review: source=openai", message)
        self.assertIn("Mixed unknown clusters: 5", message)
        self.assertIn("Unknown-dominant clusters: 2", message)
        self.assertIn("Unknown blocker active: 1", message)
        self.assertIn("Candidates blocked by unknown_pattern_blocker_active: 1", message)

    def test_format_initial_baseline_digest_includes_review(self):
        message = format_initial_baseline_digest_message(
            [
                {
                    "normalized_niche": "sort_puzzle",
                    "would_be_status": "ALERT",
                    "opportunity_score": 79.5,
                    "total_daily_installs": 50000,
                    "reason_codes": ["INITIAL_BASELINE_NO_HISTORY"],
                    "llm_status": {
                        "analysis_source": "openai",
                        "model": "gpt-4.1-mini",
                        "api_key_present": True,
                    },
                    "llm_analysis_source": "openai",
                    "llm_analysis": {
                        "recommendation": "WATCH",
                        "confidence": "medium",
                        "mvp_hypothesis": "Test a focused sorting MVP.",
                        "why_might_be_false_positive": ["possible paid spike"],
                    },
                }
            ]
        )

        self.assertIn("Review: recommendation=WATCH", message)
        self.assertIn("source=openai", message)
        self.assertIn("LLM: source=openai", message)
        self.assertIn("MVP: Test a focused sorting MVP.", message)

    def test_format_initial_baseline_digest_includes_fallback_reason(self):
        message = format_initial_baseline_digest_message(
            [
                {
                    "normalized_niche": "sort_puzzle",
                    "would_be_status": "ALERT",
                    "opportunity_score": 79.5,
                    "total_daily_installs": 50000,
                    "reason_codes": ["INITIAL_BASELINE_NO_HISTORY"],
                    "llm_status": {
                        "analysis_source": "fallback",
                        "model": "gpt-4.1-mini",
                        "api_key_present": False,
                        "fallback_reason": "missing_openai_api_key",
                    },
                    "llm_analysis_source": "fallback",
                    "llm_fallback_reason": "missing_openai_api_key",
                    "llm_analysis": {
                        "recommendation": "WATCH",
                        "confidence": "medium",
                        "mvp_hypothesis": "Test a focused sorting MVP.",
                    },
                }
            ]
        )

        self.assertIn("LLM: source=fallback", message)
        self.assertIn("fallback_reason=missing_openai_api_key", message)

    def test_regular_telegram_requires_sendable_alert_stage(self):
        with patch.dict(
            "os.environ",
            {"TELEGRAM_BOT_TOKEN": "token", "TELEGRAM_CHAT_ID": "chat"},
            clear=True,
        ):
            with patch("appstorespy_niche_monitor.telegram_notify.send_message") as send_message:
                with self.assertRaises(AssertionError):
                    send_alerts(
                        [
                            {
                                "status": "ALERT",
                                "send_regular_alert": True,
                                "alert_stage": "QUALIFIED_CANDIDATE_ONLY",
                            }
                        ],
                        {"telegram": {"enabled": True}},
                    )

        send_message.assert_not_called()


if __name__ == "__main__":
    unittest.main()
