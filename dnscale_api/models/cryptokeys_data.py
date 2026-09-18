from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.cryptokey import Cryptokey


T = TypeVar("T", bound="CryptokeysData")


@_attrs_define
class CryptokeysData:
    """
    Attributes:
        cryptokeys (list[Cryptokey]):
    """

    cryptokeys: list[Cryptokey]

    def to_dict(self) -> dict[str, Any]:
        cryptokeys = []
        for cryptokeys_item_data in self.cryptokeys:
            cryptokeys_item = cryptokeys_item_data.to_dict()
            cryptokeys.append(cryptokeys_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cryptokeys": cryptokeys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptokey import Cryptokey

        d = dict(src_dict)
        cryptokeys = []
        _cryptokeys = d.pop("cryptokeys")
        for cryptokeys_item_data in _cryptokeys:
            cryptokeys_item = Cryptokey.from_dict(cryptokeys_item_data)

            cryptokeys.append(cryptokeys_item)

        cryptokeys_data = cls(
            cryptokeys=cryptokeys,
        )

        return cryptokeys_data
