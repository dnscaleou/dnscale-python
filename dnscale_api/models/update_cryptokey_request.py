from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCryptokeyRequest")


@_attrs_define
class UpdateCryptokeyRequest:
    """
    Attributes:
        active (bool | Unset):
        published (bool | Unset):
    """

    active: bool | Unset = UNSET
    published: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        published = self.published

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if published is not UNSET:
            field_dict["published"] = published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active", UNSET)

        published = d.pop("published", UNSET)

        update_cryptokey_request = cls(
            active=active,
            published=published,
        )

        return update_cryptokey_request
