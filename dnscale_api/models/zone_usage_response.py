from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.zone_usage_response_status import ZoneUsageResponseStatus

if TYPE_CHECKING:
    from ..models.zone_usage_summary import ZoneUsageSummary


T = TypeVar("T", bound="ZoneUsageResponse")


@_attrs_define
class ZoneUsageResponse:
    """
    Attributes:
        status (ZoneUsageResponseStatus):
        data (ZoneUsageSummary):
    """

    status: ZoneUsageResponseStatus
    data: ZoneUsageSummary

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
        from ..models.zone_usage_summary import ZoneUsageSummary

        d = dict(src_dict)
        status = ZoneUsageResponseStatus(d.pop("status"))

        data = ZoneUsageSummary.from_dict(d.pop("data"))

        zone_usage_response = cls(
            status=status,
            data=data,
        )

        return zone_usage_response
