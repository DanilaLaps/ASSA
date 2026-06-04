import unittest

from appstorespy_niche_monitor.report_writer import render_initial_baseline_report


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


if __name__ == "__main__":
    unittest.main()
