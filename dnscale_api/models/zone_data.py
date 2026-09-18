from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.zone import Zone


T = TypeVar("T", bound="ZoneData")


@_attrs_define
class ZoneData:
    """
    Attributes:
        zone (Zone):
    """

    zone: Zone

    def to_dict(self) -> dict[str, Any]:
        zone = self.zone.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "zone": zone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.zone import Zone

        d = dict(src_dict)
        zone = Zone.from_dict(d.pop("zone"))

        zone_data = cls(
            zone=zone,
        )

        return zone_data
