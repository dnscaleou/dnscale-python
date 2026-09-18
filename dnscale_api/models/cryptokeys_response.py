from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.cryptokeys_response_status import CryptokeysResponseStatus

if TYPE_CHECKING:
    from ..models.cryptokeys_data import CryptokeysData


T = TypeVar("T", bound="CryptokeysResponse")


@_attrs_define
class CryptokeysResponse:
    """
    Attributes:
        status (CryptokeysResponseStatus):
        data (CryptokeysData):
    """

    status: CryptokeysResponseStatus
    data: CryptokeysData

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
        from ..models.cryptokeys_data import CryptokeysData

        d = dict(src_dict)
        status = CryptokeysResponseStatus(d.pop("status"))

        data = CryptokeysData.from_dict(d.pop("data"))

        cryptokeys_response = cls(
            status=status,
            data=data,
        )

        return cryptokeys_response
