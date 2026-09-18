import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.top_zones_response import TopZonesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    limit: int | Unset = 10,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date: str | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/usage/top-zones",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | TopZonesResponse:
    if response.status_code == 200:
        response_200 = TopZonesResponse.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | TopZonesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    limit: int | Unset = 10,
) -> Response[ErrorResponse | TopZonesResponse]:
    """List zones with the highest query volume

    Args:
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TopZonesResponse]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    limit: int | Unset = 10,
) -> ErrorResponse | TopZonesResponse | None:
    """List zones with the highest query volume

    Args:
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TopZonesResponse
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    limit: int | Unset = 10,
) -> Response[ErrorResponse | TopZonesResponse]:
    """List zones with the highest query volume

    Args:
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TopZonesResponse]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    limit: int | Unset = 10,
) -> ErrorResponse | TopZonesResponse | None:
    """List zones with the highest query volume

    Args:
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TopZonesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
            limit=limit,
        )
    ).parsed
