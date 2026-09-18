from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.user_role import UserRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        id (UUID):
        customer_id (UUID):
        email (str):
        full_name (str):
        role (UserRole):
        active (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        zone_count (int | None | Unset):
    """

    id: UUID
    customer_id: UUID
    email: str
    full_name: str
    role: UserRole
    active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    zone_count: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        customer_id = str(self.customer_id)

        email = self.email

        full_name = self.full_name

        role = self.role.value

        active = self.active

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        zone_count: int | None | Unset
        if isinstance(self.zone_count, Unset):
            zone_count = UNSET
        else:
            zone_count = self.zone_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "customer_id": customer_id,
                "email": email,
                "full_name": full_name,
                "role": role,
                "active": active,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if zone_count is not UNSET:
            field_dict["zone_count"] = zone_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        customer_id = UUID(d.pop("customer_id"))

        email = d.pop("email")

        full_name = d.pop("full_name")

        role = UserRole(d.pop("role"))

        active = d.pop("active")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_zone_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        zone_count = _parse_zone_count(d.pop("zone_count", UNSET))

        user = cls(
            id=id,
            customer_id=customer_id,
            email=email,
            full_name=full_name,
            role=role,
            active=active,
            created_at=created_at,
            updated_at=updated_at,
            zone_count=zone_count,
        )

        return user
