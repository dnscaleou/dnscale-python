from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.record_type import RecordType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        id (str):
        name (str):  Example: www.example.com..
        type_ (RecordType):
        content (str):  Example: 192.0.2.1.
        ttl (int):
        disabled (bool):
        priority (int | None | Unset):
        comment (None | str | Unset):
    """

    id: str
    name: str
    type_: RecordType
    content: str
    ttl: int
    disabled: bool
    priority: int | None | Unset = UNSET
    comment: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_.value

        content = self.content

        ttl = self.ttl

        disabled = self.disabled

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "content": content,
                "ttl": ttl,
                "disabled": disabled,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_ = RecordType(d.pop("type"))

        content = d.pop("content")

        ttl = d.pop("ttl")

        disabled = d.pop("disabled")

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        record = cls(
            id=id,
            name=name,
            type_=type_,
            content=content,
            ttl=ttl,
            disabled=disabled,
            priority=priority,
            comment=comment,
        )

        return record
