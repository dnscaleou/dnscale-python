from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="DSRecordsData")


@_attrs_define
class DSRecordsData:
    """
    Attributes:
        ds_records (list[str]):
    """

    ds_records: list[str]

    def to_dict(self) -> dict[str, Any]:
        ds_records = self.ds_records

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ds_records": ds_records,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ds_records = cast(list[str], d.pop("ds_records"))

        ds_records_data = cls(
            ds_records=ds_records,
        )

        return ds_records_data
