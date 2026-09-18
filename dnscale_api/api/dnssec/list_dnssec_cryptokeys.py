from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.cryptokeys_response import CryptokeysResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    zone_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/zones/{zone_id}/dnssec/cryptokeys".format(
            zone_id=quote(str(zone_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CryptokeysResponse | ErrorResponse:
    if response.status_code == 200:
        response_200 = CryptokeysResponse.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CryptokeysResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    zone_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CryptokeysResponse | ErrorResponse]:
    """List DNSSEC cryptographic keys

    Args:
        zone_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptokeysResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        zone_id=zone_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    zone_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> CryptokeysResponse | ErrorResponse | None:
    """List DNSSEC cryptographic keys

    Args:
        zone_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptokeysResponse | ErrorResponse
    """

    return sync_detailed(
        zone_id=zone_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    zone_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CryptokeysResponse | ErrorResponse]:
    """List DNSSEC cryptographic keys

    Args:
        zone_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptokeysResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        zone_id=zone_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    zone_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> CryptokeysResponse | ErrorResponse | None:
    """List DNSSEC cryptographic keys

    Args:
        zone_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptokeysResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            zone_id=zone_id,
            client=client,
        )
    ).parsed
