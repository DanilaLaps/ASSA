import unittest

from appstorespy_niche_monitor.cleaner import clean_apps


class CleanerTests(unittest.TestCase):
    def test_dedupes_without_country_dimension(self):
        raw_records = [
            {
                "platform": "google_play",
                "response": {
                    "apps": [
                        {
                            "id": "a1",
                            "bundle": "com.example.sort",
                            "name": "Sort One",
                            "country": "BR",
                            "downloads_daily": 500,
                        },
                        {
                            "id": "a2",
                            "bundle": "com.example.sort",
                            "name": "Sort One",
                            "country": "US",
                            "downloads_daily": 900,
                        },
                    ]
                },
            }
        ]

        apps = clean_apps(raw_records, "2026-06-04")

        self.assertEqual(len(apps), 1)
        self.assertEqual(apps[0]["downloads_daily"], 900)
        self.assertEqual(apps[0]["response_country"], "US")

    def test_normalizes_single_query_fields(self):
        raw_records = [
            {
                "platform": "google_play",
                "response": {
                    "apps": [
                        {
                            "id": "a1",
                            "bundle": "com.example.sort",
                            "developer_id": "dev1",
                            "description_short": "Short",
                            "description_full": "Full sort puzzle description",
                            "downloads_mark": "10K+",
                            "advertised": "false",
                            "ads": "true",
                            "url": "https://play.google.com/store/apps/details?id=com.example.sort",
                            "website": "https://example.com",
                        }
                    ]
                },
            }
        ]

        app = clean_apps(raw_records, "2026-06-04")[0]

        self.assertEqual(app["bundle"], "com.example.sort")
        self.assertEqual(app["developer_id"], "dev1")
        self.assertEqual(app["description"], "Full sort puzzle description")
        self.assertEqual(app["downloads_mark"], "10K+")
        self.assertFalse(app["advertised"])
        self.assertTrue(app["ads"])
        self.assertIn("play.google.com", app["url"])
        self.assertEqual(app["website"], "https://example.com")
        self.assertIn("raw_source_fields_json", app)


if __name__ == "__main__":
    unittest.main()
