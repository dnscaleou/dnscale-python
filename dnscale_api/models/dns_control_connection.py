from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.dns_control_connection_mode import DNSControlConnectionMode
from ..models.dns_control_connection_status import DNSControlConnectionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_control_provider_capabilities import DNSControlProviderCapabilities


T = TypeVar("T", bound="DNSControlConnection")


@_attrs_define
class DNSControlConnection:
    """
    Attributes:
        id (UUID):
        provider (str):
        name (str):
        mode (DNSControlConnectionMode):
        scopes (list[str]):
        status (DNSControlConnectionStatus):
        capabilities (DNSControlProviderCapabilities):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        last_verified_at (datetime.datetime | None | Unset):
        last_successful_inventory_at (datetime.datetime | None | Unset):
        disabled_at (datetime.datetime | None | Unset):
    """

    id: UUID
    provider: str
    name: str
    mode: DNSControlConnectionMode
    scopes: list[str]
    status: DNSControlConnectionStatus
    capabilities: DNSControlProviderCapabilities
    created_at: datetime.datetime
    updated_at: datetime.datetime
    last_verified_at: datetime.datetime | None | Unset = UNSET
    last_successful_inventory_at: datetime.datetime | None | Unset = UNSET
    disabled_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        provider = self.provider

        name = self.name

        mode = self.mode.value

        scopes = self.scopes

        status = self.status.value

        capabilities = self.capabilities.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        last_verified_at: None | str | Unset
        if isinstance(self.last_verified_at, Unset):
            last_verified_at = UNSET
        elif isinstance(self.last_verified_at, datetime.datetime):
            last_verified_at = self.last_verified_at.isoformat()
        else:
            last_verified_at = self.last_verified_at

        last_successful_inventory_at: None | str | Unset
        if isinstance(self.last_successful_inventory_at, Unset):
            last_successful_inventory_at = UNSET
        elif isinstance(self.last_successful_inventory_at, datetime.datetime):
            last_successful_inventory_at = self.last_successful_inventory_at.isoformat()
        else:
            last_successful_inventory_at = self.last_successful_inventory_at

        disabled_at: None | str | Unset
        if isinstance(self.disabled_at, Unset):
            disabled_at = UNSET
        elif isinstance(self.disabled_at, datetime.datetime):
            disabled_at = self.disabled_at.isoformat()
        else:
            disabled_at = self.disabled_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "provider": provider,
                "name": name,
                "mode": mode,
                "scopes": scopes,
                "status": status,
                "capabilities": capabilities,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if last_verified_at is not UNSET:
            field_dict["last_verified_at"] = last_verified_at
        if last_successful_inventory_at is not UNSET:
            field_dict["last_successful_inventory_at"] = last_successful_inventory_at
        if disabled_at is not UNSET:
            field_dict["disabled_at"] = disabled_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_provider_capabilities import DNSControlProviderCapabilities

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        provider = d.pop("provider")

        name = d.pop("name")

        mode = DNSControlConnectionMode(d.pop("mode"))

        scopes = cast(list[str], d.pop("scopes"))

        status = DNSControlConnectionStatus(d.pop("status"))

        capabilities = DNSControlProviderCapabilities.from_dict(d.pop("capabilities"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_last_verified_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_verified_at_type_0 = isoparse(data)

                return last_verified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_verified_at = _parse_last_verified_at(d.pop("last_verified_at", UNSET))

        def _parse_last_successful_inventory_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_successful_inventory_at_type_0 = isoparse(data)

                return last_successful_inventory_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_successful_inventory_at = _parse_last_successful_inventory_at(d.pop("last_successful_inventory_at", UNSET))

        def _parse_disabled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                disabled_at_type_0 = isoparse(data)

                return disabled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        disabled_at = _parse_disabled_at(d.pop("disabled_at", UNSET))

        dns_control_connection = cls(
            id=id,
            provider=provider,
            name=name,
            mode=mode,
            scopes=scopes,
            status=status,
            capabilities=capabilities,
            created_at=created_at,
            updated_at=updated_at,
            last_verified_at=last_verified_at,
            last_successful_inventory_at=last_successful_inventory_at,
            disabled_at=disabled_at,
        )

        return dns_control_connection
