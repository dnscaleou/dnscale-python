from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ProviderCredentials")



@_attrs_define
class ProviderCredentials:
    """ Credentials are accepted on create and are never returned.

        Attributes:
            api_key (str | Unset):
            api_token (str | Unset):
            access_key_id (str | Unset):
            secret_access_key (str | Unset):
            region (str | Unset):
     """

    api_key: str | Unset = UNSET
    api_token: str | Unset = UNSET
    access_key_id: str | Unset = UNSET
    secret_access_key: str | Unset = UNSET
    region: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        api_token = self.api_token

        access_key_id = self.access_key_id

        secret_access_key = self.secret_access_key

        region = self.region


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
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
        d = dict(src_dict)
        api_key = d.pop("api_key", UNSET)

        api_token = d.pop("api_token", UNSET)

        access_key_id = d.pop("access_key_id", UNSET)

        secret_access_key = d.pop("secret_access_key", UNSET)

        region = d.pop("region", UNSET)

        provider_credentials = cls(
            api_key=api_key,
            api_token=api_token,
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
            region=region,
        )

        return provider_credentials

