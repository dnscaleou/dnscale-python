from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.aggregated_usage_response_envelope_status import AggregatedUsageResponseEnvelopeStatus

if TYPE_CHECKING:
    from ..models.aggregated_usage_response import AggregatedUsageResponse


T = TypeVar("T", bound="AggregatedUsageResponseEnvelope")


@_attrs_define
class AggregatedUsageResponseEnvelope:
    """
    Attributes:
        status (AggregatedUsageResponseEnvelopeStatus):
        data (AggregatedUsageResponse):
    """

    status: AggregatedUsageResponseEnvelopeStatus
    data: AggregatedUsageResponse

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
        from ..models.aggregated_usage_response import AggregatedUsageResponse

        d = dict(src_dict)
        status = AggregatedUsageResponseEnvelopeStatus(d.pop("status"))

        data = AggregatedUsageResponse.from_dict(d.pop("data"))

        aggregated_usage_response_envelope = cls(
            status=status,
            data=data,
        )

        return aggregated_usage_response_envelope
