from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.record import Record


T = TypeVar("T", bound="RecordsData")


@_attrs_define
class RecordsData:
    """
    Attributes:
        records (list[Record]):
        pagination (Pagination):
    """

    records: list[Record]
    pagination: Pagination

    def to_dict(self) -> dict[str, Any]:
        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "records": records,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.record import Record

        d = dict(src_dict)
        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = Record.from_dict(records_item_data)

            records.append(records_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        records_data = cls(
            records=records,
            pagination=pagination,
        )

        return records_data
