from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dns_control_provider_auth_type import DNSControlProviderAuthType
from ..models.dns_control_provider_type import DNSControlProviderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_control_auth_field import DNSControlAuthField
    from ..models.dns_control_provider_capabilities import DNSControlProviderCapabilities


T = TypeVar("T", bound="DNSControlProvider")


@_attrs_define
class DNSControlProvider:
    """
    Attributes:
        type_ (DNSControlProviderType):
        name (str):
        description (str):
        auth_type (DNSControlProviderAuthType):
        auth_fields (list[DNSControlAuthField]):
        docs_url (str):
        capabilities (DNSControlProviderCapabilities):
        warnings (list[str] | Unset):
    """

    type_: DNSControlProviderType
    name: str
    description: str
    auth_type: DNSControlProviderAuthType
    auth_fields: list[DNSControlAuthField]
    docs_url: str
    capabilities: DNSControlProviderCapabilities
    warnings: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        name = self.name

        description = self.description

        auth_type = self.auth_type.value

        auth_fields = []
        for auth_fields_item_data in self.auth_fields:
            auth_fields_item = auth_fields_item_data.to_dict()
            auth_fields.append(auth_fields_item)

        docs_url = self.docs_url

        capabilities = self.capabilities.to_dict()

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "name": name,
                "description": description,
                "auth_type": auth_type,
                "auth_fields": auth_fields,
                "docs_url": docs_url,
                "capabilities": capabilities,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_auth_field import DNSControlAuthField
        from ..models.dns_control_provider_capabilities import DNSControlProviderCapabilities

        d = dict(src_dict)
        type_ = DNSControlProviderType(d.pop("type"))

        name = d.pop("name")

        description = d.pop("description")

        auth_type = DNSControlProviderAuthType(d.pop("auth_type"))

        auth_fields = []
        _auth_fields = d.pop("auth_fields")
        for auth_fields_item_data in _auth_fields:
            auth_fields_item = DNSControlAuthField.from_dict(auth_fields_item_data)

            auth_fields.append(auth_fields_item)

        docs_url = d.pop("docs_url")

        capabilities = DNSControlProviderCapabilities.from_dict(d.pop("capabilities"))

        warnings = cast(list[str], d.pop("warnings", UNSET))

        dns_control_provider = cls(
            type_=type_,
            name=name,
            description=description,
            auth_type=auth_type,
            auth_fields=auth_fields,
            docs_url=docs_url,
            capabilities=capabilities,
            warnings=warnings,
        )

        return dns_control_provider
