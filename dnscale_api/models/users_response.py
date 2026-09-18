from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.users_response_status import UsersResponseStatus

if TYPE_CHECKING:
    from ..models.users_data import UsersData


T = TypeVar("T", bound="UsersResponse")


@_attrs_define
class UsersResponse:
    """
    Attributes:
        status (UsersResponseStatus):
        data (UsersData):
    """

    status: UsersResponseStatus
    data: UsersData

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
        from ..models.users_data import UsersData

        d = dict(src_dict)
        status = UsersResponseStatus(d.pop("status"))

        data = UsersData.from_dict(d.pop("data"))

        users_response = cls(
            status=status,
            data=data,
        )

        return users_response
