from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.alert_scope_type import AlertScopeType
from ...models.alerts_response import AlertsResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    scope_type: AlertScopeType | Unset = UNSET,
    scope_id: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_scope_type: str | Unset = UNSET
    if not isinstance(scope_type, Unset):
        json_scope_type = scope_type.value

    params["scope_type"] = json_scope_type

    params["scope_id"] = scope_id

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/alerts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertsResponse | ErrorResponse:
    if response.status_code == 200:
        response_200 = AlertsResponse.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AlertsResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    scope_type: AlertScopeType | Unset = UNSET,
    scope_id: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
) -> Response[AlertsResponse | ErrorResponse]:
    """List DNS traffic alert routes

    Args:
        scope_type (AlertScopeType | Unset):
        scope_id (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertsResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        scope_type=scope_type,
        scope_id=scope_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    scope_type: AlertScopeType | Unset = UNSET,
    scope_id: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
) -> AlertsResponse | ErrorResponse | None:
    """List DNS traffic alert routes

    Args:
        scope_type (AlertScopeType | Unset):
        scope_id (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertsResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        scope_type=scope_type,
        scope_id=scope_id,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    scope_type: AlertScopeType | Unset = UNSET,
    scope_id: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
) -> Response[AlertsResponse | ErrorResponse]:
    """List DNS traffic alert routes

    Args:
        scope_type (AlertScopeType | Unset):
        scope_id (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertsResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        scope_type=scope_type,
        scope_id=scope_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    scope_type: AlertScopeType | Unset = UNSET,
    scope_id: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
) -> AlertsResponse | ErrorResponse | None:
    """List DNS traffic alert routes

    Args:
        scope_type (AlertScopeType | Unset):
        scope_id (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertsResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            scope_type=scope_type,
            scope_id=scope_id,
            offset=offset,
            limit=limit,
        )
    ).parsed
