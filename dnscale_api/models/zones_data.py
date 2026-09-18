from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.zone import Zone


T = TypeVar("T", bound="ZonesData")


@_attrs_define
class ZonesData:
    """
    Attributes:
        zones (list[Zone]):
        pagination (Pagination):
    """

    zones: list[Zone]
    pagination: Pagination

    def to_dict(self) -> dict[str, Any]:
        zones = []
        for zones_item_data in self.zones:
            zones_item = zones_item_data.to_dict()
            zones.append(zones_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "zones": zones,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.zone import Zone

        d = dict(src_dict)
        zones = []
        _zones = d.pop("zones")
        for zones_item_data in _zones:
            zones_item = Zone.from_dict(zones_item_data)

            zones.append(zones_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        zones_data = cls(
            zones=zones,
            pagination=pagination,
        )

        return zones_data
