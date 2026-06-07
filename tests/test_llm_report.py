import unittest
from unittest.mock import patch

from appstorespy_niche_monitor.llm_report import (
    analyze_candidate_pack,
    build_candidate_pack_input,
    build_llm_status,
    build_pack_prompt,
    generate_fallback_analysis,
    generate_fallback_pack_analysis,
    generate_openai_pack_analysis,
    parse_json_object,
    render_alert_report,
    validate_analysis,
)


def alert(**overrides):
    row = {
        "alert_id": "2026-06-04:sort_puzzle_sort_supermarket_collection_women_25_45:abc123:last_180d",
        "alert_tier": "TEST",
        "niche": "sort puzzle",
        "core_mechanic": "sort",
        "theme": "supermarket",
        "meta": "collection",
        "audience": "women_25_45",
        "production_complexity": "low",
        "opportunity_score": 88,
        "data_quality_score": 82,
        "release_date_window": "last_180d",
        "collection_sort": "-release_date",
        "min_app_daily_installs": 500,
        "weekly_growth_percent": 35,
        "total_daily_installs": 90000,
        "total_monthly_revenue": 55000,
        "app_count": 3,
        "successful_new_apps_count": 1,
        "top_app_share": 0.45,
        "growth_by_one_app_share": 0.35,
        "advertised_top_app_share": 0.0,
        "giant_developer_share": 0.0,
        "top_apps": [{"name": "Goods Sort", "developer_name": "Tiny Team", "downloads_daily": 40000}],
        "score_components": {"demand": 20},
        "reason_codes": ["high_demand", "historical_growth"],
        "alert_filter_reasons": ["passed"],
    }
    row.update(overrides)
    return row


def pack_candidate(**overrides):
    row = {
        "candidate_id": "candidate-1",
        "status": "ALERT",
        "would_be_status": "ALERT",
        "normalized_niche": "sort_puzzle",
        "core_mechanic": "sort",
        "theme": "supermarket",
        "opportunity_score": 79.5,
        "data_quality_score": 82,
        "mvp_feasibility_score": 80,
        "total_daily_installs": 50000,
        "reason_codes": ["strong_daily_installs", "INITIAL_BASELINE_NO_HISTORY"],
        "risk_tags": [],
        "first_run_without_history": True,
        "initial_baseline_digest": True,
        "send_regular_alert": True,
        "alert_stage": "SENDABLE_ALERT",
    }
    row.update(overrides)
    return row


def llm_config(**overrides):
    config = {
        "alert_limits": {
            "max_alerts_per_run": 3,
            "max_watch_items_per_digest": 10,
            "max_near_misses_in_report": 10,
        },
        "first_run_behavior": {"max_initial_digest_items": 10},
        "llm": {
            "enabled": True,
            "model_env": "OPENAI_MODEL",
            "default_model": "test-model",
            "timeout_seconds": 5,
            "max_output_tokens": 1000,
        },
    }
    config.update(overrides)
    return config


class FakeOpenAIResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self):
        return self.payload


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
        self.assertIn("## Source Scope", markdown)
        self.assertIn("no country, language, or active_countries filter", markdown)
        self.assertIn("Recommendation: TEST", markdown)

    def test_fallback_analysis_avoids_country_specific_claims(self):
        analysis = generate_fallback_analysis(alert())

        self.assertIn("одном AppStoreSpy query-срезе", analysis["summary"])
        self.assertNotIn("BR", analysis["summary"])

    def test_analyze_candidate_pack_reports_missing_openai_key(self):
        with patch.dict("os.environ", {}, clear=True):
            analysis = analyze_candidate_pack([pack_candidate()], llm_config())

        self.assertEqual(analysis["analysis_source"], "fallback")
        self.assertEqual(analysis["llm_status"]["fallback_reason"], "missing_openai_api_key")
        self.assertEqual(analysis["candidate_analysis_sources"]["candidate-1"], "fallback")

    def test_analyze_candidate_pack_reports_cli_disabled(self):
        analysis = analyze_candidate_pack([pack_candidate()], llm_config(), use_llm=False)

        self.assertEqual(analysis["llm_status"]["fallback_reason"], "disabled_by_cli")

    def test_analyze_candidate_pack_reports_config_disabled(self):
        config = llm_config(llm={"enabled": False})

        analysis = analyze_candidate_pack([pack_candidate()], config)

        self.assertEqual(analysis["llm_status"]["fallback_reason"], "disabled_in_config")

    def test_analyze_candidate_pack_skips_openai_when_no_sendable_alerts(self):
        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}, clear=True):
            with patch("appstorespy_niche_monitor.llm_report.urllib.request.urlopen") as urlopen:
                analysis = analyze_candidate_pack(
                    [
                        pack_candidate(
                            send_regular_alert=False,
                            alert_stage="QUALIFIED_CANDIDATE_ONLY",
                        )
                    ],
                    llm_config(),
                )

        urlopen.assert_not_called()
        self.assertEqual(analysis["analysis_source"], "fallback")
        self.assertEqual(analysis["llm_status"]["fallback_reason"], "no_sendable_alerts")
        self.assertIn("нет финальных SENDABLE_ALERT-кандидатов", analysis["llm_fallback_note_ru"])
        self.assertFalse(analysis["llm_status"]["should_call_openai"])

    def test_generate_openai_pack_analysis_marks_openai_candidate_sources(self):
        config = llm_config()
        pack_input = build_candidate_pack_input([pack_candidate()], config)
        fallback = generate_fallback_pack_analysis(pack_input)
        response_json = (
            b'{"output_text":"{\\"candidate_analyses\\":{\\"candidate-1\\":'
            b'{\\"recommendation\\":\\"WATCH\\",\\"confidence\\":\\"medium\\",'
            b'\\"mvp_hypothesis\\":\\"Test a focused sorting MVP.\\"}}}"}'
        )
        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}, clear=True):
            status = build_llm_status(pack_input, config, use_llm=True)
            with patch(
                "appstorespy_niche_monitor.llm_report.urllib.request.urlopen",
                return_value=FakeOpenAIResponse(response_json),
            ):
                analysis = generate_openai_pack_analysis(pack_input, config, fallback, status)

        self.assertEqual(analysis["analysis_source"], "openai")
        self.assertEqual(analysis["candidate_analysis_sources"]["candidate-1"], "openai")
        self.assertEqual(analysis["candidate_analyses"]["candidate-1"]["mvp_hypothesis"], "Test a focused sorting MVP.")
        self.assertEqual(
            analysis["candidate_analyses"]["candidate-1"]["llm_language_warning"],
            "non_russian_text_detected",
        )

    def test_pack_prompt_is_readable_and_requests_json(self):
        prompt = build_pack_prompt({"alerts": [], "watch": [], "near_misses": [], "initial_baseline_digest": []})

        self.assertIn("Return only a JSON object", prompt)
        self.assertIn("Отвечай только на русском языке", prompt)
        self.assertIn("одного AppStoreSpy query", prompt)
        self.assertIn("top_products", prompt)
        self.assertIn("competitor_takeaways", prompt)
        self.assertIn("Python deterministic scoring уже выбрал sendable alerts", prompt)
        self.assertIn("Верни анализ для каждого candidate_id из alerts", prompt)
        self.assertIn("recommendation", prompt)
        self.assertIn("TEST", prompt)
        self.assertIn("WATCH", prompt)
        self.assertIn("AVOID", prompt)
        self.assertIn("confidence", prompt)
        self.assertIn("low", prompt)
        self.assertIn("medium", prompt)
        self.assertIn("high", prompt)
        self.assertIn("не переводи", prompt.lower())

    def test_fallback_pack_analysis_is_russian(self):
        pack_input = build_candidate_pack_input([pack_candidate()], llm_config())

        analysis = generate_fallback_pack_analysis(pack_input)
        candidate_analysis = analysis["candidate_analyses"]["candidate-1"]

        self.assertEqual(candidate_analysis["recommendation"], "WATCH")
        self.assertEqual(candidate_analysis["confidence"], "medium")
        self.assertIn("Проверить узкий MVP", candidate_analysis["mvp_hypothesis"])
        self.assertIn("одном AppStoreSpy query-срезе", candidate_analysis["summary"])

    def test_openai_response_schema_unchanged(self):
        pack_input = build_candidate_pack_input([pack_candidate()], llm_config())
        fallback = generate_fallback_pack_analysis(pack_input)

        self.assertIn("candidate_analyses", fallback)
        self.assertIn("candidate-1", fallback["candidate_analyses"])
        candidate_analysis = fallback["candidate_analyses"]["candidate-1"]
        for field in (
            "recommendation",
            "confidence",
            "why_interesting",
            "why_might_be_false_positive",
            "mvp_hypothesis",
            "simplified_mvp_scope",
            "competitor_takeaways",
            "entry_angle",
            "differentiation_idea",
            "why_top_products_validate_or_weaken_signal",
            "validation_steps",
            "risk_notes",
            "missing_data",
            "manual_review_needed",
        ):
            self.assertIn(field, candidate_analysis)


if __name__ == "__main__":
    unittest.main()
