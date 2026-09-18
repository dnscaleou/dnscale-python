from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.error_response_status import ErrorResponseStatus

if TYPE_CHECKING:
    from ..models.error_detail import ErrorDetail


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """
    Attributes:
        status (ErrorResponseStatus):
        error (ErrorDetail):
    """

    status: ErrorResponseStatus
    error: ErrorDetail

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        error = self.error.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_detail import ErrorDetail

        d = dict(src_dict)
        status = ErrorResponseStatus(d.pop("status"))

        error = ErrorDetail.from_dict(d.pop("error"))

        error_response = cls(
            status=status,
            error=error,
        )

        return error_response
