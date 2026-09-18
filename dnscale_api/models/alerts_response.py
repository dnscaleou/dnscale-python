from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.alerts_response_status import AlertsResponseStatus

if TYPE_CHECKING:
    from ..models.alerts_data import AlertsData


T = TypeVar("T", bound="AlertsResponse")


@_attrs_define
class AlertsResponse:
    """
    Attributes:
        status (AlertsResponseStatus):
        data (AlertsData):
    """

    status: AlertsResponseStatus
    data: AlertsData

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
        from ..models.alerts_data import AlertsData

        d = dict(src_dict)
        status = AlertsResponseStatus(d.pop("status"))

        data = AlertsData.from_dict(d.pop("data"))

        alerts_response = cls(
            status=status,
            data=data,
        )

        return alerts_response
