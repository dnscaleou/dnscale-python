from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.alert_response import AlertResponse
from ...models.error_response import ErrorResponse
from ...models.update_alert_request import UpdateAlertRequest
from ...types import Response


def _get_kwargs(
    alert_id: str,
    *,
    body: UpdateAlertRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/alerts/{alert_id}".format(
            alert_id=quote(str(alert_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AlertResponse | ErrorResponse:
    if response.status_code == 200:
        response_200 = AlertResponse.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AlertResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alert_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAlertRequest,
) -> Response[AlertResponse | ErrorResponse]:
    """Update selected fields of an alert route

    Args:
        alert_id (str):
        body (UpdateAlertRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAlertRequest,
) -> AlertResponse | ErrorResponse | None:
    """Update selected fields of an alert route

    Args:
        alert_id (str):
        body (UpdateAlertRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertResponse | ErrorResponse
    """

    return sync_detailed(
        alert_id=alert_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    alert_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAlertRequest,
) -> Response[AlertResponse | ErrorResponse]:
    """Update selected fields of an alert route

    Args:
        alert_id (str):
        body (UpdateAlertRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAlertRequest,
) -> AlertResponse | ErrorResponse | None:
    """Update selected fields of an alert route

    Args:
        alert_id (str):
        body (UpdateAlertRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            alert_id=alert_id,
            client=client,
            body=body,
        )
    ).parsed
