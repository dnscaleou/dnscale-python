from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.user_role import UserRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserRequest")


@_attrs_define
class UpdateUserRequest:
    """The current API requires `email`; omitted role and active values retain their existing values.

    Attributes:
        email (str):
        full_name (str | Unset):
        role (UserRole | Unset):
        active (bool | Unset):
    """

    email: str
    full_name: str | Unset = UNSET
    role: UserRole | Unset = UNSET
    active: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        full_name = self.full_name

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        active = self.active

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
            }
        )
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if role is not UNSET:
            field_dict["role"] = role
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        full_name = d.pop("full_name", UNSET)

        _role = d.pop("role", UNSET)
        role: UserRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = UserRole(_role)

        active = d.pop("active", UNSET)

        update_user_request = cls(
            email=email,
            full_name=full_name,
            role=role,
            active=active,
        )

        return update_user_request
