from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.api_key_zone_scope_record_access import APIKeyZoneScopeRecordAccess

T = TypeVar("T", bound="APIKeyZoneScope")


@_attrs_define
class APIKeyZoneScope:
    """
    Attributes:
        zone_id (UUID):
        record_access (APIKeyZoneScopeRecordAccess): Whole-zone or exact-name access.
        record_names (list[str]): Canonical relative owners. Use `@` for the apex. Names may
            also be supplied as in-zone absolute names when creating a key and
            are returned in canonical relative form. A literal `*` matches only
            the wildcard owner; it is not a glob. Required and non-empty when
            `record_access` is `names`; empty when it is `all`.
             Example: ['_acme-challenge', '_acme-challenge.api'].
    """

    zone_id: UUID
    record_access: APIKeyZoneScopeRecordAccess
    record_names: list[str]

    def to_dict(self) -> dict[str, Any]:
        zone_id = str(self.zone_id)

        record_access = self.record_access.value

        record_names = self.record_names

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "zone_id": zone_id,
                "record_access": record_access,
                "record_names": record_names,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        zone_id = UUID(d.pop("zone_id"))

        record_access = APIKeyZoneScopeRecordAccess(d.pop("record_access"))

        record_names = cast(list[str], d.pop("record_names"))

        api_key_zone_scope = cls(
            zone_id=zone_id,
            record_access=record_access,
            record_names=record_names,
        )

        return api_key_zone_scope
