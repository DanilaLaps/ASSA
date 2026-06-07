import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from appstorespy_niche_monitor.report_writer import (
    render_initial_baseline_report,
    render_manual_review_digest,
    write_no_sendable_diagnostics,
)


class ReportWriterTests(unittest.TestCase):
    def test_initial_baseline_report_includes_ai_review(self):
        markdown = render_initial_baseline_report(
            [
                {
                    "normalized_niche": "sort_puzzle",
                    "would_be_status": "ALERT",
                    "opportunity_score": 79.5,
                    "total_daily_installs": 50000,
                    "reason_codes": ["strong_daily_installs", "INITIAL_BASELINE_NO_HISTORY"],
                    "confidence_level": "MEDIUM",
                    "llm_analysis_source": "openai",
                    "llm_analysis": {
                        "recommendation": "WATCH",
                        "confidence": "medium",
                        "why_interesting": ["fresh traction", "small-team fit"],
                        "why_might_be_false_positive": ["possible paid spike"],
                        "mvp_hypothesis": "Test a focused goods sorting MVP.",
                        "simplified_mvp_scope": "One core loop and one shelf theme.",
                        "validation_steps": ["Check top apps manually."],
                    },
                }
            ],
            "2026-06-05",
        )

        self.assertIn("AI Review", markdown)
        self.assertIn("source=openai", markdown)
        self.assertIn("mvp_hypothesis: Test a focused goods sorting MVP.", markdown)
        self.assertIn("validation_steps", markdown)

    def test_initial_baseline_report_includes_fallback_reason(self):
        markdown = render_initial_baseline_report(
            [
                {
                    "normalized_niche": "sort_puzzle",
                    "would_be_status": "ALERT",
                    "opportunity_score": 79.5,
                    "total_daily_installs": 50000,
                    "reason_codes": ["INITIAL_BASELINE_NO_HISTORY"],
                    "confidence_level": "MEDIUM",
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
                        "why_interesting": ["fresh traction"],
                    },
                }
            ],
            "2026-06-05",
        )

        self.assertIn("LLM: source=fallback", markdown)
        self.assertIn("fallback_reason=missing_openai_api_key", markdown)
        self.assertIn("Automated Review", markdown)

    def test_no_sendable_diagnostics_written_when_alerts_exist(self):
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            paths = {
                "processed_dir": root / "data" / "processed",
                "reports_daily_dir": root / "reports" / "daily",
            }
            for path in paths.values():
                path.mkdir(parents=True, exist_ok=True)

            written = write_no_sendable_diagnostics(
                paths,
                [
                    {
                        "candidate_id": "candidate-1",
                        "status": "ALERT",
                        "normalized_niche": "sort_puzzle",
                        "group_key_type": "normalized_niche",
                        "market_signal_key": "signal",
                        "opportunity_score": 74,
                        "sendable_alert_score": 69,
                        "trend_confidence_score": 55,
                        "team_fit_score": 60,
                        "data_quality_score": 70,
                        "classification_confidence_avg": 0.7,
                        "mvp_feasibility_score": 85,
                        "organic_confidence": "MEDIUM",
                        "hard_blockers_count": 0,
                        "soft_blockers_count": 1,
                        "first_blocking_failure": "below_sendable_alert_score",
                        "sendable_alert_failures": ["below_sendable_alert_score"],
                        "sendable_threshold_margins": {"sendable_alert_score": -11},
                        "top_apps": [
                            {
                                "name": "Goods Sort",
                                "developer_name": "Tiny Team",
                                "downloads_daily": 1000,
                                "rating_avg": 4.5,
                                "advertised": False,
                                "release_date": "2026-05-01",
                            }
                        ],
                    }
                ],
                "2026-06-05",
            )

            for path in written:
                self.assertTrue(Path(path).exists())
            markdown = (paths["reports_daily_dir"] / "2026-06-05_no_sendable_diagnostics.md").read_text(
                encoding="utf-8"
            )
            self.assertIn("Top ALERT Candidates Closest To SENDABLE", markdown)
            self.assertIn("below_sendable_alert_score", markdown)

    def test_manual_review_digest_is_russian(self):
        markdown = render_manual_review_digest(
            {
                "top_alert_candidates_closest_to_sendable": [
                    {
                        "status": "ALERT",
                        "normalized_niche": "sort_puzzle",
                        "alert_strength": "MEDIUM_ALERT",
                        "sendable_alert_score": 69,
                        "opportunity_score": 74,
                        "hard_blockers_count": 0,
                        "soft_blockers_count": 1,
                        "first_blocking_failure": "below_sendable_alert_score",
                        "organic_confidence": "MEDIUM",
                        "sendable_alert_failures": ["below_sendable_alert_score"],
                    }
                ],
                "top_candidates_blocked_by_exactly_one_condition": [],
            },
            "2026-06-05",
        )

        self.assertIn("Сегодня нет сильных SENDABLE-alerts", markdown)
        self.assertIn("только для ручной проверки", markdown)
        self.assertIn("не записаны в sent_alerts.json", markdown)
        self.assertIn("below_sendable_alert_score", markdown)


if __name__ == "__main__":
    unittest.main()
