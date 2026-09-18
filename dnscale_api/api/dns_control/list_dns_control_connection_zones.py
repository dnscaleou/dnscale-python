from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dns_control_provider_zones_response import DNSControlProviderZonesResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    connection_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dns-sources/connections/{connection_id}/zones".format(
            connection_id=quote(str(connection_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DNSControlProviderZonesResponse | ErrorResponse:
    if response.status_code == 200:
        response_200 = DNSControlProviderZonesResponse.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DNSControlProviderZonesResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DNSControlProviderZonesResponse | ErrorResponse]:
    """List zones visible through a provider connection

    Args:
        connection_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSControlProviderZonesResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> DNSControlProviderZonesResponse | ErrorResponse | None:
    """List zones visible through a provider connection

    Args:
        connection_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSControlProviderZonesResponse | ErrorResponse
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DNSControlProviderZonesResponse | ErrorResponse]:
    """List zones visible through a provider connection

    Args:
        connection_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSControlProviderZonesResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> DNSControlProviderZonesResponse | ErrorResponse | None:
    """List zones visible through a provider connection

    Args:
        connection_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSControlProviderZonesResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
        )
    ).parsed
