from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.record_response_status import RecordResponseStatus

if TYPE_CHECKING:
    from ..models.record_data import RecordData


T = TypeVar("T", bound="RecordResponse")


@_attrs_define
class RecordResponse:
    """
    Attributes:
        status (RecordResponseStatus):
        data (RecordData):
    """

    status: RecordResponseStatus
    data: RecordData

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
        from ..models.record_data import RecordData

        d = dict(src_dict)
        status = RecordResponseStatus(d.pop("status"))

        data = RecordData.from_dict(d.pop("data"))

        record_response = cls(
            status=status,
            data=data,
        )

        return record_response
