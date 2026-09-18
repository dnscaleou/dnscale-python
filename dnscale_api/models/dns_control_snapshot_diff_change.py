from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dns_control_snapshot_diff_change_severity import DNSControlSnapshotDiffChangeSeverity
from ..models.dns_control_snapshot_diff_change_type import DNSControlSnapshotDiffChangeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_control_snapshot_diff_change_after import DNSControlSnapshotDiffChangeAfter
    from ..models.dns_control_snapshot_diff_change_before import DNSControlSnapshotDiffChangeBefore


T = TypeVar("T", bound="DNSControlSnapshotDiffChange")


@_attrs_define
class DNSControlSnapshotDiffChange:
    """
    Attributes:
        type_ (DNSControlSnapshotDiffChangeType):
        record_set_key (str):
        owner_name (str):
        rrtype (str):
        severity (DNSControlSnapshotDiffChangeSeverity):
        before (DNSControlSnapshotDiffChangeBefore | Unset):
        after (DNSControlSnapshotDiffChangeAfter | Unset):
        warnings (list[str] | Unset):
    """

    type_: DNSControlSnapshotDiffChangeType
    record_set_key: str
    owner_name: str
    rrtype: str
    severity: DNSControlSnapshotDiffChangeSeverity
    before: DNSControlSnapshotDiffChangeBefore | Unset = UNSET
    after: DNSControlSnapshotDiffChangeAfter | Unset = UNSET
    warnings: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        record_set_key = self.record_set_key

        owner_name = self.owner_name

        rrtype = self.rrtype

        severity = self.severity.value

        before: dict[str, Any] | Unset = UNSET
        if not isinstance(self.before, Unset):
            before = self.before.to_dict()

        after: dict[str, Any] | Unset = UNSET
        if not isinstance(self.after, Unset):
            after = self.after.to_dict()

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "record_set_key": record_set_key,
                "owner_name": owner_name,
                "rrtype": rrtype,
                "severity": severity,
            }
        )
        if before is not UNSET:
            field_dict["before"] = before
        if after is not UNSET:
            field_dict["after"] = after
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_snapshot_diff_change_after import (
            DNSControlSnapshotDiffChangeAfter,
        )
        from ..models.dns_control_snapshot_diff_change_before import (
            DNSControlSnapshotDiffChangeBefore,
        )

        d = dict(src_dict)
        type_ = DNSControlSnapshotDiffChangeType(d.pop("type"))

        record_set_key = d.pop("record_set_key")

        owner_name = d.pop("owner_name")

        rrtype = d.pop("rrtype")

        severity = DNSControlSnapshotDiffChangeSeverity(d.pop("severity"))

        _before = d.pop("before", UNSET)
        before: DNSControlSnapshotDiffChangeBefore | Unset
        if isinstance(_before, Unset):
            before = UNSET
        else:
            before = DNSControlSnapshotDiffChangeBefore.from_dict(_before)

        _after = d.pop("after", UNSET)
        after: DNSControlSnapshotDiffChangeAfter | Unset
        if isinstance(_after, Unset):
            after = UNSET
        else:
            after = DNSControlSnapshotDiffChangeAfter.from_dict(_after)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        dns_control_snapshot_diff_change = cls(
            type_=type_,
            record_set_key=record_set_key,
            owner_name=owner_name,
            rrtype=rrtype,
            severity=severity,
            before=before,
            after=after,
            warnings=warnings,
        )

        return dns_control_snapshot_diff_change
