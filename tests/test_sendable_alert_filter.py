import unittest

from appstorespy_niche_monitor.alert_filter import apply_cooldown_and_alert_limits, mark_sent, split_candidates
from appstorespy_niche_monitor.config import load_config


def alert_candidate(index: int, **overrides):
    mechanic = f"mechanic_{index}"
    row = {
        "candidate_id": f"candidate-{index}",
        "status": "ALERT",
        "dedupe_key": f"dedupe-{index}",
        "normalized_niche": f"niche_{index}",
        "market_category": "puzzle",
        "core_mechanic": mechanic,
        "theme": "supermarket",
        "meta": "collection",
        "production_complexity": "low",
        "full_product_complexity": "low",
        "mvp_complexity": "low",
        "mvp_feasibility_score": 85,
        "opportunity_score": 94 - index * 0.1,
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
            {"app_id": f"{index}-a", "developer_name": "A Studio", "downloads_daily": 40000},
            {"app_id": f"{index}-b", "developer_name": "B Studio", "downloads_daily": 30000},
            {"app_id": f"{index}-c", "developer_name": "C Studio", "downloads_daily": 20000},
        ],
    }
    row.update(overrides)
    return row


class SendableAlertFilterTests(unittest.TestCase):
    def test_only_sendable_alerts_get_regular_telegram_flag(self):
        config, _ = load_config("config.yaml")
        config["alert_limits"]["max_alerts_per_run"] = 5
        config["sendable_alert_rules"]["max_sendable_per_core_mechanic"] = 20
        candidates = [alert_candidate(index) for index in range(20)]

        filtered = apply_cooldown_and_alert_limits(candidates, config, {}, "2026-06-04")
        urgent_alerts, watch, near_misses, rejected, alert_candidates = split_candidates(filtered)

        self.assertEqual(len(alert_candidates), 20)
        self.assertEqual(len(urgent_alerts), 5)
        self.assertEqual(len(watch), 0)
        self.assertEqual(len(near_misses), 0)
        self.assertEqual(len(rejected), 0)
        self.assertTrue(all(item["send_regular_alert"] is True for item in urgent_alerts))
        self.assertTrue(all(item["alert_stage"] == "SENDABLE_ALERT" for item in urgent_alerts))
        self.assertLessEqual(len(urgent_alerts), config["alert_limits"]["max_alerts_per_run"])
        blocked = [item for item in filtered if "max_alerts_per_run_blocked" in item.get("sendable_alert_failures", [])]
        self.assertEqual(len(blocked), 15)

    def test_watch_and_near_miss_never_get_regular_alert(self):
        config, _ = load_config("config.yaml")
        candidates = [
            alert_candidate(1, status="WATCH"),
            alert_candidate(2, status="SINGLE_APP_WATCH"),
            alert_candidate(3, status="NEAR_MISS"),
        ]

        filtered = apply_cooldown_and_alert_limits(candidates, config, {}, "2026-06-04")

        self.assertTrue(all(item["send_regular_alert"] is False for item in filtered))
        self.assertTrue(all(item["alert_stage"] != "SENDABLE_ALERT" for item in filtered))

    def test_promote_best_clean_alert_when_no_sendable(self):
        config, _ = load_config("config.yaml")
        config["alert_limits"]["max_alerts_per_run"] = 3
        filtered = apply_cooldown_and_alert_limits(
            [
                alert_candidate(
                    1,
                    opportunity_score=78,
                    top_app_share=0.62,
                    sendable_alert_reasons=[],
                )
            ],
            config,
            {},
            "2026-06-04",
        )
        urgent_alerts, *_ = split_candidates(filtered)

        self.assertEqual(len(urgent_alerts), 1)
        self.assertTrue(urgent_alerts[0]["calibrated_promotion"])
        self.assertIn("promoted_best_clean_alert_when_no_sendable", urgent_alerts[0]["sendable_alert_reasons"])
        self.assertEqual(urgent_alerts[0]["hard_blockers_count"], 0)

    def test_no_promotion_with_hard_blocker(self):
        config, _ = load_config("config.yaml")
        filtered = apply_cooldown_and_alert_limits(
            [
                alert_candidate(
                    1,
                    data_quality_score=40,
                    top_app_share=0.62,
                )
            ],
            config,
            {},
            "2026-06-04",
        )
        urgent_alerts, *_ = split_candidates(filtered)
        blocked = filtered[0]

        self.assertEqual(len(urgent_alerts), 0)
        self.assertIn("data_quality_below_hard_min", blocked["hard_blockers"])

    def test_manual_review_digest_does_not_mark_sent(self):
        updated = mark_sent(
            {},
            [
                {
                    "dedupe_key": "manual-only",
                    "normalized_niche": "sort_puzzle",
                    "send_regular_alert": False,
                    "alert_stage": "MANUAL_REVIEW_ONLY",
                }
            ],
            "2026-06-04",
        )

        self.assertEqual(updated, {})


if __name__ == "__main__":
    unittest.main()
