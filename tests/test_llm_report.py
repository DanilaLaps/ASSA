import unittest

from appstorespy_niche_monitor.llm_report import (
    generate_fallback_analysis,
    parse_json_object,
    render_alert_report,
    validate_analysis,
)


def alert(**overrides):
    row = {
        "alert_id": "2026-06-04_BR_sort",
        "alert_tier": "TEST",
        "country": "BR",
        "niche": "sort puzzle",
        "core_mechanic": "sort",
        "theme": "supermarket",
        "meta": "collection",
        "audience": "women_25_45",
        "production_complexity": "low",
        "opportunity_score": 88,
        "data_quality_score": 82,
        "weekly_growth_percent": 35,
        "total_daily_installs": 90000,
        "total_monthly_revenue": 55000,
        "app_count": 3,
        "successful_new_apps_count": 1,
        "top_app_share": 0.45,
        "growth_by_one_app_share": 0.35,
        "giant_developer_share": 0.0,
        "top_apps": [{"name": "Goods Sort", "developer_name": "Tiny Team", "downloads_daily": 40000}],
        "score_components": {"demand": 20},
        "reason_codes": ["high_demand", "strong_growth"],
        "alert_filter_reasons": ["passed"],
    }
    row.update(overrides)
    return row


class LlmReportTests(unittest.TestCase):
    def test_parse_json_object_from_fenced_response(self):
        parsed = parse_json_object('```json\n{"recommendation": "TEST"}\n```')

        self.assertEqual(parsed["recommendation"], "TEST")

    def test_validate_analysis_fills_missing_fields_and_normalizes_recommendation(self):
        analysis = validate_analysis({"recommendation": "maybe", "evidence": "one fact"}, alert())

        self.assertEqual(analysis["recommendation"], "TEST")
        self.assertEqual(analysis["evidence"], ["one fact"])
        self.assertIn("mvp", analysis)

    def test_fallback_analysis_avoids_giant_dominated_alert(self):
        analysis = generate_fallback_analysis(
            alert(alert_tier="WATCH", reason_codes=["giant_dominated"], giant_developer_share=0.8)
        )

        self.assertEqual(analysis["recommendation"], "AVOID")
        self.assertTrue(analysis["risks"])

    def test_render_report_includes_structured_analysis(self):
        analysis = generate_fallback_analysis(alert())
        markdown = render_alert_report(alert(), analysis)

        self.assertIn("## Structured analysis", markdown)
        self.assertIn("Recommendation: TEST", markdown)


if __name__ == "__main__":
    unittest.main()
