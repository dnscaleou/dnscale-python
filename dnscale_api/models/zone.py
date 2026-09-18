from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.zone_region import ZoneRegion
from ..models.zone_status import ZoneStatus
from ..models.zone_type import ZoneType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.zone_settings_brief import ZoneSettingsBrief


T = TypeVar("T", bound="Zone")


@_attrs_define
class Zone:
    """
    Attributes:
        id (UUID):
        customer_id (UUID):
        name (str):  Example: example.com.
        type_ (ZoneType): PowerDNS zone kind. `master` is the default for newly created zones.
        region (ZoneRegion):
        status (ZoneStatus):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        settings (ZoneSettingsBrief | Unset):
    """

    id: UUID
    customer_id: UUID
    name: str
    type_: ZoneType
    region: ZoneRegion
    status: ZoneStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    settings: ZoneSettingsBrief | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        customer_id = str(self.customer_id)

        name = self.name

        type_ = self.type_.value

        region = self.region.value

        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "customer_id": customer_id,
                "name": name,
                "type": type_,
                "region": region,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.zone_settings_brief import ZoneSettingsBrief

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        customer_id = UUID(d.pop("customer_id"))

        name = d.pop("name")

        type_ = ZoneType(d.pop("type"))

        region = ZoneRegion(d.pop("region"))

        status = ZoneStatus(d.pop("status"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        _settings = d.pop("settings", UNSET)
        settings: ZoneSettingsBrief | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = ZoneSettingsBrief.from_dict(_settings)

        zone = cls(
            id=id,
            customer_id=customer_id,
            name=name,
            type_=type_,
            region=region,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            settings=settings,
        )

        return zone
