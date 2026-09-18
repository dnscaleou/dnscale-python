from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.user_response_status import UserResponseStatus

if TYPE_CHECKING:
    from ..models.user_data import UserData


T = TypeVar("T", bound="UserResponse")


@_attrs_define
class UserResponse:
    """
    Attributes:
        status (UserResponseStatus):
        data (UserData):
    """

    status: UserResponseStatus
    data: UserData

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_data import UserData

        d = dict(src_dict)
        status = UserResponseStatus(d.pop("status"))

        data = UserData.from_dict(d.pop("data"))

        user_response = cls(
            status=status,
            data=data,
        )

        return user_response
