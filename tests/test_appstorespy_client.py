import io
import json
import unittest
import urllib.error
from unittest.mock import patch

from appstorespy_niche_monitor.appstorespy_client import AppStoreSpyClient, AppStoreSpyError


class FakeResponse:
    def __init__(self, status, body=""):
        self.status = status
        self.body = body.encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self):
        return self.body


def http_error(code, body):
    return urllib.error.HTTPError(
        url="https://api.appstorespy.com/v1/play/apps/query",
        code=code,
        msg="error",
        hdrs=None,
        fp=io.BytesIO(body.encode("utf-8")),
    )


class AppStoreSpyClientTests(unittest.TestCase):
    def test_202_returns_crawling_status(self):
        client = AppStoreSpyClient(api_key="secret-token")
        with patch("urllib.request.urlopen", return_value=FakeResponse(202)):
            result = client.query_play_apps({"limit": 1})

        self.assertEqual(result, {"status": "crawling"})

    def test_204_returns_empty_apps_for_query(self):
        client = AppStoreSpyClient(api_key="secret-token")
        with patch("urllib.request.urlopen", return_value=FakeResponse(204)):
            result = client.query_play_apps({"limit": 1})

        self.assertEqual(result, {"apps": []})

    def test_429_retries_then_returns_json(self):
        client = AppStoreSpyClient(api_key="secret-token")
        response = FakeResponse(200, json.dumps({"apps": [{"id": "app"}]}))
        with patch("urllib.request.urlopen", side_effect=[http_error(429, "rate limit"), response]):
            with patch("time.sleep") as sleep:
                result = client.query_play_apps({"limit": 1})

        self.assertEqual(result["apps"][0]["id"], "app")
        sleep.assert_called_once()

    def test_403_raises_without_leaking_api_key(self):
        client = AppStoreSpyClient(api_key="secret-token")
        with patch("urllib.request.urlopen", side_effect=http_error(403, "bad key secret-token")):
            with self.assertRaises(AppStoreSpyError) as ctx:
                client.query_play_apps({"limit": 1})

        self.assertIn("[REDACTED]", str(ctx.exception))
        self.assertNotIn("secret-token", str(ctx.exception))

    def test_5xx_retries_and_raises_after_limit(self):
        client = AppStoreSpyClient(api_key="secret-token")
        with patch("urllib.request.urlopen", side_effect=http_error(503, "down")):
            with patch("time.sleep") as sleep:
                with self.assertRaises(AppStoreSpyError):
                    client.query_play_apps({"limit": 1})

        self.assertEqual(sleep.call_count, 3)


if __name__ == "__main__":
    unittest.main()
