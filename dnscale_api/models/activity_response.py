from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.activity_response_status import ActivityResponseStatus

if TYPE_CHECKING:
    from ..models.activity_data import ActivityData


T = TypeVar("T", bound="ActivityResponse")


@_attrs_define
class ActivityResponse:
    """
    Attributes:
        status (ActivityResponseStatus):
        data (ActivityData):
    """

    status: ActivityResponseStatus
    data: ActivityData

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
        from ..models.activity_data import ActivityData

        d = dict(src_dict)
        status = ActivityResponseStatus(d.pop("status"))

        data = ActivityData.from_dict(d.pop("data"))

        activity_response = cls(
            status=status,
            data=data,
        )

        return activity_response
