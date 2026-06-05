import unittest

from appstorespy_niche_monitor.candidate_generator import generate_candidates
from appstorespy_niche_monitor.config import load_config


def summary(**overrides):
    row = {
        "snapshot_date": "2026-06-04",
        "score_version": "v1.3.2",
        "normalized_niche": "goods_sorting_supermarket",
        "group_key_type": "normalized_niche",
        "group_key_value": "goods_sorting_supermarket",
        "market_category": "puzzle",
        "core_mechanic": "sort",
        "theme": "supermarket",
        "meta": "collection",
        "audience_summary": "women_25_45:2",
        "app_count": 2,
        "total_daily_installs": 6000,
        "successful_new_apps_count": 1,
        "top_apps": [
            {"app_id": "a", "developer_name": "A Studio", "downloads_daily": 3500},
            {"app_id": "b", "developer_name": "B Studio", "downloads_daily": 2500},
        ],
        "top_app_share": 0.58,
        "giant_developer_share": 0,
        "opportunity_score": 75,
        "data_quality_score": 70,
        "mvp_feasibility_score": 70,
        "risk_tags": [],
        "reason_codes": ["multi_app_cluster"],
        "severe_paid_spike_risk": False,
    }
    row.update(overrides)
    return row


class CandidateGeneratorTests(unittest.TestCase):
    def test_single_app_breakout_gets_single_app_watch(self):
        config, _ = load_config("config.yaml")

        candidates = generate_candidates(
            [
                summary(
                    app_count=1,
                    total_daily_installs=3500,
                    successful_new_apps_count=1,
                    opportunity_score=55,
                    top_apps=[{"app_id": "solo", "downloads_daily": 3500}],
                    top_app_share=1.0,
                )
            ],
            config,
            "2026-06-04",
        )

        self.assertEqual(candidates[0]["status"], "SINGLE_APP_WATCH")
        self.assertIn("single_app_breakout", candidates[0]["reason_codes"])

    def test_leader_dominated_candidate_is_near_miss_not_alert(self):
        config, _ = load_config("config.yaml")

        candidates = generate_candidates([summary(top_app_share=0.8, risk_tags=["leader_dominated"])], config, "2026-06-04")

        self.assertEqual(candidates[0]["status"], "NEAR_MISS")
        self.assertIn("leader_dominated", candidates[0]["risk_tags"])
        self.assertIn("top_app_too_dominant", candidates[0]["failed_alert_conditions"])

    def test_alert_candidate_has_sendable_stage_defaults(self):
        config, _ = load_config("config.yaml")

        candidates = generate_candidates([summary()], config, "2026-06-04")

        self.assertEqual(candidates[0]["status"], "ALERT")
        self.assertEqual(candidates[0]["alert_stage"], "QUALIFIED_CANDIDATE")
        self.assertFalse(candidates[0]["send_regular_alert"])
        self.assertIn("sendable_alert_score", candidates[0])
        self.assertIn("sendable_alert_reasons", candidates[0])

    def test_near_miss_is_preserved(self):
        config, _ = load_config("config.yaml")

        candidates = generate_candidates([summary(opportunity_score=62, data_quality_score=60)], config, "2026-06-04")

        self.assertEqual(candidates[0]["status"], "NEAR_MISS")
        self.assertIn("weak_data_quality", candidates[0]["failed_alert_conditions"])

    def test_severe_paid_spike_rejects(self):
        config, _ = load_config("config.yaml")

        candidates = generate_candidates(
            [summary(severe_paid_spike_risk=True, risk_tags=["severe_paid_spike"])],
            config,
            "2026-06-04",
        )

        self.assertEqual(candidates[0]["status"], "REJECT")

    def test_mixed_unknown_cluster_does_not_block_alert_candidate(self):
        config, _ = load_config("config.yaml")

        candidates = generate_candidates(
            [
                summary(
                    mixed_unknown_cluster=True,
                    unknown_dominant_cluster=False,
                    unknown_pattern_blocker_active=False,
                    unknown_or_new_pattern_cluster=False,
                    unknown_app_count=1,
                    unknown_app_share=0.1,
                    unknown_installs_share=0.08,
                    reason_codes=["multi_app_cluster", "new_pattern_detected"],
                )
            ],
            config,
            "2026-06-04",
        )

        self.assertEqual(candidates[0]["status"], "ALERT")
        self.assertIn("mixed_unknown_cluster", candidates[0]["risk_tags"])
        self.assertNotIn("unknown_pattern_blocker_active", candidates[0]["failed_alert_conditions"])
        self.assertNotIn("new_pattern_detected", candidates[0]["reason_codes"])

    def test_unknown_pattern_blocker_active_blocks_alert_candidate(self):
        config, _ = load_config("config.yaml")

        candidates = generate_candidates(
            [
                summary(
                    app_count=4,
                    total_daily_installs=12000,
                    successful_new_apps_count=2,
                    unique_developer_count=2,
                    opportunity_score=82,
                    data_quality_score=82,
                    mixed_unknown_cluster=True,
                    unknown_dominant_cluster=True,
                    unknown_pattern_blocker_active=True,
                    unknown_or_new_pattern_cluster=True,
                    unknown_app_count=3,
                    unknown_app_share=0.75,
                    unknown_installs_share=0.72,
                    classification_confidence_avg=0.62,
                )
            ],
            config,
            "2026-06-04",
        )

        self.assertNotEqual(candidates[0]["status"], "ALERT")
        self.assertIn("unknown_dominant_cluster", candidates[0]["risk_tags"])
        self.assertIn("unknown_pattern_blocker_active", candidates[0]["failed_alert_conditions"])


if __name__ == "__main__":
    unittest.main()
