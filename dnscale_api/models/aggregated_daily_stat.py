from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_map import UsageMap


T = TypeVar("T", bound="AggregatedDailyStat")


@_attrs_define
class AggregatedDailyStat:
    """
    Attributes:
        date (datetime.datetime):
        total_queries (int):
        query_by_type (UsageMap | Unset):
        query_by_rcode (UsageMap | Unset):
    """

    date: datetime.datetime
    total_queries: int
    query_by_type: UsageMap | Unset = UNSET
    query_by_rcode: UsageMap | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        total_queries = self.total_queries

        query_by_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_by_type, Unset):
            query_by_type = self.query_by_type.to_dict()

        query_by_rcode: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_by_rcode, Unset):
            query_by_rcode = self.query_by_rcode.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "date": date,
                "total_queries": total_queries,
            }
        )
        if query_by_type is not UNSET:
            field_dict["query_by_type"] = query_by_type
        if query_by_rcode is not UNSET:
            field_dict["query_by_rcode"] = query_by_rcode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_map import UsageMap

        d = dict(src_dict)
        date = isoparse(d.pop("date"))

        total_queries = d.pop("total_queries")

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

        aggregated_daily_stat = cls(
            date=date,
            total_queries=total_queries,
            query_by_type=query_by_type,
            query_by_rcode=query_by_rcode,
        )

        return aggregated_daily_stat
