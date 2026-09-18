from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.cryptokey_response import CryptokeyResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    zone_id: UUID,
    key_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/zones/{zone_id}/dnssec/cryptokeys/{key_id}".format(
            zone_id=quote(str(zone_id), safe=""),
            key_id=quote(str(key_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CryptokeyResponse | ErrorResponse:
    if response.status_code == 200:
        response_200 = CryptokeyResponse.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CryptokeyResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    zone_id: UUID,
    key_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CryptokeyResponse | ErrorResponse]:
    """Get a DNSSEC cryptographic key

    Args:
        zone_id (UUID):
        key_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptokeyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        zone_id=zone_id,
        key_id=key_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    zone_id: UUID,
    key_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> CryptokeyResponse | ErrorResponse | None:
    """Get a DNSSEC cryptographic key

    Args:
        zone_id (UUID):
        key_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptokeyResponse | ErrorResponse
    """

    return sync_detailed(
        zone_id=zone_id,
        key_id=key_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    zone_id: UUID,
    key_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CryptokeyResponse | ErrorResponse]:
    """Get a DNSSEC cryptographic key

    Args:
        zone_id (UUID):
        key_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptokeyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        zone_id=zone_id,
        key_id=key_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    zone_id: UUID,
    key_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> CryptokeyResponse | ErrorResponse | None:
    """Get a DNSSEC cryptographic key

    Args:
        zone_id (UUID):
        key_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptokeyResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            zone_id=zone_id,
            key_id=key_id,
            client=client,
        )
    ).parsed
