from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateRecordByNameRequest")


@_attrs_define
class UpdateRecordByNameRequest:
    """
    Attributes:
        content (str):
        ttl (int | Unset):  Default: 3600.
        priority (int | None | Unset):
        disabled (bool | Unset):
        comment (None | str | Unset):
    """

    content: str
    ttl: int | Unset = 3600
    priority: int | None | Unset = UNSET
    disabled: bool | Unset = UNSET
    comment: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        update_record_by_name_request = cls(
            content=content,
            ttl=ttl,
            priority=priority,
            disabled=disabled,
            comment=comment,
        )

        return update_record_by_name_request
