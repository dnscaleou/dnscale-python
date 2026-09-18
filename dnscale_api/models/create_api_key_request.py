from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key_zone_scope import APIKeyZoneScope


T = TypeVar("T", bound="CreateAPIKeyRequest")


@_attrs_define
class CreateAPIKeyRequest:
    """
    Attributes:
        name (str):
        scopes (str): JSON-encoded array of scope names. Example:
            ["zones:read","zones:write","records:read","records:write"].
        expires_at (datetime.datetime | None | Unset):
        zone_ids (list[UUID] | Unset): Compatibility zone list.
            Grants all DNS names in every listed zone.
            Mutually exclusive with a non-empty `zone_scopes` value. Empty or
            omitted together with `zone_scopes` creates a customer-wide key.
        zone_scopes (list[APIKeyZoneScope] | Unset): Preferred per-zone resource policy.
            Each zone can grant all DNS names or up to 100 exact owner names;
            a key can contain at most 500 names total.
            Mutually exclusive with a non-empty `zone_ids` value.
    """

    name: str
    scopes: str
    expires_at: datetime.datetime | None | Unset = UNSET
    zone_ids: list[UUID] | Unset = UNSET
    zone_scopes: list[APIKeyZoneScope] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        scopes = self.scopes

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        zone_ids: list[str] | Unset = UNSET
        if not isinstance(self.zone_ids, Unset):
            zone_ids = []
            for zone_ids_item_data in self.zone_ids:
                zone_ids_item = str(zone_ids_item_data)
                zone_ids.append(zone_ids_item)

        zone_scopes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.zone_scopes, Unset):
            zone_scopes = []
            for zone_scopes_item_data in self.zone_scopes:
                zone_scopes_item = zone_scopes_item_data.to_dict()
                zone_scopes.append(zone_scopes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "scopes": scopes,
            }
        )
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if zone_ids is not UNSET:
            field_dict["zone_ids"] = zone_ids
        if zone_scopes is not UNSET:
            field_dict["zone_scopes"] = zone_scopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_zone_scope import APIKeyZoneScope

        d = dict(src_dict)
        name = d.pop("name")

        scopes = d.pop("scopes")

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        _zone_ids = d.pop("zone_ids", UNSET)
        zone_ids: list[UUID] | Unset = UNSET
        if _zone_ids is not UNSET:
            zone_ids = []
            for zone_ids_item_data in _zone_ids:
                zone_ids_item = UUID(zone_ids_item_data)

                zone_ids.append(zone_ids_item)

        _zone_scopes = d.pop("zone_scopes", UNSET)
        zone_scopes: list[APIKeyZoneScope] | Unset = UNSET
        if _zone_scopes is not UNSET:
            zone_scopes = []
            for zone_scopes_item_data in _zone_scopes:
                zone_scopes_item = APIKeyZoneScope.from_dict(zone_scopes_item_data)

                zone_scopes.append(zone_scopes_item)

        create_api_key_request = cls(
            name=name,
            scopes=scopes,
            expires_at=expires_at,
            zone_ids=zone_ids,
            zone_scopes=zone_scopes,
        )

        return create_api_key_request
