from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.dns_control_snapshot_response_status import DNSControlSnapshotResponseStatus

if TYPE_CHECKING:
    from ..models.dns_control_snapshot_data import DNSControlSnapshotData


T = TypeVar("T", bound="DNSControlSnapshotResponse")


@_attrs_define
class DNSControlSnapshotResponse:
    """
    Attributes:
        status (DNSControlSnapshotResponseStatus):
        data (DNSControlSnapshotData):
    """

    status: DNSControlSnapshotResponseStatus
    data: DNSControlSnapshotData

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
        from ..models.dns_control_snapshot_data import DNSControlSnapshotData

        d = dict(src_dict)
        status = DNSControlSnapshotResponseStatus(d.pop("status"))

        data = DNSControlSnapshotData.from_dict(d.pop("data"))

        dns_control_snapshot_response = cls(
            status=status,
            data=data,
        )

        return dns_control_snapshot_response
