from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.dns_control_snapshot_diff_change import DNSControlSnapshotDiffChange
    from ..models.dns_control_snapshot_diff_summary import DNSControlSnapshotDiffSummary


T = TypeVar("T", bound="DNSControlSnapshotDiff")


@_attrs_define
class DNSControlSnapshotDiff:
    """
    Attributes:
        from_snapshot_id (UUID):
        to_snapshot_id (UUID):
        summary (DNSControlSnapshotDiffSummary):
        changes (list[DNSControlSnapshotDiffChange]):
    """

    from_snapshot_id: UUID
    to_snapshot_id: UUID
    summary: DNSControlSnapshotDiffSummary
    changes: list[DNSControlSnapshotDiffChange]

    def to_dict(self) -> dict[str, Any]:
        from_snapshot_id = str(self.from_snapshot_id)

        to_snapshot_id = str(self.to_snapshot_id)

        summary = self.summary.to_dict()

        changes = []
        for changes_item_data in self.changes:
            changes_item = changes_item_data.to_dict()
            changes.append(changes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "from_snapshot_id": from_snapshot_id,
                "to_snapshot_id": to_snapshot_id,
                "summary": summary,
                "changes": changes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_snapshot_diff_change import DNSControlSnapshotDiffChange
        from ..models.dns_control_snapshot_diff_summary import DNSControlSnapshotDiffSummary

        d = dict(src_dict)
        from_snapshot_id = UUID(d.pop("from_snapshot_id"))

        to_snapshot_id = UUID(d.pop("to_snapshot_id"))

        summary = DNSControlSnapshotDiffSummary.from_dict(d.pop("summary"))

        changes = []
        _changes = d.pop("changes")
        for changes_item_data in _changes:
            changes_item = DNSControlSnapshotDiffChange.from_dict(changes_item_data)

            changes.append(changes_item)

        dns_control_snapshot_diff = cls(
            from_snapshot_id=from_snapshot_id,
            to_snapshot_id=to_snapshot_id,
            summary=summary,
            changes=changes,
        )

        return dns_control_snapshot_diff
