from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.invitation_response import InvitationResponse
from ...types import Response


def _get_kwargs(
    invitation_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/invitations-admin/{invitation_id}".format(
            invitation_id=quote(str(invitation_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | InvitationResponse:
    if response.status_code == 200:
        response_200 = InvitationResponse.from_dict(response.json())

        return response_200

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | InvitationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    invitation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | InvitationResponse]:
    """Get an invitation

    Args:
        invitation_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InvitationResponse]
    """

    kwargs = _get_kwargs(
        invitation_id=invitation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invitation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | InvitationResponse | None:
    """Get an invitation

    Args:
        invitation_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InvitationResponse
    """

    return sync_detailed(
        invitation_id=invitation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    invitation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | InvitationResponse]:
    """Get an invitation

    Args:
        invitation_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InvitationResponse]
    """

    kwargs = _get_kwargs(
        invitation_id=invitation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invitation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | InvitationResponse | None:
    """Get an invitation

    Args:
        invitation_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InvitationResponse
    """

    return (
        await asyncio_detailed(
            invitation_id=invitation_id,
            client=client,
        )
    ).parsed
