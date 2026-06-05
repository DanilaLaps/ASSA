import unittest

from appstorespy_niche_monitor.alert_ranker import (
    calculate_sendable_alert_score,
    enrich_sendable_alert_fields,
    passes_sendable_hard_filters,
)
from appstorespy_niche_monitor.config import load_config


def candidate(**overrides):
    row = {
        "candidate_id": "candidate-1",
        "status": "ALERT",
        "normalized_niche": "sort_puzzle",
        "market_category": "puzzle",
        "core_mechanic": "sort",
        "theme": "supermarket",
        "meta": "collection",
        "production_complexity": "low",
        "full_product_complexity": "low",
        "mvp_complexity": "low",
        "mvp_feasibility_score": 85,
        "opportunity_score": 92,
        "total_daily_installs": 90000,
        "weekly_growth_percent": 40,
        "monthly_growth_percent": 80,
        "history_depth_days": 14,
        "app_count": 4,
        "successful_new_apps_count": 2,
        "unique_developer_count": 3,
        "giant_developer_share": 0.0,
        "single_developer_share": 0.4,
        "top_app_share": 0.42,
        "top3_app_share": 0.78,
        "growth_by_one_app_share": 0.3,
        "advertised_top_app_share": 0.1,
        "classification_confidence_avg": 0.82,
        "data_quality_score": 86,
        "risk_tags": [],
        "reason_codes": ["high_demand"],
        "top_apps": [
            {"app_id": "a", "developer_name": "A Studio", "downloads_daily": 40000},
            {"app_id": "b", "developer_name": "B Studio", "downloads_daily": 30000},
            {"app_id": "c", "developer_name": "C Studio", "downloads_daily": 20000},
        ],
    }
    row.update(overrides)
    return row


class AlertRankerTests(unittest.TestCase):
    def test_healthy_candidate_gets_explainable_sendable_score(self):
        config, _ = load_config("config.yaml")

        enriched = enrich_sendable_alert_fields([candidate()], config)[0]

        self.assertGreaterEqual(enriched["sendable_alert_score"], 80)
        self.assertGreaterEqual(enriched["trend_confidence_score"], 65)
        self.assertGreaterEqual(enriched["team_fit_score"], 60)
        self.assertIn("final", enriched["sendable_score_components"])
        self.assertIn("qualified_alert_candidate", enriched["sendable_alert_reasons"])
        self.assertEqual(enriched["sendable_alert_failures"], [])

    def test_public_score_function_is_deterministic(self):
        config, _ = load_config("config.yaml")

        first = calculate_sendable_alert_score(candidate(), config)
        second = calculate_sendable_alert_score(candidate(), config)

        self.assertEqual(first, second)

    def test_severe_paid_spike_blocks_hard_filters(self):
        config, _ = load_config("config.yaml")
        enriched = enrich_sendable_alert_fields(
            [candidate(risk_tags=["severe_paid_spike"], advertised_top_app_share=0.8)],
            config,
        )[0]

        passed, failures = passes_sendable_hard_filters(enriched, config)

        self.assertFalse(passed)
        self.assertIn("blocked_risk_tag", failures)
        self.assertIn("organic_confidence_low", failures)

    def test_mixed_unknown_cluster_is_soft_penalty_not_hard_blocker(self):
        config, _ = load_config("config.yaml")
        enriched = enrich_sendable_alert_fields(
            [
                candidate(
                    mixed_unknown_cluster=True,
                    unknown_dominant_cluster=False,
                    unknown_pattern_blocker_active=False,
                    unknown_app_share=0.1,
                    unknown_installs_share=0.08,
                    risk_tags=["mixed_unknown_cluster"],
                )
            ],
            config,
        )[0]

        passed, failures = passes_sendable_hard_filters(enriched, config)

        self.assertTrue(passed)
        self.assertNotIn("unknown_pattern_blocker_active", failures)
        self.assertEqual(enriched["sendable_score_components"]["unknown_app_share"], 0.1)
        self.assertEqual(enriched["sendable_score_components"]["unknown_installs_share"], 0.08)

    def test_unknown_pattern_blocker_active_blocks_sendable_alert(self):
        config, _ = load_config("config.yaml")
        enriched = enrich_sendable_alert_fields(
            [
                candidate(
                    unknown_dominant_cluster=True,
                    unknown_pattern_blocker_active=True,
                    unknown_or_new_pattern_cluster=True,
                    unknown_app_share=0.7,
                    unknown_installs_share=0.72,
                    classification_confidence_avg=0.62,
                    risk_tags=["unknown_dominant_cluster"],
                )
            ],
            config,
        )[0]

        passed, failures = passes_sendable_hard_filters(enriched, config)

        self.assertFalse(passed)
        self.assertIn("unknown_pattern_blocker_active", failures)
        self.assertEqual(enriched["first_blocking_failure"], "unknown_pattern_blocker_active")
        self.assertIn("classification_confidence_for_unknown_blocker", enriched["sendable_threshold_margins"])

    def test_hard_and_soft_blockers_are_separated(self):
        config, _ = load_config("config.yaml")
        enriched = enrich_sendable_alert_fields(
            [
                candidate(
                    data_quality_score=58,
                    top_app_share=0.7,
                    risk_tags=["weak_revenue_signal"],
                )
            ],
            config,
        )[0]

        self.assertIn("data_quality_below_hard_min", enriched["hard_blockers"])
        self.assertIn("top_app_too_dominant", enriched["soft_blockers"])
        self.assertIn("weak_revenue_signal", enriched["soft_blockers"])
        self.assertGreater(enriched["hard_blockers_count"], 0)
        self.assertGreater(enriched["soft_blockers_count"], 0)

    def test_alert_strength_strong_candidate(self):
        config, _ = load_config("config.yaml")
        enriched = enrich_sendable_alert_fields([candidate()], config)[0]

        self.assertEqual(enriched["alert_strength"], "STRONG_ALERT")


if __name__ == "__main__":
    unittest.main()
