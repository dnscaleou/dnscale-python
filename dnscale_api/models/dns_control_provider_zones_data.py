from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.dns_control_provider_zone import DNSControlProviderZone


T = TypeVar("T", bound="DNSControlProviderZonesData")


@_attrs_define
class DNSControlProviderZonesData:
    """
    Attributes:
        zones (list[DNSControlProviderZone]):
    """

    zones: list[DNSControlProviderZone]

    def to_dict(self) -> dict[str, Any]:
        zones = []
        for zones_item_data in self.zones:
            zones_item = zones_item_data.to_dict()
            zones.append(zones_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "zones": zones,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_provider_zone import DNSControlProviderZone

        d = dict(src_dict)
        zones = []
        _zones = d.pop("zones")
        for zones_item_data in _zones:
            zones_item = DNSControlProviderZone.from_dict(zones_item_data)

            zones.append(zones_item)

        dns_control_provider_zones_data = cls(
            zones=zones,
        )

        return dns_control_provider_zones_data
