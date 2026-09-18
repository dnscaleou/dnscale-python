from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_detail_details_item import ErrorDetailDetailsItem


T = TypeVar("T", bound="ErrorDetail")


@_attrs_define
class ErrorDetail:
    """
    Attributes:
        code (str):  Example: INVALID_ZONE_ID.
        message (str):
        details (list[ErrorDetailDetailsItem] | Unset):
    """

    code: str
    message: str
    details: list[ErrorDetailDetailsItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_detail_details_item import ErrorDetailDetailsItem

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        _details = d.pop("details", UNSET)
        details: list[ErrorDetailDetailsItem] | Unset = UNSET
        if _details is not UNSET:
            details = []
            for details_item_data in _details:
                details_item = ErrorDetailDetailsItem.from_dict(details_item_data)

                details.append(details_item)

        error_detail = cls(
            code=code,
            message=message,
            details=details,
        )

        return error_detail
