from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.cryptokey import Cryptokey


T = TypeVar("T", bound="CryptokeyData")


@_attrs_define
class CryptokeyData:
    """
    Attributes:
        cryptokey (Cryptokey):
    """

    cryptokey: Cryptokey

    def to_dict(self) -> dict[str, Any]:
        cryptokey = self.cryptokey.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cryptokey": cryptokey,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptokey import Cryptokey

        d = dict(src_dict)
        cryptokey = Cryptokey.from_dict(d.pop("cryptokey"))

        cryptokey_data = cls(
            cryptokey=cryptokey,
        )

        return cryptokey_data
