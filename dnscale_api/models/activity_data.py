from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.activity_item import ActivityItem
    from ..models.offset_meta import OffsetMeta


T = TypeVar("T", bound="ActivityData")


@_attrs_define
class ActivityData:
    """
    Attributes:
        items (list[ActivityItem]):
        meta (OffsetMeta):
    """

    items: list[ActivityItem]
    meta: OffsetMeta

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_item import ActivityItem
        from ..models.offset_meta import OffsetMeta

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ActivityItem.from_dict(items_item_data)

            items.append(items_item)

        meta = OffsetMeta.from_dict(d.pop("meta"))

        activity_data = cls(
            items=items,
            meta=meta,
        )

        return activity_data
