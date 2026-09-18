from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.invitations_response_status import InvitationsResponseStatus

if TYPE_CHECKING:
    from ..models.invitations_data import InvitationsData


T = TypeVar("T", bound="InvitationsResponse")


@_attrs_define
class InvitationsResponse:
    """
    Attributes:
        status (InvitationsResponseStatus):
        data (InvitationsData):
    """

    status: InvitationsResponseStatus
    data: InvitationsData

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
        from ..models.invitations_data import InvitationsData

        d = dict(src_dict)
        status = InvitationsResponseStatus(d.pop("status"))

        data = InvitationsData.from_dict(d.pop("data"))

        invitations_response = cls(
            status=status,
            data=data,
        )

        return invitations_response
