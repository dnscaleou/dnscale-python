from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_control_inventory_delegation import DNSControlInventoryDelegation
    from ..models.dns_control_inventory_dnssec import DNSControlInventoryDnssec


T = TypeVar("T", bound="DNSControlInventory")


@_attrs_define
class DNSControlInventory:
    """
    Attributes:
        id (UUID):
        provider_zone_id (str):
        zone_name (str):
        status (str):
        nameservers (list[str]):
        dnssec (DNSControlInventoryDnssec):
        delegation (DNSControlInventoryDelegation):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        provider_connection_id (None | Unset | UUID):
    """

    id: UUID
    provider_zone_id: str
    zone_name: str
    status: str
    nameservers: list[str]
    dnssec: DNSControlInventoryDnssec
    delegation: DNSControlInventoryDelegation
    created_at: datetime.datetime
    updated_at: datetime.datetime
    provider_connection_id: None | Unset | UUID = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        provider_zone_id = self.provider_zone_id

        zone_name = self.zone_name

        status = self.status

        nameservers = self.nameservers

        dnssec = self.dnssec.to_dict()

        delegation = self.delegation.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        provider_connection_id: None | str | Unset
        if isinstance(self.provider_connection_id, Unset):
            provider_connection_id = UNSET
        elif isinstance(self.provider_connection_id, UUID):
            provider_connection_id = str(self.provider_connection_id)
        else:
            provider_connection_id = self.provider_connection_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "provider_zone_id": provider_zone_id,
                "zone_name": zone_name,
                "status": status,
                "nameservers": nameservers,
                "dnssec": dnssec,
                "delegation": delegation,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if provider_connection_id is not UNSET:
            field_dict["provider_connection_id"] = provider_connection_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_inventory_delegation import DNSControlInventoryDelegation
        from ..models.dns_control_inventory_dnssec import DNSControlInventoryDnssec

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        provider_zone_id = d.pop("provider_zone_id")

        zone_name = d.pop("zone_name")

        status = d.pop("status")

        nameservers = cast(list[str], d.pop("nameservers"))

        dnssec = DNSControlInventoryDnssec.from_dict(d.pop("dnssec"))

        delegation = DNSControlInventoryDelegation.from_dict(d.pop("delegation"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_provider_connection_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                provider_connection_id_type_0 = UUID(data)

                return provider_connection_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        provider_connection_id = _parse_provider_connection_id(d.pop("provider_connection_id", UNSET))

        dns_control_inventory = cls(
            id=id,
            provider_zone_id=provider_zone_id,
            zone_name=zone_name,
            status=status,
            nameservers=nameservers,
            dnssec=dnssec,
            delegation=delegation,
            created_at=created_at,
            updated_at=updated_at,
            provider_connection_id=provider_connection_id,
        )

        return dns_control_inventory
