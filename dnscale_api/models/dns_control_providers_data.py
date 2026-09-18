from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.dns_control_provider import DNSControlProvider


T = TypeVar("T", bound="DNSControlProvidersData")


@_attrs_define
class DNSControlProvidersData:
    """
    Attributes:
        providers (list[DNSControlProvider]):
    """

    providers: list[DNSControlProvider]

    def to_dict(self) -> dict[str, Any]:
        providers = []
        for providers_item_data in self.providers:
            providers_item = providers_item_data.to_dict()
            providers.append(providers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "providers": providers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_control_provider import DNSControlProvider

        d = dict(src_dict)
        providers = []
        _providers = d.pop("providers")
        for providers_item_data in _providers:
            providers_item = DNSControlProvider.from_dict(providers_item_data)

            providers.append(providers_item)

        dns_control_providers_data = cls(
            providers=providers,
        )

        return dns_control_providers_data
