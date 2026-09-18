from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DNSControlProviderCapabilities")


@_attrs_define
class DNSControlProviderCapabilities:
    """
    Attributes:
        can_list_zones (bool):
        can_read_records (bool):
        can_write_records (bool):
        supports_comments (bool):
        supports_tags (bool):
        supports_proxied_records (bool):
        supports_alias_flattening (bool):
        supports_dnssec_status_read (bool):
        exposes_assigned_nameservers (bool):
        exposes_registrar_constraints (bool):
        live_secondary_without_delegation_change (bool):
        known_import_export_exclusions (list[str] | Unset):
    """

    can_list_zones: bool
    can_read_records: bool
    can_write_records: bool
    supports_comments: bool
    supports_tags: bool
    supports_proxied_records: bool
    supports_alias_flattening: bool
    supports_dnssec_status_read: bool
    exposes_assigned_nameservers: bool
    exposes_registrar_constraints: bool
    live_secondary_without_delegation_change: bool
    known_import_export_exclusions: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        can_list_zones = self.can_list_zones

        can_read_records = self.can_read_records

        can_write_records = self.can_write_records

        supports_comments = self.supports_comments

        supports_tags = self.supports_tags

        supports_proxied_records = self.supports_proxied_records

        supports_alias_flattening = self.supports_alias_flattening

        supports_dnssec_status_read = self.supports_dnssec_status_read

        exposes_assigned_nameservers = self.exposes_assigned_nameservers

        exposes_registrar_constraints = self.exposes_registrar_constraints

        live_secondary_without_delegation_change = self.live_secondary_without_delegation_change

        known_import_export_exclusions: list[str] | Unset = UNSET
        if not isinstance(self.known_import_export_exclusions, Unset):
            known_import_export_exclusions = self.known_import_export_exclusions

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "can_list_zones": can_list_zones,
                "can_read_records": can_read_records,
                "can_write_records": can_write_records,
                "supports_comments": supports_comments,
                "supports_tags": supports_tags,
                "supports_proxied_records": supports_proxied_records,
                "supports_alias_flattening": supports_alias_flattening,
                "supports_dnssec_status_read": supports_dnssec_status_read,
                "exposes_assigned_nameservers": exposes_assigned_nameservers,
                "exposes_registrar_constraints": exposes_registrar_constraints,
                "live_secondary_without_delegation_change": live_secondary_without_delegation_change,
            }
        )
        if known_import_export_exclusions is not UNSET:
            field_dict["known_import_export_exclusions"] = known_import_export_exclusions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_list_zones = d.pop("can_list_zones")

        can_read_records = d.pop("can_read_records")

        can_write_records = d.pop("can_write_records")

        supports_comments = d.pop("supports_comments")

        supports_tags = d.pop("supports_tags")

        supports_proxied_records = d.pop("supports_proxied_records")

        supports_alias_flattening = d.pop("supports_alias_flattening")

        supports_dnssec_status_read = d.pop("supports_dnssec_status_read")

        exposes_assigned_nameservers = d.pop("exposes_assigned_nameservers")

        exposes_registrar_constraints = d.pop("exposes_registrar_constraints")

        live_secondary_without_delegation_change = d.pop("live_secondary_without_delegation_change")

        known_import_export_exclusions = cast(list[str], d.pop("known_import_export_exclusions", UNSET))

        dns_control_provider_capabilities = cls(
            can_list_zones=can_list_zones,
            can_read_records=can_read_records,
            can_write_records=can_write_records,
            supports_comments=supports_comments,
            supports_tags=supports_tags,
            supports_proxied_records=supports_proxied_records,
            supports_alias_flattening=supports_alias_flattening,
            supports_dnssec_status_read=supports_dnssec_status_read,
            exposes_assigned_nameservers=exposes_assigned_nameservers,
            exposes_registrar_constraints=exposes_registrar_constraints,
            live_secondary_without_delegation_change=live_secondary_without_delegation_change,
            known_import_export_exclusions=known_import_export_exclusions,
        )

        return dns_control_provider_capabilities
