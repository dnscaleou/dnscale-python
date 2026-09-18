from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.api_key import APIKey


T = TypeVar("T", bound="APIKeysData")


@_attrs_define
class APIKeysData:
    """
    Attributes:
        api_keys (list[APIKey]):
    """

    api_keys: list[APIKey]

    def to_dict(self) -> dict[str, Any]:
        api_keys = []
        for api_keys_item_data in self.api_keys:
            api_keys_item = api_keys_item_data.to_dict()
            api_keys.append(api_keys_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "api_keys": api_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key import APIKey

        d = dict(src_dict)
        api_keys = []
        _api_keys = d.pop("api_keys")
        for api_keys_item_data in _api_keys:
            api_keys_item = APIKey.from_dict(api_keys_item_data)

            api_keys.append(api_keys_item)

        api_keys_data = cls(
            api_keys=api_keys,
        )

        return api_keys_data
