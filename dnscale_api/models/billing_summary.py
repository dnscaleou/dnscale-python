from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingSummary")


@_attrs_define
class BillingSummary:
    """
    Attributes:
        customer_id (UUID):
        billing_month (str):
        total_queries (int):
        included_queries (int):
        overage_queries (int):
        overage_rate (float):
        overage_amount (float):
        usage_percentage (float):
        is_pro_rated (bool):
        days_active (int | Unset):
        days_in_month (int | Unset):
    """

    customer_id: UUID
    billing_month: str
    total_queries: int
    included_queries: int
    overage_queries: int
    overage_rate: float
    overage_amount: float
    usage_percentage: float
    is_pro_rated: bool
    days_active: int | Unset = UNSET
    days_in_month: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        customer_id = str(self.customer_id)

        billing_month = self.billing_month

        total_queries = self.total_queries

        included_queries = self.included_queries

        overage_queries = self.overage_queries

        overage_rate = self.overage_rate

        overage_amount = self.overage_amount

        usage_percentage = self.usage_percentage

        is_pro_rated = self.is_pro_rated

        days_active = self.days_active

        days_in_month = self.days_in_month

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "customer_id": customer_id,
                "billing_month": billing_month,
                "total_queries": total_queries,
                "included_queries": included_queries,
                "overage_queries": overage_queries,
                "overage_rate": overage_rate,
                "overage_amount": overage_amount,
                "usage_percentage": usage_percentage,
                "is_pro_rated": is_pro_rated,
            }
        )
        if days_active is not UNSET:
            field_dict["days_active"] = days_active
        if days_in_month is not UNSET:
            field_dict["days_in_month"] = days_in_month

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        customer_id = UUID(d.pop("customer_id"))

        billing_month = d.pop("billing_month")

        total_queries = d.pop("total_queries")

        included_queries = d.pop("included_queries")

        overage_queries = d.pop("overage_queries")

        overage_rate = d.pop("overage_rate")

        overage_amount = d.pop("overage_amount")

        usage_percentage = d.pop("usage_percentage")

        is_pro_rated = d.pop("is_pro_rated")

        days_active = d.pop("days_active", UNSET)

        days_in_month = d.pop("days_in_month", UNSET)

        billing_summary = cls(
            customer_id=customer_id,
            billing_month=billing_month,
            total_queries=total_queries,
            included_queries=included_queries,
            overage_queries=overage_queries,
            overage_rate=overage_rate,
            overage_amount=overage_amount,
            usage_percentage=usage_percentage,
            is_pro_rated=is_pro_rated,
            days_active=days_active,
            days_in_month=days_in_month,
        )

        return billing_summary
