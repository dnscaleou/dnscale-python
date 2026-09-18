from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.record_response import RecordResponse
from ...models.record_type import RecordType
from ...models.update_record_by_name_request import UpdateRecordByNameRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    zone_id: UUID,
    record_name: str,
    record_type: RecordType,
    *,
    body: UpdateRecordByNameRequest,
    content: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["content"] = content

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/zones/{zone_id}/records/by-name/{record_name}/{record_type}".format(
            zone_id=quote(str(zone_id), safe=""),
            record_name=quote(str(record_name), safe=""),
            record_type=quote(str(record_type), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | RecordResponse:
    if response.status_code == 200:
        response_200 = RecordResponse.from_dict(response.json())

        return response_200

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
    record_name: str,
    record_type: RecordType,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateRecordByNameRequest,
    content: str | Unset = UNSET,
) -> Response[ErrorResponse | RecordResponse]:
    """Update a record without tracking its content-derived ID

     For a multi-value RRset, pass the old value in `content` to select one record.

    Args:
        zone_id (UUID):
        record_name (str):
        record_type (RecordType):
        content (str | Unset):
        body (UpdateRecordByNameRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | RecordResponse]
    """

    kwargs = _get_kwargs(
        zone_id=zone_id,
        record_name=record_name,
        record_type=record_type,
        body=body,
        content=content,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    zone_id: UUID,
    record_name: str,
    record_type: RecordType,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateRecordByNameRequest,
    content: str | Unset = UNSET,
) -> ErrorResponse | RecordResponse | None:
    """Update a record without tracking its content-derived ID

     For a multi-value RRset, pass the old value in `content` to select one record.

    Args:
        zone_id (UUID):
        record_name (str):
        record_type (RecordType):
        content (str | Unset):
        body (UpdateRecordByNameRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | RecordResponse
    """

    return sync_detailed(
        zone_id=zone_id,
        record_name=record_name,
        record_type=record_type,
        client=client,
        body=body,
        content=content,
    ).parsed


async def asyncio_detailed(
    zone_id: UUID,
    record_name: str,
    record_type: RecordType,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateRecordByNameRequest,
    content: str | Unset = UNSET,
) -> Response[ErrorResponse | RecordResponse]:
    """Update a record without tracking its content-derived ID

     For a multi-value RRset, pass the old value in `content` to select one record.

    Args:
        zone_id (UUID):
        record_name (str):
        record_type (RecordType):
        content (str | Unset):
        body (UpdateRecordByNameRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | RecordResponse]
    """

    kwargs = _get_kwargs(
        zone_id=zone_id,
        record_name=record_name,
        record_type=record_type,
        body=body,
        content=content,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    zone_id: UUID,
    record_name: str,
    record_type: RecordType,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateRecordByNameRequest,
    content: str | Unset = UNSET,
) -> ErrorResponse | RecordResponse | None:
    """Update a record without tracking its content-derived ID

     For a multi-value RRset, pass the old value in `content` to select one record.

    Args:
        zone_id (UUID):
        record_name (str):
        record_type (RecordType):
        content (str | Unset):
        body (UpdateRecordByNameRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | RecordResponse
    """

    return (
        await asyncio_detailed(
            zone_id=zone_id,
            record_name=record_name,
            record_type=record_type,
            client=client,
            body=body,
            content=content,
        )
    ).parsed
