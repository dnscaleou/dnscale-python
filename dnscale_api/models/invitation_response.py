from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.invitation_response_status import InvitationResponseStatus

if TYPE_CHECKING:
    from ..models.invitation_data import InvitationData


T = TypeVar("T", bound="InvitationResponse")


@_attrs_define
class InvitationResponse:
    """
    Attributes:
        status (InvitationResponseStatus):
        data (InvitationData):
    """

    status: InvitationResponseStatus
    data: InvitationData

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
        from ..models.invitation_data import InvitationData

        d = dict(src_dict)
        status = InvitationResponseStatus(d.pop("status"))

        data = InvitationData.from_dict(d.pop("data"))

        invitation_response = cls(
            status=status,
            data=data,
        )

        return invitation_response
