import unittest

from appstorespy_niche_monitor.aggregator import aggregate_apps, stable_key
from appstorespy_niche_monitor.config import load_config


def app(**overrides):
    row = {
        "snapshot_date": "2026-06-04",
        "platform": "google_play",
        "country": "BR",
        "app_id": "com.example.sort",
        "bundle": "com.example.sort",
        "name": "Goods Sort",
        "developer_name": "Tiny Team",
        "developer_id": "dev1",
        "category": "GAME_PUZZLE",
        "niche": "sort puzzle",
        "normalized_niche": "sort_puzzle",
        "market_category": "puzzle",
        "core_mechanic": "sort",
        "theme": "supermarket",
        "meta": "collection",
        "audience": "women_25_45",
        "production_complexity": "low",
        "downloads_daily": 3000,
        "downloads_month": 90000,
        "revenue_month": 1000,
        "rating_avg": 4.4,
        "release_date": "2026-04-01",
        "update_date": "2026-05-01",
        "advertised": False,
        "ads": True,
        "url_appstorespy": "https://appstorespy.example/apps/com.example.sort",
        "description_short": "Sort goods on supermarket shelves.",
        "description_full": "A sorting puzzle about arranging goods on supermarket shelves.",
        "icon": "https://cdn.example/icon.png",
        "screenshots": ["one.png", "two.png", "three.png", "four.png"],
    }
    row.update(overrides)
    return row


class AggregatorTests(unittest.TestCase):
    def test_group_key_excludes_country(self):
        base = app(country="BR")
        other_country = app(country="US")

        self.assertEqual(stable_key(base), stable_key(other_country))
        self.assertNotIn("BR", stable_key(base))

    def test_aggregates_single_query_scope_without_country_dimension(self):
        config, _ = load_config("config.yaml")

        summary = aggregate_apps(
            [
                app(country="BR", app_id="a", bundle="a", downloads_daily=3000),
                app(country="US", app_id="b", bundle="b", downloads_daily=2500, advertised=True),
            ],
            config,
            "2026-06-04",
        )[0]

        self.assertEqual(summary["app_count"], 2)
        self.assertEqual(summary["total_daily_installs"], 5500)
        self.assertIn(summary["group_key_type"], config["aggregation"]["group_keys"])
        self.assertEqual(summary["release_date_window"], "last_180d")
        self.assertEqual(summary["source_scope"], "single_appstorespy_query_no_country_language")
        self.assertNotIn("country", summary["group_key"])
        self.assertNotIn("women_25_45", summary["group_key"])
        self.assertEqual(summary["audience"], "women_25_45")
        self.assertEqual(summary["top_apps"][0]["bundle"], "a")
        self.assertEqual(summary["top_apps"][0]["url_appstorespy"], "https://appstorespy.example/apps/com.example.sort")
        self.assertEqual(summary["top_apps"][0]["description_short"], "Sort goods on supermarket shelves.")
        self.assertEqual(summary["top_apps"][0]["screenshots"], ["one.png", "two.png", "three.png"])
        self.assertGreater(summary["advertised_top_app_share"], 0)


if __name__ == "__main__":
    unittest.main()
