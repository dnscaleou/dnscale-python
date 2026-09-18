from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.dns_control_connection import DNSControlConnection


T = TypeVar("T", bound="DNSControlConnectionData")


@_attrs_define
class DNSControlConnectionData:
    """
    Attributes:
        connection (DNSControlConnection):
    """

    connection: DNSControlConnection

    def to_dict(self) -> dict[str, Any]:
        connection = self.connection.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "connection": connection,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_connection import DNSControlConnection

        d = dict(src_dict)
        connection = DNSControlConnection.from_dict(d.pop("connection"))

        dns_control_connection_data = cls(
            connection=connection,
        )

        return dns_control_connection_data
