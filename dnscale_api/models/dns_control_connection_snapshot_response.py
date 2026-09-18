from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.dns_control_connection_snapshot_response_status import (
    DNSControlConnectionSnapshotResponseStatus,
)

if TYPE_CHECKING:
    from ..models.dns_control_connection_snapshot_data import DNSControlConnectionSnapshotData


T = TypeVar("T", bound="DNSControlConnectionSnapshotResponse")


@_attrs_define
class DNSControlConnectionSnapshotResponse:
    """
    Attributes:
        status (DNSControlConnectionSnapshotResponseStatus):
        data (DNSControlConnectionSnapshotData):
    """

    status: DNSControlConnectionSnapshotResponseStatus
    data: DNSControlConnectionSnapshotData

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
        from ..models.dns_control_connection_snapshot_data import DNSControlConnectionSnapshotData

        d = dict(src_dict)
        status = DNSControlConnectionSnapshotResponseStatus(d.pop("status"))

        data = DNSControlConnectionSnapshotData.from_dict(d.pop("data"))

        dns_control_connection_snapshot_response = cls(
            status=status,
            data=data,
        )

        return dns_control_connection_snapshot_response
