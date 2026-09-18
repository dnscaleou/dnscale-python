from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DNSControlSnapshotDiffSummary")


@_attrs_define
class DNSControlSnapshotDiffSummary:
    """
    Attributes:
        added_record_sets (int):
        removed_record_sets (int):
        value_changed (int):
        ttl_changed (int):
        provider_metadata_changed (int):
        unsupported_provider_features (int):
    """

    added_record_sets: int
    removed_record_sets: int
    value_changed: int
    ttl_changed: int
    provider_metadata_changed: int
    unsupported_provider_features: int

    def to_dict(self) -> dict[str, Any]:
        added_record_sets = self.added_record_sets

        removed_record_sets = self.removed_record_sets

        value_changed = self.value_changed

        ttl_changed = self.ttl_changed

        provider_metadata_changed = self.provider_metadata_changed

        unsupported_provider_features = self.unsupported_provider_features

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "added_record_sets": added_record_sets,
                "removed_record_sets": removed_record_sets,
                "value_changed": value_changed,
                "ttl_changed": ttl_changed,
                "provider_metadata_changed": provider_metadata_changed,
                "unsupported_provider_features": unsupported_provider_features,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        added_record_sets = d.pop("added_record_sets")

        removed_record_sets = d.pop("removed_record_sets")

        value_changed = d.pop("value_changed")

        ttl_changed = d.pop("ttl_changed")

        provider_metadata_changed = d.pop("provider_metadata_changed")

        unsupported_provider_features = d.pop("unsupported_provider_features")

        dns_control_snapshot_diff_summary = cls(
            added_record_sets=added_record_sets,
            removed_record_sets=removed_record_sets,
            value_changed=value_changed,
            ttl_changed=ttl_changed,
            provider_metadata_changed=provider_metadata_changed,
            unsupported_provider_features=unsupported_provider_features,
        )

        return dns_control_snapshot_diff_summary
