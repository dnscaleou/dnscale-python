from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.customer_usage_response import CustomerUsageResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    month: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["month"] = month

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/usage/summary",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomerUsageResponse | ErrorResponse:
    if response.status_code == 200:
        response_200 = CustomerUsageResponse.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CustomerUsageResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    month: str | Unset = UNSET,
) -> Response[CustomerUsageResponse | ErrorResponse]:
    """Get customer usage for a billing month

    Args:
        month (str | Unset):  Example: 2026-08.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerUsageResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        month=month,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    month: str | Unset = UNSET,
) -> CustomerUsageResponse | ErrorResponse | None:
    """Get customer usage for a billing month

    Args:
        month (str | Unset):  Example: 2026-08.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerUsageResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        month=month,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    month: str | Unset = UNSET,
) -> Response[CustomerUsageResponse | ErrorResponse]:
    """Get customer usage for a billing month

    Args:
        month (str | Unset):  Example: 2026-08.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerUsageResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        month=month,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    month: str | Unset = UNSET,
) -> CustomerUsageResponse | ErrorResponse | None:
    """Get customer usage for a billing month

    Args:
        month (str | Unset):  Example: 2026-08.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerUsageResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            month=month,
        )
    ).parsed
