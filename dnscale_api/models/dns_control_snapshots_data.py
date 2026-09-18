from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.dns_control_snapshot import DNSControlSnapshot
    from ..models.offset_meta import OffsetMeta


T = TypeVar("T", bound="DNSControlSnapshotsData")


@_attrs_define
class DNSControlSnapshotsData:
    """
    Attributes:
        snapshots (list[DNSControlSnapshot]):
        meta (OffsetMeta):
    """

    snapshots: list[DNSControlSnapshot]
    meta: OffsetMeta

    def to_dict(self) -> dict[str, Any]:
        snapshots = []
        for snapshots_item_data in self.snapshots:
            snapshots_item = snapshots_item_data.to_dict()
            snapshots.append(snapshots_item)

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "snapshots": snapshots,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_snapshot import DNSControlSnapshot
        from ..models.offset_meta import OffsetMeta

        d = dict(src_dict)
        snapshots = []
        _snapshots = d.pop("snapshots")
        for snapshots_item_data in _snapshots:
            snapshots_item = DNSControlSnapshot.from_dict(snapshots_item_data)

            snapshots.append(snapshots_item)

        meta = OffsetMeta.from_dict(d.pop("meta"))

        dns_control_snapshots_data = cls(
            snapshots=snapshots,
            meta=meta,
        )

        return dns_control_snapshots_data
