from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_record_request import CreateRecordRequest
from ...models.error_response import ErrorResponse
from ...models.record_response import RecordResponse
from ...types import Response


def _get_kwargs(
    zone_id: UUID,
    *,
    body: CreateRecordRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/zones/{zone_id}/records".format(
            zone_id=quote(str(zone_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | RecordResponse:
    if response.status_code == 201:
        response_201 = RecordResponse.from_dict(response.json())

        return response_201

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | RecordResponse]:
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
    body: CreateRecordRequest,
) -> Response[ErrorResponse | RecordResponse]:
    """Create a DNS record value

    Args:
        zone_id (UUID):
        body (CreateRecordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | RecordResponse]
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
    body: CreateRecordRequest,
) -> ErrorResponse | RecordResponse | None:
    """Create a DNS record value

    Args:
        zone_id (UUID):
        body (CreateRecordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | RecordResponse
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
    body: CreateRecordRequest,
) -> Response[ErrorResponse | RecordResponse]:
    """Create a DNS record value

    Args:
        zone_id (UUID):
        body (CreateRecordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | RecordResponse]
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
    body: CreateRecordRequest,
) -> ErrorResponse | RecordResponse | None:
    """Create a DNS record value

    Args:
        zone_id (UUID):
        body (CreateRecordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | RecordResponse
    """

    return (
        await asyncio_detailed(
            zone_id=zone_id,
            client=client,
            body=body,
        )
    ).parsed
