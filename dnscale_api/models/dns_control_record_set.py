from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.dns_control_record_set_provider_metadata import DNSControlRecordSetProviderMetadata
    from ..models.dns_control_record_set_raw_refs_item import DNSControlRecordSetRawRefsItem
    from ..models.dns_control_record_set_values_item import DNSControlRecordSetValuesItem


T = TypeVar("T", bound="DNSControlRecordSet")


@_attrs_define
class DNSControlRecordSet:
    """
    Attributes:
        id (UUID):
        snapshot_id (UUID):
        record_set_key (str):
        owner_name (str):
        rrtype (str):
        dns_class (str):
        routing_policy_key (str):
        ttl (int):
        values (list[DNSControlRecordSetValuesItem]):
        provider_metadata (DNSControlRecordSetProviderMetadata):
        raw_refs (list[DNSControlRecordSetRawRefsItem]):
        portable_hash (str):
        value_hash (str):
        provider_hash (str):
        unsupported (bool):
        warnings (list[str]):
    """

    id: UUID
    snapshot_id: UUID
    record_set_key: str
    owner_name: str
    rrtype: str
    dns_class: str
    routing_policy_key: str
    ttl: int
    values: list[DNSControlRecordSetValuesItem]
    provider_metadata: DNSControlRecordSetProviderMetadata
    raw_refs: list[DNSControlRecordSetRawRefsItem]
    portable_hash: str
    value_hash: str
    provider_hash: str
    unsupported: bool
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        snapshot_id = str(self.snapshot_id)

        record_set_key = self.record_set_key

        owner_name = self.owner_name

        rrtype = self.rrtype

        dns_class = self.dns_class

        routing_policy_key = self.routing_policy_key

        ttl = self.ttl

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        provider_metadata = self.provider_metadata.to_dict()

        raw_refs = []
        for raw_refs_item_data in self.raw_refs:
            raw_refs_item = raw_refs_item_data.to_dict()
            raw_refs.append(raw_refs_item)

        portable_hash = self.portable_hash

        value_hash = self.value_hash

        provider_hash = self.provider_hash

        unsupported = self.unsupported

        warnings = self.warnings

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "snapshot_id": snapshot_id,
                "record_set_key": record_set_key,
                "owner_name": owner_name,
                "rrtype": rrtype,
                "dns_class": dns_class,
                "routing_policy_key": routing_policy_key,
                "ttl": ttl,
                "values": values,
                "provider_metadata": provider_metadata,
                "raw_refs": raw_refs,
                "portable_hash": portable_hash,
                "value_hash": value_hash,
                "provider_hash": provider_hash,
                "unsupported": unsupported,
                "warnings": warnings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_record_set_provider_metadata import (
            DNSControlRecordSetProviderMetadata,
        )
        from ..models.dns_control_record_set_raw_refs_item import DNSControlRecordSetRawRefsItem
        from ..models.dns_control_record_set_values_item import DNSControlRecordSetValuesItem

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        snapshot_id = UUID(d.pop("snapshot_id"))

        record_set_key = d.pop("record_set_key")

        owner_name = d.pop("owner_name")

        rrtype = d.pop("rrtype")

        dns_class = d.pop("dns_class")

        routing_policy_key = d.pop("routing_policy_key")

        ttl = d.pop("ttl")

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = DNSControlRecordSetValuesItem.from_dict(values_item_data)

            values.append(values_item)

        provider_metadata = DNSControlRecordSetProviderMetadata.from_dict(d.pop("provider_metadata"))

        raw_refs = []
        _raw_refs = d.pop("raw_refs")
        for raw_refs_item_data in _raw_refs:
            raw_refs_item = DNSControlRecordSetRawRefsItem.from_dict(raw_refs_item_data)

            raw_refs.append(raw_refs_item)

        portable_hash = d.pop("portable_hash")

        value_hash = d.pop("value_hash")

        provider_hash = d.pop("provider_hash")

        unsupported = d.pop("unsupported")

        warnings = cast(list[str], d.pop("warnings"))

        dns_control_record_set = cls(
            id=id,
            snapshot_id=snapshot_id,
            record_set_key=record_set_key,
            owner_name=owner_name,
            rrtype=rrtype,
            dns_class=dns_class,
            routing_policy_key=routing_policy_key,
            ttl=ttl,
            values=values,
            provider_metadata=provider_metadata,
            raw_refs=raw_refs,
            portable_hash=portable_hash,
            value_hash=value_hash,
            provider_hash=provider_hash,
            unsupported=unsupported,
            warnings=warnings,
        )

        return dns_control_record_set
