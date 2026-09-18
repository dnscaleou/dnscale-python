from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.alert_response_status import AlertResponseStatus

if TYPE_CHECKING:
    from ..models.alert_data import AlertData


T = TypeVar("T", bound="AlertResponse")


@_attrs_define
class AlertResponse:
    """
    Attributes:
        status (AlertResponseStatus):
        data (AlertData):
    """

    status: AlertResponseStatus
    data: AlertData

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
        from ..models.alert_data import AlertData

        d = dict(src_dict)
        status = AlertResponseStatus(d.pop("status"))

        data = AlertData.from_dict(d.pop("data"))

        alert_response = cls(
            status=status,
            data=data,
        )

        return alert_response
