from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.dnssec_status_response_status import DNSSECStatusResponseStatus

if TYPE_CHECKING:
    from ..models.dnssec_status_data import DNSSECStatusData


T = TypeVar("T", bound="DNSSECStatusResponse")


@_attrs_define
class DNSSECStatusResponse:
    """
    Attributes:
        status (DNSSECStatusResponseStatus):
        data (DNSSECStatusData):
    """

    status: DNSSECStatusResponseStatus
    data: DNSSECStatusData

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
        from ..models.dnssec_status_data import DNSSECStatusData

        d = dict(src_dict)
        status = DNSSECStatusResponseStatus(d.pop("status"))

        data = DNSSECStatusData.from_dict(d.pop("data"))

        dnssec_status_response = cls(
            status=status,
            data=data,
        )

        return dnssec_status_response
