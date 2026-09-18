from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.billing_summary import BillingSummary


T = TypeVar("T", bound="BillingHistory")


@_attrs_define
class BillingHistory:
    """
    Attributes:
        records (list[BillingSummary]):
        total (int):
    """

    records: list[BillingSummary]
    total: int

    def to_dict(self) -> dict[str, Any]:
        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        total = self.total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "records": records,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_summary import BillingSummary

        d = dict(src_dict)
        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = BillingSummary.from_dict(records_item_data)

            records.append(records_item)

        total = d.pop("total")

        billing_history = cls(
            records=records,
            total=total,
        )

        return billing_history
