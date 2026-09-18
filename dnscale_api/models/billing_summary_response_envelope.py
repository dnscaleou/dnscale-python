from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.billing_summary_response_envelope_status import BillingSummaryResponseEnvelopeStatus

if TYPE_CHECKING:
    from ..models.billing_summary import BillingSummary


T = TypeVar("T", bound="BillingSummaryResponseEnvelope")


@_attrs_define
class BillingSummaryResponseEnvelope:
    """
    Attributes:
        status (BillingSummaryResponseEnvelopeStatus):
        data (BillingSummary):
    """

    status: BillingSummaryResponseEnvelopeStatus
    data: BillingSummary

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
        from ..models.billing_summary import BillingSummary

        d = dict(src_dict)
        status = BillingSummaryResponseEnvelopeStatus(d.pop("status"))

        data = BillingSummary.from_dict(d.pop("data"))

        billing_summary_response_envelope = cls(
            status=status,
            data=data,
        )

        return billing_summary_response_envelope
