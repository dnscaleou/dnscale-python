from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.ds_records_response_status import DSRecordsResponseStatus

if TYPE_CHECKING:
    from ..models.ds_records_data import DSRecordsData


T = TypeVar("T", bound="DSRecordsResponse")


@_attrs_define
class DSRecordsResponse:
    """
    Attributes:
        status (DSRecordsResponseStatus):
        data (DSRecordsData):
    """

    status: DSRecordsResponseStatus
    data: DSRecordsData

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
        from ..models.ds_records_data import DSRecordsData

        d = dict(src_dict)
        status = DSRecordsResponseStatus(d.pop("status"))

        data = DSRecordsData.from_dict(d.pop("data"))

        ds_records_response = cls(
            status=status,
            data=data,
        )

        return ds_records_response
