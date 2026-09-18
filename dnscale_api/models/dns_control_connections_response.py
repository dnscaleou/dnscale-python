from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.dns_control_connections_response_status import DNSControlConnectionsResponseStatus

if TYPE_CHECKING:
    from ..models.dns_control_connections_data import DNSControlConnectionsData


T = TypeVar("T", bound="DNSControlConnectionsResponse")


@_attrs_define
class DNSControlConnectionsResponse:
    """
    Attributes:
        status (DNSControlConnectionsResponseStatus):
        data (DNSControlConnectionsData):
    """

    status: DNSControlConnectionsResponseStatus
    data: DNSControlConnectionsData

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
        from ..models.dns_control_connections_data import DNSControlConnectionsData

        d = dict(src_dict)
        status = DNSControlConnectionsResponseStatus(d.pop("status"))

        data = DNSControlConnectionsData.from_dict(d.pop("data"))

        dns_control_connections_response = cls(
            status=status,
            data=data,
        )

        return dns_control_connections_response
