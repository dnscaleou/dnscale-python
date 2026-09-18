from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.dns_control_inventory_response_status import DNSControlInventoryResponseStatus

if TYPE_CHECKING:
    from ..models.dns_control_inventory_data import DNSControlInventoryData


T = TypeVar("T", bound="DNSControlInventoryResponse")


@_attrs_define
class DNSControlInventoryResponse:
    """
    Attributes:
        status (DNSControlInventoryResponseStatus):
        data (DNSControlInventoryData):
    """

    status: DNSControlInventoryResponseStatus
    data: DNSControlInventoryData

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
        from ..models.dns_control_inventory_data import DNSControlInventoryData

        d = dict(src_dict)
        status = DNSControlInventoryResponseStatus(d.pop("status"))

        data = DNSControlInventoryData.from_dict(d.pop("data"))

        dns_control_inventory_response = cls(
            status=status,
            data=data,
        )

        return dns_control_inventory_response
