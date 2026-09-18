from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.api_keys_response_status import APIKeysResponseStatus

if TYPE_CHECKING:
    from ..models.api_keys_data import APIKeysData


T = TypeVar("T", bound="APIKeysResponse")


@_attrs_define
class APIKeysResponse:
    """
    Attributes:
        status (APIKeysResponseStatus):
        data (APIKeysData):
    """

    status: APIKeysResponseStatus
    data: APIKeysData

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
        from ..models.api_keys_data import APIKeysData

        d = dict(src_dict)
        status = APIKeysResponseStatus(d.pop("status"))

        data = APIKeysData.from_dict(d.pop("data"))

        api_keys_response = cls(
            status=status,
            data=data,
        )

        return api_keys_response
