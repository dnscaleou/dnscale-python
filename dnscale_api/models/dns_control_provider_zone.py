from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_control_provider_zone_dnssec import DNSControlProviderZoneDnssec
    from ..models.dns_control_provider_zone_metadata import DNSControlProviderZoneMetadata


T = TypeVar("T", bound="DNSControlProviderZone")


@_attrs_define
class DNSControlProviderZone:
    """
    Attributes:
        id (str):
        name (str):
        status (str | Unset):
        record_count (int | Unset):
        nameservers (list[str] | Unset):
        dnssec (DNSControlProviderZoneDnssec | Unset):
        metadata (DNSControlProviderZoneMetadata | Unset):
    """

    id: str
    name: str
    status: str | Unset = UNSET
    record_count: int | Unset = UNSET
    nameservers: list[str] | Unset = UNSET
    dnssec: DNSControlProviderZoneDnssec | Unset = UNSET
    metadata: DNSControlProviderZoneMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        record_count = self.record_count

        nameservers: list[str] | Unset = UNSET
        if not isinstance(self.nameservers, Unset):
            nameservers = self.nameservers

        dnssec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dnssec, Unset):
            dnssec = self.dnssec.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if record_count is not UNSET:
            field_dict["record_count"] = record_count
        if nameservers is not UNSET:
            field_dict["nameservers"] = nameservers
        if dnssec is not UNSET:
            field_dict["dnssec"] = dnssec
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_provider_zone_dnssec import DNSControlProviderZoneDnssec
        from ..models.dns_control_provider_zone_metadata import DNSControlProviderZoneMetadata

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        status = d.pop("status", UNSET)

        record_count = d.pop("record_count", UNSET)

        nameservers = cast(list[str], d.pop("nameservers", UNSET))

        _dnssec = d.pop("dnssec", UNSET)
        dnssec: DNSControlProviderZoneDnssec | Unset
        if isinstance(_dnssec, Unset):
            dnssec = UNSET
        else:
            dnssec = DNSControlProviderZoneDnssec.from_dict(_dnssec)

        _metadata = d.pop("metadata", UNSET)
        metadata: DNSControlProviderZoneMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DNSControlProviderZoneMetadata.from_dict(_metadata)

        dns_control_provider_zone = cls(
            id=id,
            name=name,
            status=status,
            record_count=record_count,
            nameservers=nameservers,
            dnssec=dnssec,
            metadata=metadata,
        )

        return dns_control_provider_zone
