import unittest

from appstorespy_niche_monitor.coverage import build_coverage_metadata


class CoverageTests(unittest.TestCase):
    def test_total_count_within_limit_is_full_window(self):
        coverage = build_coverage_metadata({"data": [{"id": "a"}], "total_count": 1}, {"limit": 10000}, {})

        self.assertFalse(coverage["sample_truncated"])
        self.assertTrue(coverage["full_window_claim_allowed"])

    def test_total_count_over_limit_is_truncated(self):
        coverage = build_coverage_metadata({"data": [{"id": "a"}], "total_count": 10001}, {"limit": 10000}, {})

        self.assertTrue(coverage["sample_truncated"])
        self.assertFalse(coverage["full_window_claim_allowed"])
        self.assertEqual(coverage["coverage_ratio"], 0.0001)

    def test_missing_total_count_is_unknown(self):
        coverage = build_coverage_metadata({"data": [{"id": "a"}]}, {"limit": 10000}, {})

        self.assertEqual(coverage["sample_truncated"], "unknown")
        self.assertFalse(coverage["full_window_claim_allowed"])


if __name__ == "__main__":
    unittest.main()
