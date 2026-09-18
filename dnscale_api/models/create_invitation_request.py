from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateInvitationRequest")


@_attrs_define
class CreateInvitationRequest:
    """
    Attributes:
        email (str):
    """

    email: str

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        create_invitation_request = cls(
            email=email,
        )

        return create_invitation_request
