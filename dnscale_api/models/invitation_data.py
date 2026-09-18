from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.invitation import Invitation


T = TypeVar("T", bound="InvitationData")


@_attrs_define
class InvitationData:
    """
    Attributes:
        invitation (Invitation):
    """

    invitation: Invitation

    def to_dict(self) -> dict[str, Any]:
        invitation = self.invitation.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "invitation": invitation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invitation import Invitation

        d = dict(src_dict)
        invitation = Invitation.from_dict(d.pop("invitation"))

        invitation_data = cls(
            invitation=invitation,
        )

        return invitation_data
