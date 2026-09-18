from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.api_key import APIKey


T = TypeVar("T", bound="APIKeyData")


@_attrs_define
class APIKeyData:
    """
    Attributes:
        api_key (APIKey):
    """

    api_key: APIKey

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "api_key": api_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key import APIKey

        d = dict(src_dict)
        api_key = APIKey.from_dict(d.pop("api_key"))

        api_key_data = cls(
            api_key=api_key,
        )

        return api_key_data
