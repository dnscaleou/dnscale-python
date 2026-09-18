from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.cryptokey_response_status import CryptokeyResponseStatus

if TYPE_CHECKING:
    from ..models.cryptokey_data import CryptokeyData


T = TypeVar("T", bound="CryptokeyResponse")


@_attrs_define
class CryptokeyResponse:
    """
    Attributes:
        status (CryptokeyResponseStatus):
        data (CryptokeyData):
    """

    status: CryptokeyResponseStatus
    data: CryptokeyData

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
        from ..models.cryptokey_data import CryptokeyData

        d = dict(src_dict)
        status = CryptokeyResponseStatus(d.pop("status"))

        data = CryptokeyData.from_dict(d.pop("data"))

        cryptokey_response = cls(
            status=status,
            data=data,
        )

        return cryptokey_response
