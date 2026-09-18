from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.top_zones_response_status import TopZonesResponseStatus

if TYPE_CHECKING:
    from ..models.top_zones_data import TopZonesData


T = TypeVar("T", bound="TopZonesResponse")


@_attrs_define
class TopZonesResponse:
    """
    Attributes:
        status (TopZonesResponseStatus):
        data (TopZonesData):
    """

    status: TopZonesResponseStatus
    data: TopZonesData

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
        from ..models.top_zones_data import TopZonesData

        d = dict(src_dict)
        status = TopZonesResponseStatus(d.pop("status"))

        data = TopZonesData.from_dict(d.pop("data"))

        top_zones_response = cls(
            status=status,
            data=data,
        )

        return top_zones_response
