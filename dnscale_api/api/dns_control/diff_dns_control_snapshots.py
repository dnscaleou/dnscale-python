from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dns_control_snapshot_diff_response import DNSControlSnapshotDiffResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    inventory_id: UUID,
    from_snapshot_id: UUID,
    to_snapshot_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dns-inventory/{inventory_id}/snapshots/{from_snapshot_id}/diff/{to_snapshot_id}".format(
            inventory_id=quote(str(inventory_id), safe=""),
            from_snapshot_id=quote(str(from_snapshot_id), safe=""),
            to_snapshot_id=quote(str(to_snapshot_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DNSControlSnapshotDiffResponse | ErrorResponse:
    if response.status_code == 200:
        response_200 = DNSControlSnapshotDiffResponse.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DNSControlSnapshotDiffResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    inventory_id: UUID,
    from_snapshot_id: UUID,
    to_snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DNSControlSnapshotDiffResponse | ErrorResponse]:
    """Compare two immutable DNS state snapshots

    Args:
        inventory_id (UUID):
        from_snapshot_id (UUID):
        to_snapshot_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSControlSnapshotDiffResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        inventory_id=inventory_id,
        from_snapshot_id=from_snapshot_id,
        to_snapshot_id=to_snapshot_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    inventory_id: UUID,
    from_snapshot_id: UUID,
    to_snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> DNSControlSnapshotDiffResponse | ErrorResponse | None:
    """Compare two immutable DNS state snapshots

    Args:
        inventory_id (UUID):
        from_snapshot_id (UUID):
        to_snapshot_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSControlSnapshotDiffResponse | ErrorResponse
    """

    return sync_detailed(
        inventory_id=inventory_id,
        from_snapshot_id=from_snapshot_id,
        to_snapshot_id=to_snapshot_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    inventory_id: UUID,
    from_snapshot_id: UUID,
    to_snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DNSControlSnapshotDiffResponse | ErrorResponse]:
    """Compare two immutable DNS state snapshots

    Args:
        inventory_id (UUID):
        from_snapshot_id (UUID):
        to_snapshot_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSControlSnapshotDiffResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        inventory_id=inventory_id,
        from_snapshot_id=from_snapshot_id,
        to_snapshot_id=to_snapshot_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    inventory_id: UUID,
    from_snapshot_id: UUID,
    to_snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> DNSControlSnapshotDiffResponse | ErrorResponse | None:
    """Compare two immutable DNS state snapshots

    Args:
        inventory_id (UUID):
        from_snapshot_id (UUID):
        to_snapshot_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSControlSnapshotDiffResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            inventory_id=inventory_id,
            from_snapshot_id=from_snapshot_id,
            to_snapshot_id=to_snapshot_id,
            client=client,
        )
    ).parsed
