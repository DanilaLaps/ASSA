from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


class AppStoreSpyError(RuntimeError):
    """Raised when AppStoreSpy returns an unrecoverable response."""


class AppStoreSpyClient:
    def __init__(self, api_key: str | None = None, base_url: str = "https://api.appstorespy.com/v1"):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key or os.environ.get("APPSTORESPY_API_KEY")
        if not self.api_key:
            raise AppStoreSpyError("APPSTORESPY_API_KEY is required in production mode.")

    def _request(
        self,
        method: str,
        path: str,
        *,
        json_body: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        timeout: int = 60,
    ) -> Any:
        query = urllib.parse.urlencode(params or {}, doseq=True)
        url = f"{self.base_url}{path}"
        if query:
            url = f"{url}?{query}"
        body = json.dumps(json_body).encode("utf-8") if json_body is not None else None
        headers = {
            "accept": "application/json",
            "API-KEY": self.api_key or "",
            "content-type": "application/json",
        }
        last_error: Exception | None = None
        for attempt in range(4):
            request = urllib.request.Request(url, data=body, method=method, headers=headers)
            try:
                with urllib.request.urlopen(request, timeout=timeout) as response:
                    if response.status == 202:
                        return {"status": "crawling"}
                    if response.status == 204:
                        return None
                    raw = response.read().decode("utf-8")
                    return json.loads(raw) if raw else None
            except urllib.error.HTTPError as exc:
                last_error = exc
                if exc.code == 202:
                    return {"status": "crawling"}
                if exc.code in (429, 500, 502, 503, 504):
                    if attempt < 3:
                        time.sleep(2**attempt)
                    continue
                detail = exc.read().decode("utf-8", errors="replace")
                raise AppStoreSpyError(f"AppStoreSpy HTTP {exc.code}: {redact_secret(detail, self.api_key)}") from exc
            except urllib.error.URLError as exc:
                last_error = exc
                if attempt < 3:
                    time.sleep(2**attempt)
        raise AppStoreSpyError(f"AppStoreSpy request failed after retries: {redact_secret(last_error, self.api_key)}")

    def query_play_apps(self, payload: dict[str, Any]) -> dict[str, Any]:
        result = self._request("POST", "/play/apps/query", json_body=payload)
        if not isinstance(result, dict):
            return {"apps": []}
        return result

    def get_play_estimates(self, app_ids: list[str], start: str, end: str) -> dict[str, Any]:
        result = self._request(
            "GET",
            "/play/estimates",
            params={"id": ",".join(app_ids), "start": start, "end": end},
        )
        if not isinstance(result, dict):
            return {}
        return result


def redact_secret(value: Any, secret: str | None) -> str:
    text = str(value)
    if secret:
        text = text.replace(secret, "[REDACTED]")
    return text
