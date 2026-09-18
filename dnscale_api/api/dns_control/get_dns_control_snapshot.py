from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dns_control_snapshot_response import DNSControlSnapshotResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    inventory_id: UUID,
    snapshot_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dns-inventory/{inventory_id}/snapshots/{snapshot_id}".format(
            inventory_id=quote(str(inventory_id), safe=""),
            snapshot_id=quote(str(snapshot_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DNSControlSnapshotResponse | ErrorResponse:
    if response.status_code == 200:
        response_200 = DNSControlSnapshotResponse.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DNSControlSnapshotResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    inventory_id: UUID,
    snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DNSControlSnapshotResponse | ErrorResponse]:
    """Get a snapshot and its normalized record sets

    Args:
        inventory_id (UUID):
        snapshot_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSControlSnapshotResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        inventory_id=inventory_id,
        snapshot_id=snapshot_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    inventory_id: UUID,
    snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> DNSControlSnapshotResponse | ErrorResponse | None:
    """Get a snapshot and its normalized record sets

    Args:
        inventory_id (UUID):
        snapshot_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSControlSnapshotResponse | ErrorResponse
    """

    return sync_detailed(
        inventory_id=inventory_id,
        snapshot_id=snapshot_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    inventory_id: UUID,
    snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DNSControlSnapshotResponse | ErrorResponse]:
    """Get a snapshot and its normalized record sets

    Args:
        inventory_id (UUID):
        snapshot_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSControlSnapshotResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        inventory_id=inventory_id,
        snapshot_id=snapshot_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    inventory_id: UUID,
    snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> DNSControlSnapshotResponse | ErrorResponse | None:
    """Get a snapshot and its normalized record sets

    Args:
        inventory_id (UUID):
        snapshot_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSControlSnapshotResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            inventory_id=inventory_id,
            snapshot_id=snapshot_id,
            client=client,
        )
    ).parsed
