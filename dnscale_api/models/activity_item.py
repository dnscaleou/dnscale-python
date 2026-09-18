from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_item_new_values_type_0 import ActivityItemNewValuesType0
    from ..models.activity_item_old_values_type_0 import ActivityItemOldValuesType0


T = TypeVar("T", bound="ActivityItem")


@_attrs_define
class ActivityItem:
    """
    Attributes:
        id (UUID):
        action (str):
        resource (str):
        resource_id (str):
        ip_address (str):
        user_agent (str):
        created_at (datetime.datetime):
        old_values (ActivityItemOldValuesType0 | None | Unset):
        new_values (ActivityItemNewValuesType0 | None | Unset):
        user_id (None | Unset | UUID):
        user_email (None | str | Unset):
        user_name (None | str | Unset):
    """

    id: UUID
    action: str
    resource: str
    resource_id: str
    ip_address: str
    user_agent: str
    created_at: datetime.datetime
    old_values: ActivityItemOldValuesType0 | None | Unset = UNSET
    new_values: ActivityItemNewValuesType0 | None | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    user_email: None | str | Unset = UNSET
    user_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_item_new_values_type_0 import ActivityItemNewValuesType0
        from ..models.activity_item_old_values_type_0 import ActivityItemOldValuesType0

        id = str(self.id)

        action = self.action

        resource = self.resource

        resource_id = self.resource_id

        ip_address = self.ip_address

        user_agent = self.user_agent

        created_at = self.created_at.isoformat()

        old_values: dict[str, Any] | None | Unset
        if isinstance(self.old_values, Unset):
            old_values = UNSET
        elif isinstance(self.old_values, ActivityItemOldValuesType0):
            old_values = self.old_values.to_dict()
        else:
            old_values = self.old_values

        new_values: dict[str, Any] | None | Unset
        if isinstance(self.new_values, Unset):
            new_values = UNSET
        elif isinstance(self.new_values, ActivityItemNewValuesType0):
            new_values = self.new_values.to_dict()
        else:
            new_values = self.new_values

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "action": action,
                "resource": resource,
                "resource_id": resource_id,
                "ip_address": ip_address,
                "user_agent": user_agent,
                "created_at": created_at,
            }
        )
        if old_values is not UNSET:
            field_dict["old_values"] = old_values
        if new_values is not UNSET:
            field_dict["new_values"] = new_values
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if user_name is not UNSET:
            field_dict["user_name"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_item_new_values_type_0 import ActivityItemNewValuesType0
        from ..models.activity_item_old_values_type_0 import ActivityItemOldValuesType0

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        action = d.pop("action")

        resource = d.pop("resource")

        resource_id = d.pop("resource_id")

        ip_address = d.pop("ip_address")

        user_agent = d.pop("user_agent")

        created_at = isoparse(d.pop("created_at"))

        def _parse_old_values(data: object) -> ActivityItemOldValuesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                old_values_type_0 = ActivityItemOldValuesType0.from_dict(data)

                return old_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActivityItemOldValuesType0 | None | Unset, data)

        old_values = _parse_old_values(d.pop("old_values", UNSET))

        def _parse_new_values(data: object) -> ActivityItemNewValuesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                new_values_type_0 = ActivityItemNewValuesType0.from_dict(data)

                return new_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActivityItemNewValuesType0 | None | Unset, data)

        new_values = _parse_new_values(d.pop("new_values", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("user_name", UNSET))

        activity_item = cls(
            id=id,
            action=action,
            resource=resource,
            resource_id=resource_id,
            ip_address=ip_address,
            user_agent=user_agent,
            created_at=created_at,
            old_values=old_values,
            new_values=new_values,
            user_id=user_id,
            user_email=user_email,
            user_name=user_name,
        )

        return activity_item
