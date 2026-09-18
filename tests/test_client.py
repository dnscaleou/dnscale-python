from __future__ import annotations

import asyncio
import pkgutil
from collections.abc import Callable
from typing import Any

import httpx
import pytest

import dnscale_api.api
from dnscale import APIError, DNScale, RateLimitError


def _zones_response() -> dict[str, Any]:
    return {
        "status": "success",
        "data": {
            "zones": [],
            "pagination": {
                "total": 0,
                "offset": 0,
                "limit": 10,
                "count": 0,
                "has_more": False,
            },
        },
    }


def _error_response(code: str = "TEST_ERROR", message: str = "request failed") -> dict[str, Any]:
    return {"status": "error", "error": {"code": code, "message": message}}


def _client(
    handler: Callable[[httpx.Request], httpx.Response],
    *,
    max_retries: int = 0,
) -> DNScale:
    return DNScale(
        "test-key",
        base_url="https://api.example.test/v1",
        max_retries=max_retries,
        retry_backoff=0,
        transport=httpx.MockTransport(handler),
        async_transport=httpx.MockTransport(handler),
    )


def test_api_key_is_required(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DNSCALE_API_KEY", raising=False)

    with pytest.raises(ValueError, match="API key is required"):
        DNScale()


def test_list_zones_uses_authentication_and_versioned_base_url() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "GET"
        assert request.url == "https://api.example.test/v1/zones?offset=0&limit=10"
        assert request.headers["Authorization"] == "Bearer test-key"
        assert request.headers["User-Agent"] == "dnscale-python/0.1.0"
        return httpx.Response(200, json=_zones_response())

    sdk = _client(handler)
    try:
        result = sdk.zones.list()
    finally:
        sdk.close()

    assert result.zones == []
    assert result.pagination.total == 0


def test_structured_api_errors_are_raised() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            404,
            headers={"X-Request-ID": "request-123"},
            json=_error_response("ZONE_NOT_FOUND", "zone does not exist"),
        )

    sdk = _client(handler)
    try:
        with pytest.raises(APIError) as raised:
            sdk.zones.list()
    finally:
        sdk.close()

    assert raised.value.status_code == 404
    assert raised.value.code == "ZONE_NOT_FOUND"
    assert raised.value.request_id == "request-123"


def test_safe_requests_retry_transient_responses() -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            return httpx.Response(503, json=_error_response("UNAVAILABLE"))
        return httpx.Response(200, json=_zones_response())

    sdk = _client(handler, max_retries=2)
    try:
        sdk.zones.list()
    finally:
        sdk.close()

    assert attempts == 3


def test_rate_limit_error_exposes_retry_after() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            429,
            headers={"Retry-After": "5"},
            json=_error_response("RATE_LIMITED"),
        )

    sdk = _client(handler)
    try:
        with pytest.raises(RateLimitError) as raised:
            sdk.zones.list()
    finally:
        sdk.close()

    assert raised.value.retry_after == "5"


def test_mutations_are_never_retried() -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        assert request.method == "POST"
        return httpx.Response(503, json=_error_response("UNAVAILABLE"))

    sdk = _client(handler, max_retries=2)
    try:
        with pytest.raises(APIError):
            sdk.zones.create("example.com")
    finally:
        sdk.close()

    assert attempts == 1


def test_async_resource_uses_the_same_contract() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=_zones_response())

    async def exercise() -> None:
        sdk = _client(handler)
        try:
            result = await sdk.zones.alist()
            assert result.pagination.count == 0
        finally:
            await sdk.aclose()

    asyncio.run(exercise())


def test_generated_client_covers_every_public_operation() -> None:
    operations = [
        module
        for module in pkgutil.walk_packages(
            dnscale_api.api.__path__, f"{dnscale_api.api.__name__}."
        )
        if not module.ispkg
    ]

    assert len(operations) == 59
