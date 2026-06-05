import unittest

from appstorespy_niche_monitor.main import build_alert_funnel


def candidate(**overrides):
    row = {
        "candidate_id": "candidate-1",
        "status": "ALERT",
        "alert_stage": "QUALIFIED_CANDIDATE_ONLY",
        "send_regular_alert": False,
        "sendable_alert_score": 67.0,
        "opportunity_score": 74.0,
        "trend_confidence_score": 54.0,
        "team_fit_score": 61.0,
        "data_quality_score": 70.0,
        "classification_confidence_avg": 0.72,
        "mvp_feasibility_score": 85.0,
        "top_app_share": 0.58,
        "top3_app_share": 0.82,
        "growth_by_one_app_share": 0.35,
        "advertised_top_app_share": 0.1,
        "organic_confidence": "MEDIUM",
        "first_blocking_failure": "below_sendable_alert_score",
        "sendable_alert_failures": ["below_sendable_alert_score", "below_trend_confidence_score"],
        "alert_strength": "MEDIUM_ALERT",
    }
    row.update(overrides)
    return row


class AlertFunnelTests(unittest.TestCase):
    def test_sendable_failure_distribution_written(self):
        funnel = build_alert_funnel(
            [candidate()],
            urgent_alerts=[],
            watch=[],
            near_misses=[],
            rejected=[],
            summaries=[],
            filter_diagnostics={
                "candidates_before_market_signal_dedupe": 1,
                "candidates_after_market_signal_dedupe": 1,
                "status_counts_before_dedupe": {"ALERT": 1},
                "status_counts_after_dedupe": {"ALERT": 1},
                "sendable_hard_filter_pass_count": 0,
                "sendable_hard_filter_fail_count": 1,
                "sendable_hard_filter_denominator": 1,
            },
        )

        self.assertEqual(funnel["blocked_alert_first_blocking_failure_counts"]["below_sendable_alert_score"], 1)
        self.assertEqual(funnel["blocked_alert_sendable_failure_counts"]["below_trend_confidence_score"], 1)
        self.assertIn("sendable_alert_score", funnel["blocked_alert_metric_stats"])
        self.assertEqual(funnel["blocked_alert_organic_confidence_distribution"]["MEDIUM"], 1)

    def test_status_counts_reconcile_with_single_app_watch(self):
        rows = [
            candidate(status="ALERT"),
            candidate(candidate_id="watch", status="WATCH"),
            candidate(candidate_id="single", status="SINGLE_APP_WATCH"),
            candidate(candidate_id="near", status="NEAR_MISS"),
            candidate(candidate_id="reject", status="REJECT"),
        ]
        funnel = build_alert_funnel(rows, [], [rows[1], rows[2]], [rows[3]], [rows[4]], summaries=[])

        self.assertEqual(funnel["status_counts"]["SINGLE_APP_WATCH"], 1)
        self.assertEqual(sum(funnel["status_counts"].values()), funnel["candidates_count"])
        self.assertEqual(funnel["watch_count"], 1)
        self.assertEqual(funnel["watch_like_count"], 2)


if __name__ == "__main__":
    unittest.main()
