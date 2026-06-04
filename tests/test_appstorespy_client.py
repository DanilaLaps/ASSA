import io
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

    def test_query_uses_custom_timeout(self):
        client = AppStoreSpyClient(api_key="secret-token")
        with patch("urllib.request.urlopen", return_value=FakeResponse(204)) as urlopen:
            client.query_play_apps({"limit": 10000}, timeout=180)

        self.assertEqual(urlopen.call_args.kwargs["timeout"], 180)

    def test_query_does_not_retry_429(self):
        client = AppStoreSpyClient(api_key="secret-token")
        with patch("urllib.request.urlopen", side_effect=http_error(429, "rate limit")):
            with patch("time.sleep") as sleep:
                with self.assertRaises(AppStoreSpyError):
                    client.query_play_apps({"limit": 1})

        sleep.assert_not_called()

    def test_403_raises_without_leaking_api_key(self):
        client = AppStoreSpyClient(api_key="secret-token")
        with patch("urllib.request.urlopen", side_effect=http_error(403, "bad key secret-token")):
            with self.assertRaises(AppStoreSpyError) as ctx:
                client.query_play_apps({"limit": 1})

        self.assertIn("[REDACTED]", str(ctx.exception))
        self.assertNotIn("secret-token", str(ctx.exception))

    def test_query_does_not_retry_5xx(self):
        client = AppStoreSpyClient(api_key="secret-token")
        with patch("urllib.request.urlopen", side_effect=http_error(503, "down")):
            with patch("time.sleep") as sleep:
                with self.assertRaises(AppStoreSpyError):
                    client.query_play_apps({"limit": 1})

        sleep.assert_not_called()


if __name__ == "__main__":
    unittest.main()
