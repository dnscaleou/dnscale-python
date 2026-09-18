from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.zone_region import ZoneRegion
from ..models.zone_status import ZoneStatus
from ..models.zone_type import ZoneType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateZoneRequest")


@_attrs_define
class UpdateZoneRequest:
    """The current API requires `name`; omitted type, region, and status values retain their existing values.

    Attributes:
        name (str):
        type_ (ZoneType | Unset): PowerDNS zone kind. `master` is the default for newly created zones.
        region (ZoneRegion | Unset):
        status (ZoneStatus | Unset):
    """

    name: str
    type_: ZoneType | Unset = UNSET
    region: ZoneRegion | Unset = UNSET
    status: ZoneStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        region: str | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if region is not UNSET:
            field_dict["region"] = region
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _type_ = d.pop("type", UNSET)
        type_: ZoneType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ZoneType(_type_)

        _region = d.pop("region", UNSET)
        region: ZoneRegion | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = ZoneRegion(_region)

        _status = d.pop("status", UNSET)
        status: ZoneStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ZoneStatus(_status)

        update_zone_request = cls(
            name=name,
            type_=type_,
            region=region,
            status=status,
        )

        return update_zone_request
