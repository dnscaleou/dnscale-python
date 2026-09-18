from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.dns_control_connection import DNSControlConnection


T = TypeVar("T", bound="DNSControlConnectionsData")


@_attrs_define
class DNSControlConnectionsData:
    """
    Attributes:
        connections (list[DNSControlConnection]):
    """

    connections: list[DNSControlConnection]

    def to_dict(self) -> dict[str, Any]:
        connections = []
        for connections_item_data in self.connections:
            connections_item = connections_item_data.to_dict()
            connections.append(connections_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "connections": connections,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_connection import DNSControlConnection

        d = dict(src_dict)
        connections = []
        _connections = d.pop("connections")
        for connections_item_data in _connections:
            connections_item = DNSControlConnection.from_dict(connections_item_data)

            connections.append(connections_item)

        dns_control_connections_data = cls(
            connections=connections,
        )

        return dns_control_connections_data
