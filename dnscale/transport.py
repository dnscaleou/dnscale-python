"""Conservative retry transports for DNScale reads."""

from __future__ import annotations

import asyncio
import ssl
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

import httpx

_SAFE_METHODS = frozenset({"GET", "HEAD", "OPTIONS"})
_RETRYABLE_STATUS_CODES = frozenset({408, 429, 500, 502, 503, 504})
_MAX_RETRY_DELAY = 30.0


def _retry_delay(response: httpx.Response | None, retry_number: int, backoff: float) -> float:
    if response is not None:
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            try:
                return min(max(float(retry_after), 0.0), _MAX_RETRY_DELAY)
            except ValueError:
                try:
                    retry_at = parsedate_to_datetime(retry_after)
                    if retry_at.tzinfo is None:
                        retry_at = retry_at.replace(tzinfo=timezone.utc)
                    seconds = (retry_at - datetime.now(timezone.utc)).total_seconds()
                    return min(max(seconds, 0.0), _MAX_RETRY_DELAY)
                except (TypeError, ValueError, OverflowError):
                    pass
    return min(backoff * (2 ** (retry_number - 1)), _MAX_RETRY_DELAY)


class RetryTransport(httpx.BaseTransport):
    """Retry transient failures only for methods that cannot mutate DNS state."""

    def __init__(
        self,
        *,
        max_retries: int,
        backoff: float,
        verify_ssl: str | bool | ssl.SSLContext,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self._max_retries = max_retries
        self._backoff = backoff
        self._transport = transport or httpx.HTTPTransport(verify=verify_ssl)

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        if request.method not in _SAFE_METHODS:
            return self._transport.handle_request(request)

        for retry_number in range(1, self._max_retries + 2):
            response = None
            try:
                response = self._transport.handle_request(request)
            except httpx.TransportError:
                if retry_number > self._max_retries:
                    raise
            else:
                if (
                    response.status_code not in _RETRYABLE_STATUS_CODES
                    or retry_number > self._max_retries
                ):
                    return response
                response.close()

            delay = _retry_delay(response, retry_number, self._backoff)
            if delay:
                time.sleep(delay)

        raise RuntimeError("unreachable retry state")

    def close(self) -> None:
        self._transport.close()


class AsyncRetryTransport(httpx.AsyncBaseTransport):
    """Async equivalent of :class:`RetryTransport`."""

    def __init__(
        self,
        *,
        max_retries: int,
        backoff: float,
        verify_ssl: str | bool | ssl.SSLContext,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        self._max_retries = max_retries
        self._backoff = backoff
        self._transport = transport or httpx.AsyncHTTPTransport(verify=verify_ssl)

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        if request.method not in _SAFE_METHODS:
            return await self._transport.handle_async_request(request)

        for retry_number in range(1, self._max_retries + 2):
            response = None
            try:
                response = await self._transport.handle_async_request(request)
            except httpx.TransportError:
                if retry_number > self._max_retries:
                    raise
            else:
                if (
                    response.status_code not in _RETRYABLE_STATUS_CODES
                    or retry_number > self._max_retries
                ):
                    return response
                await response.aclose()

            delay = _retry_delay(response, retry_number, self._backoff)
            if delay:
                await asyncio.sleep(delay)

        raise RuntimeError("unreachable retry state")

    async def aclose(self) -> None:
        await self._transport.aclose()
