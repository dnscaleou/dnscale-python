from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.dns_control_snapshot_diff import DNSControlSnapshotDiff


T = TypeVar("T", bound="DNSControlSnapshotDiffData")


@_attrs_define
class DNSControlSnapshotDiffData:
    """
    Attributes:
        diff (DNSControlSnapshotDiff):
    """

    diff: DNSControlSnapshotDiff

    def to_dict(self) -> dict[str, Any]:
        diff = self.diff.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "diff": diff,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_snapshot_diff import DNSControlSnapshotDiff

        d = dict(src_dict)
        diff = DNSControlSnapshotDiff.from_dict(d.pop("diff"))

        dns_control_snapshot_diff_data = cls(
            diff=diff,
        )

        return dns_control_snapshot_diff_data
