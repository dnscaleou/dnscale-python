from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DNSSECStatusData")


@_attrs_define
class DNSSECStatusData:
    """
    Attributes:
        dnssec (bool):
    """

    dnssec: bool

    def to_dict(self) -> dict[str, Any]:
        dnssec = self.dnssec

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dnssec": dnssec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dnssec = d.pop("dnssec")

        dnssec_status_data = cls(
            dnssec=dnssec,
        )

        return dnssec_status_data
