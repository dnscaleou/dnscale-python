from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_cryptokey_request_keytype import CreateCryptokeyRequestKeytype
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCryptokeyRequest")


@_attrs_define
class CreateCryptokeyRequest:
    """
    Attributes:
        active (bool | Unset):
        published (bool | Unset):
        keytype (CreateCryptokeyRequestKeytype | Unset):
        algorithm (str | Unset):
        bits (int | Unset):
        content (str | Unset):
        dnskey (str | Unset):
        ds (list[str] | Unset):
        cds (list[str] | Unset):
        privatekey (str | Unset):
    """

    active: bool | Unset = UNSET
    published: bool | Unset = UNSET
    keytype: CreateCryptokeyRequestKeytype | Unset = UNSET
    algorithm: str | Unset = UNSET
    bits: int | Unset = UNSET
    content: str | Unset = UNSET
    dnskey: str | Unset = UNSET
    ds: list[str] | Unset = UNSET
    cds: list[str] | Unset = UNSET
    privatekey: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        published = self.published

        keytype: str | Unset = UNSET
        if not isinstance(self.keytype, Unset):
            keytype = self.keytype.value

        algorithm = self.algorithm

        bits = self.bits

        content = self.content

        dnskey = self.dnskey

        ds: list[str] | Unset = UNSET
        if not isinstance(self.ds, Unset):
            ds = self.ds

        cds: list[str] | Unset = UNSET
        if not isinstance(self.cds, Unset):
            cds = self.cds

        privatekey = self.privatekey

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if published is not UNSET:
            field_dict["published"] = published
        if keytype is not UNSET:
            field_dict["keytype"] = keytype
        if algorithm is not UNSET:
            field_dict["algorithm"] = algorithm
        if bits is not UNSET:
            field_dict["bits"] = bits
        if content is not UNSET:
            field_dict["content"] = content
        if dnskey is not UNSET:
            field_dict["dnskey"] = dnskey
        if ds is not UNSET:
            field_dict["ds"] = ds
        if cds is not UNSET:
            field_dict["cds"] = cds
        if privatekey is not UNSET:
            field_dict["privatekey"] = privatekey

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active", UNSET)

        published = d.pop("published", UNSET)

        _keytype = d.pop("keytype", UNSET)
        keytype: CreateCryptokeyRequestKeytype | Unset
        if isinstance(_keytype, Unset):
            keytype = UNSET
        else:
            keytype = CreateCryptokeyRequestKeytype(_keytype)

        algorithm = d.pop("algorithm", UNSET)

        bits = d.pop("bits", UNSET)

        content = d.pop("content", UNSET)

        dnskey = d.pop("dnskey", UNSET)

        ds = cast(list[str], d.pop("ds", UNSET))

        cds = cast(list[str], d.pop("cds", UNSET))

        privatekey = d.pop("privatekey", UNSET)

        create_cryptokey_request = cls(
            active=active,
            published=published,
            keytype=keytype,
            algorithm=algorithm,
            bits=bits,
            content=content,
            dnskey=dnskey,
            ds=ds,
            cds=cds,
            privatekey=privatekey,
        )

        return create_cryptokey_request
