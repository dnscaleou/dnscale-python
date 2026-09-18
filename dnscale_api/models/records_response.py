from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.records_response_status import RecordsResponseStatus

if TYPE_CHECKING:
    from ..models.records_data import RecordsData


T = TypeVar("T", bound="RecordsResponse")


@_attrs_define
class RecordsResponse:
    """
    Attributes:
        status (RecordsResponseStatus):
        data (RecordsData):
    """

    status: RecordsResponseStatus
    data: RecordsData

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
        from ..models.records_data import RecordsData

        d = dict(src_dict)
        status = RecordsResponseStatus(d.pop("status"))

        data = RecordsData.from_dict(d.pop("data"))

        records_response = cls(
            status=status,
            data=data,
        )

        return records_response
