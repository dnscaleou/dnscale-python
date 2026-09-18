"""Exceptions raised by the handwritten SDK layer."""

from __future__ import annotations

from typing import Any, TypeVar, cast

import httpx

from dnscale_api.models.error_response import ErrorResponse
from dnscale_api.types import Response, Unset

T = TypeVar("T")


class APIError(Exception):
    """A structured error returned by DNScale."""

    def __init__(
        self,
        *,
        status_code: int,
        code: str,
        message: str,
        details: list[dict[str, Any]] | None = None,
        request_id: str | None = None,
    ) -> None:
        self.status_code = status_code
        self.code = code
        self.message = message
        self.details = details
        self.request_id = request_id
        super().__init__(f"DNScale API error {status_code} ({code}): {message}")


class RateLimitError(APIError):
    """The API still returned HTTP 429 after safe retries were exhausted."""

    def __init__(self, *, retry_after: str | None = None, **kwargs: Any) -> None:
        self.retry_after = retry_after
        super().__init__(**kwargs)


class ProtocolError(Exception):
    """The API returned a successful response that did not match its contract."""


def _check_error_body(response: httpx.Response) -> None:
    try:
        body = response.json()
        if isinstance(body, dict) and isinstance(body.get("error"), dict):
            error = body["error"]
            if isinstance(error.get("code"), str) and isinstance(error.get("message"), str):
                return
    except ValueError:
        pass
    kwargs: dict[str, Any] = {
        "status_code": response.status_code,
        "code": "HTTP_ERROR",
        "message": "DNScale returned an HTTP error without a valid API error envelope",
        "request_id": response.headers.get("X-Request-ID"),
    }
    if response.status_code == 429:
        raise RateLimitError(retry_after=response.headers.get("Retry-After"), **kwargs)
    raise APIError(**kwargs)


def check_error_response(response: httpx.Response) -> None:
    if response.status_code >= 400:
        response.read()
        _check_error_body(response)


async def acheck_error_response(response: httpx.Response) -> None:
    if response.status_code >= 400:
        await response.aread()
        _check_error_body(response)


def unwrap(response: Response[T | ErrorResponse]) -> T | None:
    """Return a successful parsed response or raise a structured SDK exception."""

    parsed = response.parsed
    if isinstance(parsed, ErrorResponse):
        raw_details = parsed.error.details
        details = None
        if not isinstance(raw_details, Unset):
            details = [item.to_dict() for item in raw_details]

        error_type = RateLimitError if int(response.status_code) == 429 else APIError
        kwargs: dict[str, Any] = {
            "status_code": int(response.status_code),
            "code": parsed.error.code,
            "message": parsed.error.message,
            "details": details,
            "request_id": response.headers.get("X-Request-ID"),
        }
        if error_type is RateLimitError:
            kwargs["retry_after"] = response.headers.get("Retry-After")
        raise error_type(**kwargs)

    if parsed is None and not 200 <= int(response.status_code) < 300:
        raise ProtocolError(
            f"DNScale returned HTTP {int(response.status_code)} without a valid error body"
        )

    return cast(T | None, parsed)


def expect(value: T | None, expected_type: type[T]) -> T:
    """Narrow generated response unions and detect successful contract drift."""

    if not isinstance(value, expected_type):
        raise ProtocolError(f"DNScale returned an invalid {expected_type.__name__} response")
    return value
