from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.record_type import RecordType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRecordRequest")


@_attrs_define
class CreateRecordRequest:
    """
    Attributes:
        name (str): Relative owner name, `@` for the apex, or a fully qualified name.
        type_ (RecordType):
        content (str):
        ttl (int | Unset):  Default: 3600.
        priority (int | None | Unset):
        disabled (bool | Unset):  Default: False.
        comment (None | str | Unset):
    """

    name: str
    type_: RecordType
    content: str
    ttl: int | Unset = 3600
    priority: int | None | Unset = UNSET
    disabled: bool | Unset = False
    comment: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        content = self.content

        ttl = self.ttl

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        disabled = self.disabled

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
                "content": content,
            }
        )
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if priority is not UNSET:
            field_dict["priority"] = priority
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = RecordType(d.pop("type"))

        content = d.pop("content")

        ttl = d.pop("ttl", UNSET)

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        disabled = d.pop("disabled", UNSET)

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        create_record_request = cls(
            name=name,
            type_=type_,
            content=content,
            ttl=ttl,
            priority=priority,
            disabled=disabled,
            comment=comment,
        )

        return create_record_request
