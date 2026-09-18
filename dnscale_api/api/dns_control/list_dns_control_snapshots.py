from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dns_control_snapshots_response import DNSControlSnapshotsResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    inventory_id: UUID,
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dns-inventory/{inventory_id}/snapshots".format(
            inventory_id=quote(str(inventory_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DNSControlSnapshotsResponse | ErrorResponse:
    if response.status_code == 200:
        response_200 = DNSControlSnapshotsResponse.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DNSControlSnapshotsResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    inventory_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> Response[DNSControlSnapshotsResponse | ErrorResponse]:
    """List snapshots for an inventory item

    Args:
        inventory_id (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSControlSnapshotsResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        inventory_id=inventory_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    inventory_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> DNSControlSnapshotsResponse | ErrorResponse | None:
    """List snapshots for an inventory item

    Args:
        inventory_id (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSControlSnapshotsResponse | ErrorResponse
    """

    return sync_detailed(
        inventory_id=inventory_id,
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    inventory_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> Response[DNSControlSnapshotsResponse | ErrorResponse]:
    """List snapshots for an inventory item

    Args:
        inventory_id (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSControlSnapshotsResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        inventory_id=inventory_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    inventory_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> DNSControlSnapshotsResponse | ErrorResponse | None:
    """List snapshots for an inventory item

    Args:
        inventory_id (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSControlSnapshotsResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            inventory_id=inventory_id,
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
