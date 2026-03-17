from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any, Callable, Optional, Union
from urllib.parse import urlparse

import httpx

from .types import BeforeRequestContext, BeforeRequestHook


_DEFAULT_REFRESH_URL = "https://auth.squadcast.com/oauth/access-token"
_REFRESH_PATH = "/oauth/access-token"
_EXPIRY_SKEW = timedelta(seconds=30)


@dataclass
class _CachedAccessToken:
    token: str
    expiry: datetime


class _AccessTokenCache:
    _token: Optional[_CachedAccessToken]

    def __init__(self) -> None:
        self._token = None

    def get(self) -> Optional[str]:
        if self._token is None:
            return None

        if datetime.now(timezone.utc) >= self._token.expiry:
            self._token = None
            return None

        return self._token.token

    def set(self, token: str, expiry: datetime) -> None:
        self._token = _CachedAccessToken(token=token, expiry=expiry)


class AccessTokenHook(BeforeRequestHook):
    def __init__(self) -> None:
        self._cache = _AccessTokenCache()

    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> Union[httpx.Request, Exception]:
        refresh_token = _extract_refresh_token(hook_ctx.security_source)
        if not refresh_token:
            return request

        cached_token = self._cache.get()
        if cached_token:
            request.headers["Authorization"] = f"Bearer {cached_token}"
            return request

        refresh_url = _resolve_refresh_url(hook_ctx.base_url, request.url)

        try:
            token, expiry = _fetch_access_token(refresh_url, refresh_token)
        except Exception as exc:  # pragma: no cover - passthrough to generated flow
            return exc

        self._cache.set(token, expiry)
        request.headers["Authorization"] = f"Bearer {token}"
        return request


def _extract_refresh_token(
    source: Optional[Union[Any, Callable[[], Any]]],
) -> Optional[str]:
    if source is None:
        return None

    raw = source() if callable(source) else source
    if isinstance(raw, str) and raw:
        return raw

    if raw is None:
        return None

    refresh_token = getattr(raw, "refresh_token_auth", None)
    if isinstance(refresh_token, str) and refresh_token:
        return refresh_token

    refresh_token = getattr(raw, "refreshToken", None)
    if isinstance(refresh_token, str) and refresh_token:
        return refresh_token

    refresh_token = getattr(raw, "bearer_auth", None)
    if isinstance(refresh_token, str) and refresh_token:
        return refresh_token

    return None


def _resolve_refresh_url(base_url: str, request_url: httpx.URL) -> str:
    for candidate in (base_url, str(request_url)):
        if not candidate:
            continue

        parsed = urlparse(candidate)
        auth_host = _auth_host_for_api_host(parsed.hostname or "")
        if not auth_host:
            continue

        return f"https://{auth_host}{_REFRESH_PATH}"

    return _DEFAULT_REFRESH_URL


def _auth_host_for_api_host(api_host: str) -> str:
    normalized_host = api_host.strip().lower()
    if not normalized_host:
        return ""

    if normalized_host.startswith("api."):
        return f"auth.{normalized_host[4:]}"

    return "auth.squadcast.com"


def _fetch_access_token(refresh_url: str, refresh_token: str) -> tuple[str, datetime]:
    response = httpx.get(
        refresh_url,
        headers={
            "Accept": "application/json",
            "X-Refresh-Token": refresh_token,
        },
        follow_redirects=True,
    )
    response.raise_for_status()

    payload = response.json()
    data = payload.get("data") if isinstance(payload, dict) else None
    if not isinstance(data, dict):
        raise ValueError("squadcast-sdk: invalid refresh token response payload")

    token = data.get("access_token")
    if not isinstance(token, str) or not token:
        raise ValueError("squadcast-sdk: empty access_token in refresh response")

    expires_at = data.get("expires_at")
    if isinstance(expires_at, (int, float)):
        expiry = datetime.fromtimestamp(expires_at, tz=timezone.utc) - _EXPIRY_SKEW
    else:
        expiry = datetime.now(timezone.utc)

    return token, expiry