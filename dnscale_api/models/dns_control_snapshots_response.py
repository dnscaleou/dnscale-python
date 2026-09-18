from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.dns_control_snapshots_response_status import DNSControlSnapshotsResponseStatus

if TYPE_CHECKING:
    from ..models.dns_control_snapshots_data import DNSControlSnapshotsData


T = TypeVar("T", bound="DNSControlSnapshotsResponse")


@_attrs_define
class DNSControlSnapshotsResponse:
    """
    Attributes:
        status (DNSControlSnapshotsResponseStatus):
        data (DNSControlSnapshotsData):
    """

    status: DNSControlSnapshotsResponseStatus
    data: DNSControlSnapshotsData

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
        from ..models.dns_control_snapshots_data import DNSControlSnapshotsData

        d = dict(src_dict)
        status = DNSControlSnapshotsResponseStatus(d.pop("status"))

        data = DNSControlSnapshotsData.from_dict(d.pop("data"))

        dns_control_snapshots_response = cls(
            status=status,
            data=data,
        )

        return dns_control_snapshots_response
