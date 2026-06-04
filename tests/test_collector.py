import unittest

from appstorespy_niche_monitor.collector import (
    build_single_query_payload,
    collect_apps,
    validate_single_query_payload,
)
from appstorespy_niche_monitor.config import load_config


class FakeClient:
    def __init__(self):
        self.calls = []

    def query_play_apps(self, query, *, timeout=60):
        self.calls.append({"query": query, "timeout": timeout})
        return {"apps": [{"id": "com.example.game", "name": "Example Game"}]}


class CollectorTests(unittest.TestCase):
    def test_single_query_payload_matches_appstorespy_contract(self):
        config, _ = load_config("config.yaml")

        payload = build_single_query_payload(config, "2026-06-04")

        self.assertEqual(payload["limit"], 10000)
        self.assertEqual(payload["page"], 1)
        self.assertEqual(payload["sort"], "-release_date")
        self.assertNotIn("country", payload)
        self.assertNotIn("language", payload)
        self.assertNotIn("active_countries", payload)
        self.assertNotIn("active_countries", payload.get("filter", {}))
        self.assertEqual(payload["filter"]["published"], True)
        self.assertEqual(payload["filter"]["category_type"], "GAME")
        self.assertEqual(payload["filter"]["release_date"]["gte"], "2025-12-06")
        self.assertEqual(payload["filter"]["downloads_daily"]["gte"], 500)
        self.assertIn("description_short", payload["fields"])
        self.assertIn("description_full", payload["fields"])

    def test_collect_apps_calls_appstorespy_once_in_production(self):
        config, config_dir = load_config("config.yaml")
        client = FakeClient()

        records = collect_apps(config, config_dir, mode="production", snapshot_date="2026-06-04", client=client)

        self.assertEqual(len(client.calls), 1)
        self.assertEqual(client.calls[0]["timeout"], 180)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["api_requests_count"], 1)
        self.assertEqual(records[0]["collection_mode"], "single_query")

    def test_validation_rejects_forbidden_dimensions(self):
        config, _ = load_config("config.yaml")
        payload = build_single_query_payload(config, "2026-06-04")
        payload["language"] = "en_US"

        with self.assertRaises(ValueError):
            validate_single_query_payload(payload, config)

    def test_config_has_no_multi_query_axes(self):
        config, _ = load_config("config.yaml")

        for key in ("countries", "languages", "categories", "sorts", "collection_limits"):
            self.assertNotIn(key, config)
        self.assertEqual(config["collection"]["mode"], "single_query")
        self.assertFalse(config["collection"]["include_country"])
        self.assertFalse(config["collection"]["include_language"])
        self.assertFalse(config["collection"]["include_active_countries"])
        self.assertFalse(config["collection"]["allow_pagination"])
        self.assertEqual(config["collection"]["max_api_requests_per_run"], 1)


if __name__ == "__main__":
    unittest.main()
