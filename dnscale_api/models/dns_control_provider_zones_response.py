from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.dns_control_provider_zones_response_status import (
    DNSControlProviderZonesResponseStatus,
)

if TYPE_CHECKING:
    from ..models.dns_control_provider_zones_data import DNSControlProviderZonesData


T = TypeVar("T", bound="DNSControlProviderZonesResponse")


@_attrs_define
class DNSControlProviderZonesResponse:
    """
    Attributes:
        status (DNSControlProviderZonesResponseStatus):
        data (DNSControlProviderZonesData):
    """

    status: DNSControlProviderZonesResponseStatus
    data: DNSControlProviderZonesData

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_provider_zones_data import DNSControlProviderZonesData

        d = dict(src_dict)
        status = DNSControlProviderZonesResponseStatus(d.pop("status"))

        data = DNSControlProviderZonesData.from_dict(d.pop("data"))

        dns_control_provider_zones_response = cls(
            status=status,
            data=data,
        )

        return dns_control_provider_zones_response
