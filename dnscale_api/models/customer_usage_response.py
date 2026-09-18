from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.customer_usage_response_status import CustomerUsageResponseStatus

if TYPE_CHECKING:
    from ..models.customer_usage_summary import CustomerUsageSummary


T = TypeVar("T", bound="CustomerUsageResponse")


@_attrs_define
class CustomerUsageResponse:
    """
    Attributes:
        status (CustomerUsageResponseStatus):
        data (CustomerUsageSummary):
    """

    status: CustomerUsageResponseStatus
    data: CustomerUsageSummary

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.customer_usage_summary import CustomerUsageSummary

        d = dict(src_dict)
        status = CustomerUsageResponseStatus(d.pop("status"))

        data = CustomerUsageSummary.from_dict(d.pop("data"))

        customer_usage_response = cls(
            status=status,
            data=data,
        )

        return customer_usage_response
