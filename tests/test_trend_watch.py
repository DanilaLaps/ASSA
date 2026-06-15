import unittest

from appstorespy_niche_monitor.config import load_config
from appstorespy_niche_monitor.trend_watch import mark_trend_watch_sent, select_trend_watch, trend_watch_key


def candidate(index: int, **overrides):
    row = {
        "candidate_id": f"candidate-{index}",
        "status": "ALERT",
        "dedupe_key": f"dedupe-{index}",
        "normalized_niche": f"niche_{index}",
        "market_category": "puzzle",
        "core_mechanic": "match",
        "theme": "abstract",
        "meta": "levels",
        "audience": "women_25_45",
        "production_complexity": "medium",
        "full_product_complexity": "medium",
        "mvp_complexity": "medium",
        "mvp_feasibility_score": 65,
        "opportunity_score": 74,
        "sendable_alert_score": 69,
        "trend_confidence_score": 70,
        "team_fit_score": 58,
        "organic_confidence": "HIGH",
        "weekly_growth_percent": 35,
        "monthly_growth_percent": 60,
        "history_depth_days": 7,
        "app_count": 8,
        "successful_new_apps_count": 2,
        "unique_developer_count": 4,
        "total_daily_installs": 50000,
        "top_app_share": 0.35,
        "top3_app_share": 0.65,
        "growth_by_one_app_share": 0.4,
        "advertised_top_app_share": 0.0,
        "classification_confidence_avg": 0.72,
        "data_quality_score": 82,
        "risk_tags": [],
        "reason_codes": ["fresh_traction"],
        "send_regular_alert": False,
        "alert_stage": "QUALIFIED_CANDIDATE_ONLY",
        "top_apps": [
            {"app_id": f"{index}-a", "developer_name": "A Studio", "downloads_daily": 22000},
            {"app_id": f"{index}-b", "developer_name": "B Studio", "downloads_daily": 18000},
            {"app_id": f"{index}-c", "developer_name": "C Studio", "downloads_daily": 10000},
        ],
    }
    row.update(overrides)
    return row


class TrendWatchTests(unittest.TestCase):
    def test_selects_one_strong_growth_candidate_without_regular_alert_flag(self):
        config, _ = load_config("config.yaml")
        enriched, selected = select_trend_watch(
            [
                candidate(1, normalized_niche="stable", weekly_growth_percent=-5, monthly_growth_percent=0),
                candidate(2, normalized_niche="growing", weekly_growth_percent=45, monthly_growth_percent=90),
            ],
            config,
            {},
            "2026-06-04",
        )

        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0]["normalized_niche"], "growing")
        self.assertTrue(selected[0]["send_trend_watch"])
        self.assertFalse(selected[0]["send_regular_alert"])
        self.assertEqual(selected[0]["trend_watch_stage"], "TREND_WATCH")
        self.assertIn("trend_watch_selected", selected[0]["reason_codes"])
        self.assertEqual(sum(1 for item in enriched if item.get("send_trend_watch")), 1)

    def test_trend_watch_respects_own_cooldown(self):
        config, _ = load_config("config.yaml")
        item = candidate(1, normalized_niche="growing", weekly_growth_percent=45, monthly_growth_percent=90)
        enriched, selected = select_trend_watch(
            [item],
            config,
            {
                trend_watch_key(item): {
                    "normalized_niche": "growing",
                    "last_sent_at": "2026-06-03T10:00:00+00:00",
                }
            },
            "2026-06-04",
        )

        self.assertEqual(selected, [])
        self.assertTrue(
            any(str(failure).startswith("trend_watch_cooldown") for failure in enriched[0]["trend_watch_failures"])
        )
        self.assertFalse(enriched[0]["send_trend_watch"])

    def test_mark_trend_watch_sent_writes_separate_state(self):
        item = candidate(1, normalized_niche="growing")
        item["send_trend_watch"] = True
        item["trend_watch_stage"] = "TREND_WATCH"
        item["trend_watch_instance_id"] = "2026-06-04:trend_watch:growing"

        updated = mark_trend_watch_sent({}, [item], "2026-06-04")

        self.assertIn("trend_watch:growing", updated)
        self.assertEqual(updated["trend_watch:growing"]["normalized_niche"], "growing")
        self.assertEqual(updated["trend_watch:growing"]["last_trend_watch_instance_id"], item["trend_watch_instance_id"])


if __name__ == "__main__":
    unittest.main()
