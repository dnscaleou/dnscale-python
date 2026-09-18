from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.dns_control_snapshot_source_kind import DNSControlSnapshotSourceKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_control_record_set import DNSControlRecordSet
    from ..models.dns_control_snapshot_canonical_zone import DNSControlSnapshotCanonicalZone


T = TypeVar("T", bound="DNSControlSnapshot")


@_attrs_define
class DNSControlSnapshot:
    """
    Attributes:
        id (UUID):
        zone_inventory_id (UUID):
        captured_at (datetime.datetime):
        source_kind (DNSControlSnapshotSourceKind):
        source_version (str):
        canonical_zone (DNSControlSnapshotCanonicalZone):
        portable_hash (str):
        provider_hash (str):
        record_set_count (int):
        record_sets (list[DNSControlRecordSet] | Unset):
    """

    id: UUID
    zone_inventory_id: UUID
    captured_at: datetime.datetime
    source_kind: DNSControlSnapshotSourceKind
    source_version: str
    canonical_zone: DNSControlSnapshotCanonicalZone
    portable_hash: str
    provider_hash: str
    record_set_count: int
    record_sets: list[DNSControlRecordSet] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        zone_inventory_id = str(self.zone_inventory_id)

        captured_at = self.captured_at.isoformat()

        source_kind = self.source_kind.value

        source_version = self.source_version

        canonical_zone = self.canonical_zone.to_dict()

        portable_hash = self.portable_hash

        provider_hash = self.provider_hash

        record_set_count = self.record_set_count

        record_sets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.record_sets, Unset):
            record_sets = []
            for record_sets_item_data in self.record_sets:
                record_sets_item = record_sets_item_data.to_dict()
                record_sets.append(record_sets_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "zone_inventory_id": zone_inventory_id,
                "captured_at": captured_at,
                "source_kind": source_kind,
                "source_version": source_version,
                "canonical_zone": canonical_zone,
                "portable_hash": portable_hash,
                "provider_hash": provider_hash,
                "record_set_count": record_set_count,
            }
        )
        if record_sets is not UNSET:
            field_dict["record_sets"] = record_sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_record_set import DNSControlRecordSet
        from ..models.dns_control_snapshot_canonical_zone import DNSControlSnapshotCanonicalZone

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        zone_inventory_id = UUID(d.pop("zone_inventory_id"))

        captured_at = isoparse(d.pop("captured_at"))

        source_kind = DNSControlSnapshotSourceKind(d.pop("source_kind"))

        source_version = d.pop("source_version")

        canonical_zone = DNSControlSnapshotCanonicalZone.from_dict(d.pop("canonical_zone"))

        portable_hash = d.pop("portable_hash")

        provider_hash = d.pop("provider_hash")

        record_set_count = d.pop("record_set_count")

        _record_sets = d.pop("record_sets", UNSET)
        record_sets: list[DNSControlRecordSet] | Unset = UNSET
        if _record_sets is not UNSET:
            record_sets = []
            for record_sets_item_data in _record_sets:
                record_sets_item = DNSControlRecordSet.from_dict(record_sets_item_data)

                record_sets.append(record_sets_item)

        dns_control_snapshot = cls(
            id=id,
            zone_inventory_id=zone_inventory_id,
            captured_at=captured_at,
            source_kind=source_kind,
            source_version=source_version,
            canonical_zone=canonical_zone,
            portable_hash=portable_hash,
            provider_hash=provider_hash,
            record_set_count=record_set_count,
            record_sets=record_sets,
        )

        return dns_control_snapshot
