from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.dns_control_providers_response_status import DNSControlProvidersResponseStatus

if TYPE_CHECKING:
    from ..models.dns_control_providers_data import DNSControlProvidersData


T = TypeVar("T", bound="DNSControlProvidersResponse")


@_attrs_define
class DNSControlProvidersResponse:
    """
    Attributes:
        status (DNSControlProvidersResponseStatus):
        data (DNSControlProvidersData):
    """

    status: DNSControlProvidersResponseStatus
    data: DNSControlProvidersData

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
        from ..models.dns_control_providers_data import DNSControlProvidersData

        d = dict(src_dict)
        status = DNSControlProvidersResponseStatus(d.pop("status"))

        data = DNSControlProvidersData.from_dict(d.pop("data"))

        dns_control_providers_response = cls(
            status=status,
            data=data,
        )

        return dns_control_providers_response
