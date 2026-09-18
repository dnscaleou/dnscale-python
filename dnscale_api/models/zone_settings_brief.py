from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ZoneSettingsBrief")


@_attrs_define
class ZoneSettingsBrief:
    """
    Attributes:
        dnssec_enabled (bool):
    """

    dnssec_enabled: bool

    def to_dict(self) -> dict[str, Any]:
        dnssec_enabled = self.dnssec_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dnssec_enabled": dnssec_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dnssec_enabled = d.pop("dnssec_enabled")

        zone_settings_brief = cls(
            dnssec_enabled=dnssec_enabled,
        )

        return zone_settings_brief
