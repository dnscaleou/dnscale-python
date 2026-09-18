from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.dns_control_auth_field_type import DNSControlAuthFieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DNSControlAuthField")


@_attrs_define
class DNSControlAuthField:
    """
    Attributes:
        name (str):
        label (str):
        type_ (DNSControlAuthFieldType):
        required (bool):
        placeholder (str | Unset):
        help_text (str | Unset):
    """

    name: str
    label: str
    type_: DNSControlAuthFieldType
    required: bool
    placeholder: str | Unset = UNSET
    help_text: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        label = self.label

        type_ = self.type_.value

        required = self.required

        placeholder = self.placeholder

        help_text = self.help_text

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "label": label,
                "type": type_,
                "required": required,
            }
        )
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
        if help_text is not UNSET:
            field_dict["help_text"] = help_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        label = d.pop("label")

        type_ = DNSControlAuthFieldType(d.pop("type"))

        required = d.pop("required")

        placeholder = d.pop("placeholder", UNSET)

        help_text = d.pop("help_text", UNSET)

        dns_control_auth_field = cls(
            name=name,
            label=label,
            type_=type_,
            required=required,
            placeholder=placeholder,
            help_text=help_text,
        )

        return dns_control_auth_field
