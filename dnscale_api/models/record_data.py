from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.record import Record


T = TypeVar("T", bound="RecordData")


@_attrs_define
class RecordData:
    """
    Attributes:
        record (Record):
    """

    record: Record

    def to_dict(self) -> dict[str, Any]:
        record = self.record.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "record": record,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record import Record

        d = dict(src_dict)
        record = Record.from_dict(d.pop("record"))

        record_data = cls(
            record=record,
        )

        return record_data
