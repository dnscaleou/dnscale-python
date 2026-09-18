from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.invitation_status import InvitationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Invitation")


@_attrs_define
class Invitation:
    """
    Attributes:
        id (UUID):
        customer_id (UUID):
        email (str):
        invited_by (str): UUID of the inviting user, or an empty string for legacy invitations.
        expires_at (datetime.datetime):
        status (InvitationStatus):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        token (str | Unset): Present only in the create response.
    """

    id: UUID
    customer_id: UUID
    email: str
    invited_by: str
    expires_at: datetime.datetime
    status: InvitationStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    token: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        customer_id = str(self.customer_id)

        email = self.email

        invited_by = self.invited_by

        expires_at = self.expires_at.isoformat()

        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        token = self.token

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "customer_id": customer_id,
                "email": email,
                "invited_by": invited_by,
                "expires_at": expires_at,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        customer_id = UUID(d.pop("customer_id"))

        email = d.pop("email")

        invited_by = d.pop("invited_by")

        expires_at = isoparse(d.pop("expires_at"))

        status = InvitationStatus(d.pop("status"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        token = d.pop("token", UNSET)

        invitation = cls(
            id=id,
            customer_id=customer_id,
            email=email,
            invited_by=invited_by,
            expires_at=expires_at,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            token=token,
        )

        return invitation
