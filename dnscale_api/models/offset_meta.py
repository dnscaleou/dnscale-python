from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="OffsetMeta")


@_attrs_define
class OffsetMeta:
    """
    Attributes:
        limit (int):
        offset (int):
    """

    limit: int
    offset: int

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "limit": limit,
                "offset": offset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit")

        offset = d.pop("offset")

        offset_meta = cls(
            limit=limit,
            offset=offset,
        )

        return offset_meta
