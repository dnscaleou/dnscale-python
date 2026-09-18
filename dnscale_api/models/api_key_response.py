from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.api_key_response_status import APIKeyResponseStatus

if TYPE_CHECKING:
    from ..models.api_key_data import APIKeyData


T = TypeVar("T", bound="APIKeyResponse")


@_attrs_define
class APIKeyResponse:
    """
    Attributes:
        status (APIKeyResponseStatus):
        data (APIKeyData):
    """

    status: APIKeyResponseStatus
    data: APIKeyData

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_data import APIKeyData

        d = dict(src_dict)
        status = APIKeyResponseStatus(d.pop("status"))

        data = APIKeyData.from_dict(d.pop("data"))

        api_key_response = cls(
            status=status,
            data=data,
        )

        return api_key_response
