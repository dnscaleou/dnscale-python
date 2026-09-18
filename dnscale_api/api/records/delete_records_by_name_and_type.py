from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.record_type import RecordType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    zone_id: UUID,
    record_name: str,
    record_type: RecordType,
    *,
    content: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["content"] = content

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/zones/{zone_id}/records/by-name/{record_name}/{record_type}".format(
            zone_id=quote(str(zone_id), safe=""),
            record_name=quote(str(record_name), safe=""),
            record_type=quote(str(record_type), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorResponse:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorResponse]:
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
    content: str | Unset = UNSET,
) -> Response[Any | ErrorResponse]:
    """Delete matching record values

     Omit `content` to delete the entire RRset, or supply it to delete one value.

    Args:
        zone_id (UUID):
        record_name (str):
        record_type (RecordType):
        content (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        zone_id=zone_id,
        record_name=record_name,
        record_type=record_type,
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
    content: str | Unset = UNSET,
) -> Any | ErrorResponse | None:
    """Delete matching record values

     Omit `content` to delete the entire RRset, or supply it to delete one value.

    Args:
        zone_id (UUID):
        record_name (str):
        record_type (RecordType):
        content (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return sync_detailed(
        zone_id=zone_id,
        record_name=record_name,
        record_type=record_type,
        client=client,
        content=content,
    ).parsed


async def asyncio_detailed(
    zone_id: UUID,
    record_name: str,
    record_type: RecordType,
    *,
    client: AuthenticatedClient | Client,
    content: str | Unset = UNSET,
) -> Response[Any | ErrorResponse]:
    """Delete matching record values

     Omit `content` to delete the entire RRset, or supply it to delete one value.

    Args:
        zone_id (UUID):
        record_name (str):
        record_type (RecordType):
        content (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        zone_id=zone_id,
        record_name=record_name,
        record_type=record_type,
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
    content: str | Unset = UNSET,
) -> Any | ErrorResponse | None:
    """Delete matching record values

     Omit `content` to delete the entire RRset, or supply it to delete one value.

    Args:
        zone_id (UUID):
        record_name (str):
        record_type (RecordType):
        content (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return (
        await asyncio_detailed(
            zone_id=zone_id,
            record_name=record_name,
            record_type=record_type,
            client=client,
            content=content,
        )
    ).parsed
