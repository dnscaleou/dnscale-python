from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.zone_response_status import ZoneResponseStatus

if TYPE_CHECKING:
    from ..models.zone_data import ZoneData


T = TypeVar("T", bound="ZoneResponse")


@_attrs_define
class ZoneResponse:
    """
    Attributes:
        status (ZoneResponseStatus):
        data (ZoneData):
    """

    status: ZoneResponseStatus
    data: ZoneData

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
        from ..models.zone_data import ZoneData

        d = dict(src_dict)
        status = ZoneResponseStatus(d.pop("status"))

        data = ZoneData.from_dict(d.pop("data"))

        zone_response = cls(
            status=status,
            data=data,
        )

        return zone_response
