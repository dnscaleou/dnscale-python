from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Pagination")


@_attrs_define
class Pagination:
    """
    Attributes:
        total (int):
        offset (int):
        limit (int):
        count (int):
        has_more (bool):
    """

    total: int
    offset: int
    limit: int
    count: int
    has_more: bool

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        offset = self.offset

        limit = self.limit

        count = self.count

        has_more = self.has_more

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total": total,
                "offset": offset,
                "limit": limit,
                "count": count,
                "has_more": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        offset = d.pop("offset")

        limit = d.pop("limit")

        count = d.pop("count")

        has_more = d.pop("has_more")

        pagination = cls(
            total=total,
            offset=offset,
            limit=limit,
            count=count,
            has_more=has_more,
        )

        return pagination
