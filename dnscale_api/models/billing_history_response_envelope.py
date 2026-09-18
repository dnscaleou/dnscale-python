from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.billing_history_response_envelope_status import BillingHistoryResponseEnvelopeStatus

if TYPE_CHECKING:
    from ..models.billing_history import BillingHistory


T = TypeVar("T", bound="BillingHistoryResponseEnvelope")


@_attrs_define
class BillingHistoryResponseEnvelope:
    """
    Attributes:
        status (BillingHistoryResponseEnvelopeStatus):
        data (BillingHistory):
    """

    status: BillingHistoryResponseEnvelopeStatus
    data: BillingHistory

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
        from ..models.billing_history import BillingHistory

        d = dict(src_dict)
        status = BillingHistoryResponseEnvelopeStatus(d.pop("status"))

        data = BillingHistory.from_dict(d.pop("data"))

        billing_history_response_envelope = cls(
            status=status,
            data=data,
        )

        return billing_history_response_envelope
