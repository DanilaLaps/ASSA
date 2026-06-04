import unittest

from appstorespy_niche_monitor.appstorespy_client import AppStoreSpyError
from appstorespy_niche_monitor.collector import (
    APPSTORESPY_ALLOWED_LANGUAGES,
    build_play_query,
    normalize_appstorespy_language,
    parse_unknown_fields,
    query_play_apps_with_field_fallback,
)
from appstorespy_niche_monitor.config import load_config


class FakeClient:
    def __init__(self):
        self.calls = []

    def query_play_apps(self, query):
        self.calls.append(list(query["fields"]))
        if len(self.calls) == 1:
            raise AppStoreSpyError(
                'AppStoreSpy HTTP 400: {"errors":[{"location":"fields","message":"Unknown fields","value":["ads"]}]}'
            )
        return {"apps": []}


class CollectorTests(unittest.TestCase):
    def test_default_play_query_does_not_request_description(self):
        config, _ = load_config("config.yaml")

        query = build_play_query(config, "BR", "GAME_PUZZLE", "-downloads_daily", 1)

        self.assertNotIn("description", query["fields"])
        self.assertIn("downloads_daily", query["fields"])

    def test_configured_languages_are_valid_for_appstorespy(self):
        config, _ = load_config("config.yaml")

        for country in config["countries"]:
            query = build_play_query(config, country, "GAME_PUZZLE", "-downloads_daily", 1)
            self.assertIn(query["language"], APPSTORESPY_ALLOWED_LANGUAGES, country)

    def test_language_aliases_match_appstorespy_enum(self):
        self.assertEqual(normalize_appstorespy_language("es_MX"), "es_419")
        self.assertEqual(normalize_appstorespy_language("en_IN"), "en_US")
        self.assertEqual(normalize_appstorespy_language("id_ID"), "en_US")
        self.assertEqual(normalize_appstorespy_language("th_TH"), "en_US")
        self.assertEqual(normalize_appstorespy_language("vi_VN"), "vi")

    def test_parse_unknown_fields_from_appstorespy_error(self):
        fields = parse_unknown_fields(
            'AppStoreSpy HTTP 400: {"errors":[{"location":"fields","message":"Unknown fields","value":["description"]}]}'
        )

        self.assertEqual(fields, ["description"])

    def test_query_fallback_removes_unknown_fields_and_retries_once(self):
        client = FakeClient()
        query = {"fields": ["id", "name", "ads"]}

        result = query_play_apps_with_field_fallback(client, query)

        self.assertEqual(result, {"apps": []})
        self.assertEqual(client.calls, [["id", "name", "ads"], ["id", "name"]])
        self.assertEqual(query["removed_unknown_fields"], ["ads"])


if __name__ == "__main__":
    unittest.main()
