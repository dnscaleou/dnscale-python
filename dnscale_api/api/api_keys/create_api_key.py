from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_key_response import APIKeyResponse
from ...models.create_api_key_request import CreateAPIKeyRequest
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    user_id: UUID,
    *,
    body: CreateAPIKeyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/{user_id}/apikeys".format(
            user_id=quote(str(user_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIKeyResponse | ErrorResponse:
    if response.status_code == 201:
        response_201 = APIKeyResponse.from_dict(response.json())

        return response_201

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIKeyResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateAPIKeyRequest,
) -> Response[APIKeyResponse | ErrorResponse]:
    """Create an API key for a user

     The secret key is returned only in this response. Use `zone_scopes` to
    restrict a key to zones and, optionally, exact DNS owner names within
    each zone. `zone_ids` is retained for compatibility and grants all DNS
    names in each listed zone. Do not send both fields with non-empty values.

    Args:
        user_id (UUID):
        body (CreateAPIKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIKeyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateAPIKeyRequest,
) -> APIKeyResponse | ErrorResponse | None:
    """Create an API key for a user

     The secret key is returned only in this response. Use `zone_scopes` to
    restrict a key to zones and, optionally, exact DNS owner names within
    each zone. `zone_ids` is retained for compatibility and grants all DNS
    names in each listed zone. Do not send both fields with non-empty values.

    Args:
        user_id (UUID):
        body (CreateAPIKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIKeyResponse | ErrorResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateAPIKeyRequest,
) -> Response[APIKeyResponse | ErrorResponse]:
    """Create an API key for a user

     The secret key is returned only in this response. Use `zone_scopes` to
    restrict a key to zones and, optionally, exact DNS owner names within
    each zone. `zone_ids` is retained for compatibility and grants all DNS
    names in each listed zone. Do not send both fields with non-empty values.

    Args:
        user_id (UUID):
        body (CreateAPIKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIKeyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateAPIKeyRequest,
) -> APIKeyResponse | ErrorResponse | None:
    """Create an API key for a user

     The secret key is returned only in this response. Use `zone_scopes` to
    restrict a key to zones and, optionally, exact DNS owner names within
    each zone. `zone_ids` is retained for compatibility and grants all DNS
    names in each listed zone. Do not send both fields with non-empty values.

    Args:
        user_id (UUID):
        body (CreateAPIKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIKeyResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
