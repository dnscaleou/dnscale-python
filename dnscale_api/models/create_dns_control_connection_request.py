from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_dns_control_connection_request_mode import (
    CreateDNSControlConnectionRequestMode,
)
from ..models.create_dns_control_connection_request_provider import (
    CreateDNSControlConnectionRequestProvider,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_credentials import ProviderCredentials


T = TypeVar("T", bound="CreateDNSControlConnectionRequest")


@_attrs_define
class CreateDNSControlConnectionRequest:
    """
    Attributes:
        provider (CreateDNSControlConnectionRequestProvider):
        name (str | Unset):
        mode (CreateDNSControlConnectionRequestMode | Unset):  Default: CreateDNSControlConnectionRequestMode.READ_ONLY.
        scopes (list[str] | Unset):
        credentials (ProviderCredentials | Unset): Credentials are accepted on create and are never returned.
        api_token (str | Unset):
        access_key_id (str | Unset):
        secret_access_key (str | Unset):
        region (str | Unset):
    """

    provider: CreateDNSControlConnectionRequestProvider
    name: str | Unset = UNSET
    mode: CreateDNSControlConnectionRequestMode | Unset = CreateDNSControlConnectionRequestMode.READ_ONLY
    scopes: list[str] | Unset = UNSET
    credentials: ProviderCredentials | Unset = UNSET
    api_token: str | Unset = UNSET
    access_key_id: str | Unset = UNSET
    secret_access_key: str | Unset = UNSET
    region: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        name = self.name

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes

        credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        api_token = self.api_token

        access_key_id = self.access_key_id

        secret_access_key = self.secret_access_key

        region = self.region

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "provider": provider,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if mode is not UNSET:
            field_dict["mode"] = mode
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if api_token is not UNSET:
            field_dict["api_token"] = api_token
        if access_key_id is not UNSET:
            field_dict["access_key_id"] = access_key_id
        if secret_access_key is not UNSET:
            field_dict["secret_access_key"] = secret_access_key
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_credentials import ProviderCredentials

        d = dict(src_dict)
        provider = CreateDNSControlConnectionRequestProvider(d.pop("provider"))

        name = d.pop("name", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: CreateDNSControlConnectionRequestMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = CreateDNSControlConnectionRequestMode(_mode)

        scopes = cast(list[str], d.pop("scopes", UNSET))

        _credentials = d.pop("credentials", UNSET)
        credentials: ProviderCredentials | Unset
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = ProviderCredentials.from_dict(_credentials)

        api_token = d.pop("api_token", UNSET)

        access_key_id = d.pop("access_key_id", UNSET)

        secret_access_key = d.pop("secret_access_key", UNSET)

        region = d.pop("region", UNSET)

        create_dns_control_connection_request = cls(
            provider=provider,
            name=name,
            mode=mode,
            scopes=scopes,
            credentials=credentials,
            api_token=api_token,
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
            region=region,
        )

        return create_dns_control_connection_request
