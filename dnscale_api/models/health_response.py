from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.health_response_status import HealthResponseStatus

if TYPE_CHECKING:
    from ..models.health_data import HealthData


T = TypeVar("T", bound="HealthResponse")


@_attrs_define
class HealthResponse:
    """
    Attributes:
        status (HealthResponseStatus):
        data (HealthData):
    """

    status: HealthResponseStatus
    data: HealthData

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
        from ..models.health_data import HealthData

        d = dict(src_dict)
        status = HealthResponseStatus(d.pop("status"))

        data = HealthData.from_dict(d.pop("data"))

        health_response = cls(
            status=status,
            data=data,
        )

        return health_response
