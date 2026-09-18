from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_cryptokey_request import CreateCryptokeyRequest
from ...models.cryptokey_response import CryptokeyResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    zone_id: UUID,
    *,
    body: CreateCryptokeyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/zones/{zone_id}/dnssec/cryptokeys".format(
            zone_id=quote(str(zone_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CryptokeyResponse | ErrorResponse:
    if response.status_code == 201:
        response_201 = CryptokeyResponse.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient | Client,
    body: CreateCryptokeyRequest,
) -> Response[CryptokeyResponse | ErrorResponse]:
    """Create a DNSSEC cryptographic key

    Args:
        zone_id (UUID):
        body (CreateCryptokeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptokeyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        zone_id=zone_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    zone_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateCryptokeyRequest,
) -> CryptokeyResponse | ErrorResponse | None:
    """Create a DNSSEC cryptographic key

    Args:
        zone_id (UUID):
        body (CreateCryptokeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptokeyResponse | ErrorResponse
    """

    return sync_detailed(
        zone_id=zone_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    zone_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateCryptokeyRequest,
) -> Response[CryptokeyResponse | ErrorResponse]:
    """Create a DNSSEC cryptographic key

    Args:
        zone_id (UUID):
        body (CreateCryptokeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptokeyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        zone_id=zone_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    zone_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateCryptokeyRequest,
) -> CryptokeyResponse | ErrorResponse | None:
    """Create a DNSSEC cryptographic key

    Args:
        zone_id (UUID):
        body (CreateCryptokeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptokeyResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            zone_id=zone_id,
            client=client,
            body=body,
        )
    ).parsed
