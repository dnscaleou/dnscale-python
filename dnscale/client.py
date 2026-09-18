"""Configured DNScale API client."""

from __future__ import annotations

import os
import ssl
from collections.abc import Mapping

import httpx

from dnscale_api import AuthenticatedClient

from .records import Records
from .transport import AsyncRetryTransport, RetryTransport
from .zones import Zones

DEFAULT_BASE_URL = "https://api.dnscale.eu/v1"


class DNScale:
    """DNScale client with typed resources and access to every generated endpoint.

    The API key is read from ``DNSCALE_API_KEY`` when it is not passed explicitly.
    Only safe read requests are retried after transient HTTP or transport failures.
    """

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float | httpx.Timeout = 10.0,
        max_retries: int = 2,
        retry_backoff: float = 0.25,
        verify_ssl: str | bool | ssl.SSLContext = True,
        follow_redirects: bool = False,
        headers: Mapping[str, str] | None = None,
        transport: httpx.BaseTransport | None = None,
        async_transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        token = api_key or os.getenv("DNSCALE_API_KEY")
        if not token:
            raise ValueError("A DNScale API key is required; pass api_key or set DNSCALE_API_KEY")
        if max_retries < 0:
            raise ValueError("max_retries must be zero or greater")
        if retry_backoff < 0:
            raise ValueError("retry_backoff must be zero or greater")

        normalized_base_url = base_url.rstrip("/")
        request_headers = {
            "Accept": "application/json",
            "User-Agent": "dnscale-python/0.1.0",
            **dict(headers or {}),
            "Authorization": f"Bearer {token}",
        }

        sync_client = httpx.Client(
            base_url=normalized_base_url,
            headers=request_headers,
            timeout=timeout,
            verify=verify_ssl,
            follow_redirects=follow_redirects,
            transport=RetryTransport(
                max_retries=max_retries,
                backoff=retry_backoff,
                verify_ssl=verify_ssl,
                transport=transport,
            ),
        )
        async_client = httpx.AsyncClient(
            base_url=normalized_base_url,
            headers=request_headers,
            timeout=timeout,
            verify=verify_ssl,
            follow_redirects=follow_redirects,
            transport=AsyncRetryTransport(
                max_retries=max_retries,
                backoff=retry_backoff,
                verify_ssl=verify_ssl,
                transport=async_transport,
            ),
        )

        self.client = AuthenticatedClient(
            base_url=normalized_base_url,
            token=token,
            headers=dict(request_headers),
            timeout=httpx.Timeout(timeout) if isinstance(timeout, float | int) else timeout,
            verify_ssl=verify_ssl,
            follow_redirects=follow_redirects,
            raise_on_unexpected_status=True,
        )
        self.client.set_httpx_client(sync_client)
        self.client.set_async_httpx_client(async_client)

        self.zones = Zones(self.client)
        self.records = Records(self.client)

    def close(self) -> None:
        """Close the blocking HTTP client."""

        self.client.get_httpx_client().close()

    async def aclose(self) -> None:
        """Close the asynchronous HTTP client."""

        await self.client.get_async_httpx_client().aclose()

    def __enter__(self) -> DNScale:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    async def __aenter__(self) -> DNScale:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.aclose()
