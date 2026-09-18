import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.aggregated_usage_response_envelope import AggregatedUsageResponseEnvelope
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
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

    json_zone_id: str | Unset = UNSET
    if not isinstance(zone_id, Unset):
        json_zone_id = str(zone_id)
    params["zone_id"] = json_zone_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/usage/daily",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AggregatedUsageResponseEnvelope | ErrorResponse:
    if response.status_code == 200:
        response_200 = AggregatedUsageResponseEnvelope.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AggregatedUsageResponseEnvelope | ErrorResponse]:
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
    zone_id: UUID | Unset = UNSET,
) -> Response[AggregatedUsageResponseEnvelope | ErrorResponse]:
    """Get daily usage aggregated across accessible zones

    Args:
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AggregatedUsageResponseEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        zone_id=zone_id,
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
    zone_id: UUID | Unset = UNSET,
) -> AggregatedUsageResponseEnvelope | ErrorResponse | None:
    """Get daily usage aggregated across accessible zones

    Args:
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AggregatedUsageResponseEnvelope | ErrorResponse
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
        zone_id=zone_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
) -> Response[AggregatedUsageResponseEnvelope | ErrorResponse]:
    """Get daily usage aggregated across accessible zones

    Args:
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AggregatedUsageResponseEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        zone_id=zone_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
) -> AggregatedUsageResponseEnvelope | ErrorResponse | None:
    """Get daily usage aggregated across accessible zones

    Args:
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AggregatedUsageResponseEnvelope | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
            zone_id=zone_id,
        )
    ).parsed
