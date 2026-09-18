from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.zone_usage_daily import ZoneUsageDaily


T = TypeVar("T", bound="ZoneUsageSummary")


@_attrs_define
class ZoneUsageSummary:
    """
    Attributes:
        zone_name (str):
        total_queries (int):
        period_start (datetime.datetime):
        period_end (datetime.datetime):
        zone_id (None | Unset | UUID):
        daily_breakdown (list[ZoneUsageDaily] | Unset):
    """

    zone_name: str
    total_queries: int
    period_start: datetime.datetime
    period_end: datetime.datetime
    zone_id: None | Unset | UUID = UNSET
    daily_breakdown: list[ZoneUsageDaily] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        zone_name = self.zone_name

        total_queries = self.total_queries

        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        zone_id: None | str | Unset
        if isinstance(self.zone_id, Unset):
            zone_id = UNSET
        elif isinstance(self.zone_id, UUID):
            zone_id = str(self.zone_id)
        else:
            zone_id = self.zone_id

        daily_breakdown: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.daily_breakdown, Unset):
            daily_breakdown = []
            for daily_breakdown_item_data in self.daily_breakdown:
                daily_breakdown_item = daily_breakdown_item_data.to_dict()
                daily_breakdown.append(daily_breakdown_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "zone_name": zone_name,
                "total_queries": total_queries,
                "period_start": period_start,
                "period_end": period_end,
            }
        )
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id
        if daily_breakdown is not UNSET:
            field_dict["daily_breakdown"] = daily_breakdown

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.zone_usage_daily import ZoneUsageDaily

        d = dict(src_dict)
        zone_name = d.pop("zone_name")

        total_queries = d.pop("total_queries")

        period_start = isoparse(d.pop("period_start"))

        period_end = isoparse(d.pop("period_end"))

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

        _daily_breakdown = d.pop("daily_breakdown", UNSET)
        daily_breakdown: list[ZoneUsageDaily] | Unset = UNSET
        if _daily_breakdown is not UNSET:
            daily_breakdown = []
            for daily_breakdown_item_data in _daily_breakdown:
                daily_breakdown_item = ZoneUsageDaily.from_dict(daily_breakdown_item_data)

                daily_breakdown.append(daily_breakdown_item)

        zone_usage_summary = cls(
            zone_name=zone_name,
            total_queries=total_queries,
            period_start=period_start,
            period_end=period_end,
            zone_id=zone_id,
            daily_breakdown=daily_breakdown,
        )

        return zone_usage_summary
