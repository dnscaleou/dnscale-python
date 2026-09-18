from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_map import UsageMap


T = TypeVar("T", bound="ZoneUsageDaily")


@_attrs_define
class ZoneUsageDaily:
    """
    Attributes:
        id (int):
        zone_name (str):
        customer_id (UUID):
        usage_date (datetime.datetime):
        total_queries (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        zone_id (None | Unset | UUID):
        query_by_type (UsageMap | Unset):
        query_by_rcode (UsageMap | Unset):
    """

    id: int
    zone_name: str
    customer_id: UUID
    usage_date: datetime.datetime
    total_queries: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    zone_id: None | Unset | UUID = UNSET
    query_by_type: UsageMap | Unset = UNSET
    query_by_rcode: UsageMap | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        zone_name = self.zone_name

        customer_id = str(self.customer_id)

        usage_date = self.usage_date.isoformat()

        total_queries = self.total_queries

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        zone_id: None | str | Unset
        if isinstance(self.zone_id, Unset):
            zone_id = UNSET
        elif isinstance(self.zone_id, UUID):
            zone_id = str(self.zone_id)
        else:
            zone_id = self.zone_id

        query_by_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_by_type, Unset):
            query_by_type = self.query_by_type.to_dict()

        query_by_rcode: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_by_rcode, Unset):
            query_by_rcode = self.query_by_rcode.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "zone_name": zone_name,
                "customer_id": customer_id,
                "usage_date": usage_date,
                "total_queries": total_queries,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id
        if query_by_type is not UNSET:
            field_dict["query_by_type"] = query_by_type
        if query_by_rcode is not UNSET:
            field_dict["query_by_rcode"] = query_by_rcode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_map import UsageMap

        d = dict(src_dict)
        id = d.pop("id")

        zone_name = d.pop("zone_name")

        customer_id = UUID(d.pop("customer_id"))

        usage_date = isoparse(d.pop("usage_date"))

        total_queries = d.pop("total_queries")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_zone_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                zone_id_type_0 = UUID(data)

                return zone_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        zone_id = _parse_zone_id(d.pop("zone_id", UNSET))

        _query_by_type = d.pop("query_by_type", UNSET)
        query_by_type: UsageMap | Unset
        if isinstance(_query_by_type, Unset):
            query_by_type = UNSET
        else:
            query_by_type = UsageMap.from_dict(_query_by_type)

        _query_by_rcode = d.pop("query_by_rcode", UNSET)
        query_by_rcode: UsageMap | Unset
        if isinstance(_query_by_rcode, Unset):
            query_by_rcode = UNSET
        else:
            query_by_rcode = UsageMap.from_dict(_query_by_rcode)

        zone_usage_daily = cls(
            id=id,
            zone_name=zone_name,
            customer_id=customer_id,
            usage_date=usage_date,
            total_queries=total_queries,
            created_at=created_at,
            updated_at=updated_at,
            zone_id=zone_id,
            query_by_type=query_by_type,
            query_by_rcode=query_by_rcode,
        )

        return zone_usage_daily
