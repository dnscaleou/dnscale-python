from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dns_control_connection_snapshot_response import DNSControlConnectionSnapshotResponse
from ...models.dns_control_provider_zone_request import DNSControlProviderZoneRequest
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    connection_id: UUID,
    external_zone_id: str,
    *,
    body: DNSControlProviderZoneRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dns-sources/connections/{connection_id}/zones/{external_zone_id}/snapshots".format(
            connection_id=quote(str(connection_id), safe=""),
            external_zone_id=quote(str(external_zone_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DNSControlConnectionSnapshotResponse | ErrorResponse:
    if response.status_code == 201:
        response_201 = DNSControlConnectionSnapshotResponse.from_dict(response.json())

        return response_201

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DNSControlConnectionSnapshotResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_id: UUID,
    external_zone_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DNSControlProviderZoneRequest | Unset = UNSET,
) -> Response[DNSControlConnectionSnapshotResponse | ErrorResponse]:
    """Capture a snapshot directly from an external provider zone

    Args:
        connection_id (UUID):
        external_zone_id (str):
        body (DNSControlProviderZoneRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSControlConnectionSnapshotResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        external_zone_id=external_zone_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_id: UUID,
    external_zone_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DNSControlProviderZoneRequest | Unset = UNSET,
) -> DNSControlConnectionSnapshotResponse | ErrorResponse | None:
    """Capture a snapshot directly from an external provider zone

    Args:
        connection_id (UUID):
        external_zone_id (str):
        body (DNSControlProviderZoneRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSControlConnectionSnapshotResponse | ErrorResponse
    """

    return sync_detailed(
        connection_id=connection_id,
        external_zone_id=external_zone_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    connection_id: UUID,
    external_zone_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DNSControlProviderZoneRequest | Unset = UNSET,
) -> Response[DNSControlConnectionSnapshotResponse | ErrorResponse]:
    """Capture a snapshot directly from an external provider zone

    Args:
        connection_id (UUID):
        external_zone_id (str):
        body (DNSControlProviderZoneRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSControlConnectionSnapshotResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        external_zone_id=external_zone_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: UUID,
    external_zone_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DNSControlProviderZoneRequest | Unset = UNSET,
) -> DNSControlConnectionSnapshotResponse | ErrorResponse | None:
    """Capture a snapshot directly from an external provider zone

    Args:
        connection_id (UUID):
        external_zone_id (str):
        body (DNSControlProviderZoneRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSControlConnectionSnapshotResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            external_zone_id=external_zone_id,
            client=client,
            body=body,
        )
    ).parsed
