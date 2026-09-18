from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.dns_control_snapshot_diff_response_status import DNSControlSnapshotDiffResponseStatus

if TYPE_CHECKING:
    from ..models.dns_control_snapshot_diff_data import DNSControlSnapshotDiffData


T = TypeVar("T", bound="DNSControlSnapshotDiffResponse")


@_attrs_define
class DNSControlSnapshotDiffResponse:
    """
    Attributes:
        status (DNSControlSnapshotDiffResponseStatus):
        data (DNSControlSnapshotDiffData):
    """

    status: DNSControlSnapshotDiffResponseStatus
    data: DNSControlSnapshotDiffData

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
        from ..models.dns_control_snapshot_diff_data import DNSControlSnapshotDiffData

        d = dict(src_dict)
        status = DNSControlSnapshotDiffResponseStatus(d.pop("status"))

        data = DNSControlSnapshotDiffData.from_dict(d.pop("data"))

        dns_control_snapshot_diff_response = cls(
            status=status,
            data=data,
        )

        return dns_control_snapshot_diff_response
