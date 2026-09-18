from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.dns_control_connection_response_status import DNSControlConnectionResponseStatus

if TYPE_CHECKING:
    from ..models.dns_control_connection_data import DNSControlConnectionData


T = TypeVar("T", bound="DNSControlConnectionResponse")


@_attrs_define
class DNSControlConnectionResponse:
    """
    Attributes:
        status (DNSControlConnectionResponseStatus):
        data (DNSControlConnectionData):
    """

    status: DNSControlConnectionResponseStatus
    data: DNSControlConnectionData

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
        from ..models.dns_control_connection_data import DNSControlConnectionData

        d = dict(src_dict)
        status = DNSControlConnectionResponseStatus(d.pop("status"))

        data = DNSControlConnectionData.from_dict(d.pop("data"))

        dns_control_connection_response = cls(
            status=status,
            data=data,
        )

        return dns_control_connection_response
