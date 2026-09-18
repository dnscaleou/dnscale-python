from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DNSControlProviderZoneRequest")


@_attrs_define
class DNSControlProviderZoneRequest:
    """
    Attributes:
        zone_name (str | Unset):
    """

    zone_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        zone_name = self.zone_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if zone_name is not UNSET:
            field_dict["zone_name"] = zone_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        zone_name = d.pop("zone_name", UNSET)

        dns_control_provider_zone_request = cls(
            zone_name=zone_name,
        )

        return dns_control_provider_zone_request
