from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.aggregated_daily_stat import AggregatedDailyStat
    from ..models.usage_map import UsageMap


T = TypeVar("T", bound="AggregatedUsageResponse")


@_attrs_define
class AggregatedUsageResponse:
    """
    Attributes:
        period_start (datetime.datetime):
        period_end (datetime.datetime):
        total_queries (int):
        daily_stats (list[AggregatedDailyStat]):
        query_type_breakdown (UsageMap):
        rcode_breakdown (UsageMap):
    """

    period_start: datetime.datetime
    period_end: datetime.datetime
    total_queries: int
    daily_stats: list[AggregatedDailyStat]
    query_type_breakdown: UsageMap
    rcode_breakdown: UsageMap

    def to_dict(self) -> dict[str, Any]:
        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        total_queries = self.total_queries

        daily_stats = []
        for daily_stats_item_data in self.daily_stats:
            daily_stats_item = daily_stats_item_data.to_dict()
            daily_stats.append(daily_stats_item)

        query_type_breakdown = self.query_type_breakdown.to_dict()

        rcode_breakdown = self.rcode_breakdown.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "period_start": period_start,
                "period_end": period_end,
                "total_queries": total_queries,
                "daily_stats": daily_stats,
                "query_type_breakdown": query_type_breakdown,
                "rcode_breakdown": rcode_breakdown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aggregated_daily_stat import AggregatedDailyStat
        from ..models.usage_map import UsageMap

        d = dict(src_dict)
        period_start = isoparse(d.pop("period_start"))

        period_end = isoparse(d.pop("period_end"))

        total_queries = d.pop("total_queries")

        daily_stats = []
        _daily_stats = d.pop("daily_stats")
        for daily_stats_item_data in _daily_stats:
            daily_stats_item = AggregatedDailyStat.from_dict(daily_stats_item_data)

            daily_stats.append(daily_stats_item)

        query_type_breakdown = UsageMap.from_dict(d.pop("query_type_breakdown"))

        rcode_breakdown = UsageMap.from_dict(d.pop("rcode_breakdown"))

        aggregated_usage_response = cls(
            period_start=period_start,
            period_end=period_end,
            total_queries=total_queries,
            daily_stats=daily_stats,
            query_type_breakdown=query_type_breakdown,
            rcode_breakdown=rcode_breakdown,
        )

        return aggregated_usage_response
