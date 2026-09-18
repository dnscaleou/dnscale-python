from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.dns_control_inventory import DNSControlInventory


T = TypeVar("T", bound="DNSControlInventoryListData")


@_attrs_define
class DNSControlInventoryListData:
    """
    Attributes:
        inventory (list[DNSControlInventory]):
    """

    inventory: list[DNSControlInventory]

    def to_dict(self) -> dict[str, Any]:
        inventory = []
        for inventory_item_data in self.inventory:
            inventory_item = inventory_item_data.to_dict()
            inventory.append(inventory_item)

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
        inventory = []
        _inventory = d.pop("inventory")
        for inventory_item_data in _inventory:
            inventory_item = DNSControlInventory.from_dict(inventory_item_data)

            inventory.append(inventory_item)

        dns_control_inventory_list_data = cls(
            inventory=inventory,
        )

        return dns_control_inventory_list_data
