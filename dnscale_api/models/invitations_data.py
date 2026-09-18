from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.invitation import Invitation


T = TypeVar("T", bound="InvitationsData")


@_attrs_define
class InvitationsData:
    """
    Attributes:
        invitations (list[Invitation]):
    """

    invitations: list[Invitation]

    def to_dict(self) -> dict[str, Any]:
        invitations = []
        for invitations_item_data in self.invitations:
            invitations_item = invitations_item_data.to_dict()
            invitations.append(invitations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "invitations": invitations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invitation import Invitation

        d = dict(src_dict)
        invitations = []
        _invitations = d.pop("invitations")
        for invitations_item_data in _invitations:
            invitations_item = Invitation.from_dict(invitations_item_data)

            invitations.append(invitations_item)

        invitations_data = cls(
            invitations=invitations,
        )

        return invitations_data
