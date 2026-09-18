from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.customer_usage_summary_billing_type import CustomerUsageSummaryBillingType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.zone_usage_summary import ZoneUsageSummary


T = TypeVar("T", bound="CustomerUsageSummary")


@_attrs_define
class CustomerUsageSummary:
    """
    Attributes:
        customer_id (UUID):
        billing_month (datetime.datetime):
        billing_type (CustomerUsageSummaryBillingType):
        total_queries (int):
        included_queries (int):
        overage_queries (int):
        overage_amount (float):
        usage_percentage (float):
        days_active (int):
        days_in_month (int):
        is_pro_rated (bool):
        zone_breakdown (list[ZoneUsageSummary] | Unset):
        active_zones (int | Unset):
        zone_charges (float | Unset):
        query_charges (float | Unset):
        estimated_total (float | Unset):
    """

    customer_id: UUID
    billing_month: datetime.datetime
    billing_type: CustomerUsageSummaryBillingType
    total_queries: int
    included_queries: int
    overage_queries: int
    overage_amount: float
    usage_percentage: float
    days_active: int
    days_in_month: int
    is_pro_rated: bool
    zone_breakdown: list[ZoneUsageSummary] | Unset = UNSET
    active_zones: int | Unset = UNSET
    zone_charges: float | Unset = UNSET
    query_charges: float | Unset = UNSET
    estimated_total: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        customer_id = str(self.customer_id)

        billing_month = self.billing_month.isoformat()

        billing_type = self.billing_type.value

        total_queries = self.total_queries

        included_queries = self.included_queries

        overage_queries = self.overage_queries

        overage_amount = self.overage_amount

        usage_percentage = self.usage_percentage

        days_active = self.days_active

        days_in_month = self.days_in_month

        is_pro_rated = self.is_pro_rated

        zone_breakdown: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.zone_breakdown, Unset):
            zone_breakdown = []
            for zone_breakdown_item_data in self.zone_breakdown:
                zone_breakdown_item = zone_breakdown_item_data.to_dict()
                zone_breakdown.append(zone_breakdown_item)

        active_zones = self.active_zones

        zone_charges = self.zone_charges

        query_charges = self.query_charges

        estimated_total = self.estimated_total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "customer_id": customer_id,
                "billing_month": billing_month,
                "billing_type": billing_type,
                "total_queries": total_queries,
                "included_queries": included_queries,
                "overage_queries": overage_queries,
                "overage_amount": overage_amount,
                "usage_percentage": usage_percentage,
                "days_active": days_active,
                "days_in_month": days_in_month,
                "is_pro_rated": is_pro_rated,
            }
        )
        if zone_breakdown is not UNSET:
            field_dict["zone_breakdown"] = zone_breakdown
        if active_zones is not UNSET:
            field_dict["active_zones"] = active_zones
        if zone_charges is not UNSET:
            field_dict["zone_charges"] = zone_charges
        if query_charges is not UNSET:
            field_dict["query_charges"] = query_charges
        if estimated_total is not UNSET:
            field_dict["estimated_total"] = estimated_total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.zone_usage_summary import ZoneUsageSummary

        d = dict(src_dict)
        customer_id = UUID(d.pop("customer_id"))

        billing_month = isoparse(d.pop("billing_month"))

        billing_type = CustomerUsageSummaryBillingType(d.pop("billing_type"))

        total_queries = d.pop("total_queries")

        included_queries = d.pop("included_queries")

        overage_queries = d.pop("overage_queries")

        overage_amount = d.pop("overage_amount")

        usage_percentage = d.pop("usage_percentage")

        days_active = d.pop("days_active")

        days_in_month = d.pop("days_in_month")

        is_pro_rated = d.pop("is_pro_rated")

        _zone_breakdown = d.pop("zone_breakdown", UNSET)
        zone_breakdown: list[ZoneUsageSummary] | Unset = UNSET
        if _zone_breakdown is not UNSET:
            zone_breakdown = []
            for zone_breakdown_item_data in _zone_breakdown:
                zone_breakdown_item = ZoneUsageSummary.from_dict(zone_breakdown_item_data)

                zone_breakdown.append(zone_breakdown_item)

        active_zones = d.pop("active_zones", UNSET)

        zone_charges = d.pop("zone_charges", UNSET)

        query_charges = d.pop("query_charges", UNSET)

        estimated_total = d.pop("estimated_total", UNSET)

        customer_usage_summary = cls(
            customer_id=customer_id,
            billing_month=billing_month,
            billing_type=billing_type,
            total_queries=total_queries,
            included_queries=included_queries,
            overage_queries=overage_queries,
            overage_amount=overage_amount,
            usage_percentage=usage_percentage,
            days_active=days_active,
            days_in_month=days_in_month,
            is_pro_rated=is_pro_rated,
            zone_breakdown=zone_breakdown,
            active_zones=active_zones,
            zone_charges=zone_charges,
            query_charges=query_charges,
            estimated_total=estimated_total,
        )

        return customer_usage_summary
