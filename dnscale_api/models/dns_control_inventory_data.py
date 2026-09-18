from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.dns_control_inventory import DNSControlInventory


T = TypeVar("T", bound="DNSControlInventoryData")


@_attrs_define
class DNSControlInventoryData:
    """
    Attributes:
        inventory (DNSControlInventory):
    """

    inventory: DNSControlInventory

    def to_dict(self) -> dict[str, Any]:
        inventory = self.inventory.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "inventory": inventory,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_inventory import DNSControlInventory

        d = dict(src_dict)
        inventory = DNSControlInventory.from_dict(d.pop("inventory"))

        dns_control_inventory_data = cls(
            inventory=inventory,
        )

        return dns_control_inventory_data
