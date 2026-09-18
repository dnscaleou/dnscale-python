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


T = TypeVar("T", bound="APIKey")


@_attrs_define
class APIKey:
    """
    Attributes:
        id (UUID):
        customer_id (UUID):
        user_id (UUID):
        name (str):
        scopes (str): JSON-encoded scope-name array. Example: ["zones:read","records:read"].
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        zone_ids (list[UUID]): Compatibility zone list. Empty means customer-wide.
        zone_scopes (list[APIKeyZoneScope]): Per-zone resource policy. Empty means customer-wide.
        key (str | Unset): Secret API key. Present only in the create response.
        expires_at (datetime.datetime | None | Unset):
    """

    id: UUID
    customer_id: UUID
    user_id: UUID
    name: str
    scopes: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    zone_ids: list[UUID]
    zone_scopes: list[APIKeyZoneScope]
    key: str | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        customer_id = str(self.customer_id)

        user_id = str(self.user_id)

        name = self.name

        scopes = self.scopes

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        zone_ids = []
        for zone_ids_item_data in self.zone_ids:
            zone_ids_item = str(zone_ids_item_data)
            zone_ids.append(zone_ids_item)

        zone_scopes = []
        for zone_scopes_item_data in self.zone_scopes:
            zone_scopes_item = zone_scopes_item_data.to_dict()
            zone_scopes.append(zone_scopes_item)

        key = self.key

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "customer_id": customer_id,
                "user_id": user_id,
                "name": name,
                "scopes": scopes,
                "created_at": created_at,
                "updated_at": updated_at,
                "zone_ids": zone_ids,
                "zone_scopes": zone_scopes,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_zone_scope import APIKeyZoneScope

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        customer_id = UUID(d.pop("customer_id"))

        user_id = UUID(d.pop("user_id"))

        name = d.pop("name")

        scopes = d.pop("scopes")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        zone_ids = []
        _zone_ids = d.pop("zone_ids")
        for zone_ids_item_data in _zone_ids:
            zone_ids_item = UUID(zone_ids_item_data)

            zone_ids.append(zone_ids_item)

        zone_scopes = []
        _zone_scopes = d.pop("zone_scopes")
        for zone_scopes_item_data in _zone_scopes:
            zone_scopes_item = APIKeyZoneScope.from_dict(zone_scopes_item_data)

            zone_scopes.append(zone_scopes_item)

        key = d.pop("key", UNSET)

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

        api_key = cls(
            id=id,
            customer_id=customer_id,
            user_id=user_id,
            name=name,
            scopes=scopes,
            created_at=created_at,
            updated_at=updated_at,
            zone_ids=zone_ids,
            zone_scopes=zone_scopes,
            key=key,
            expires_at=expires_at,
        )

        return api_key
