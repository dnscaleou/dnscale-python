from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.dns_control_inventory import DNSControlInventory
    from ..models.dns_control_snapshot import DNSControlSnapshot


T = TypeVar("T", bound="DNSControlConnectionSnapshotData")


@_attrs_define
class DNSControlConnectionSnapshotData:
    """
    Attributes:
        inventory (DNSControlInventory):
        snapshot (DNSControlSnapshot):
    """

    inventory: DNSControlInventory
    snapshot: DNSControlSnapshot

    def to_dict(self) -> dict[str, Any]:
        inventory = self.inventory.to_dict()

        snapshot = self.snapshot.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "inventory": inventory,
                "snapshot": snapshot,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_inventory import DNSControlInventory
        from ..models.dns_control_snapshot import DNSControlSnapshot

        d = dict(src_dict)
        inventory = DNSControlInventory.from_dict(d.pop("inventory"))

        snapshot = DNSControlSnapshot.from_dict(d.pop("snapshot"))

        dns_control_connection_snapshot_data = cls(
            inventory=inventory,
            snapshot=snapshot,
        )

        return dns_control_connection_snapshot_data
