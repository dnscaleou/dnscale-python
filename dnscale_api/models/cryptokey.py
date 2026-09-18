from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.cryptokey_keytype import CryptokeyKeytype
from ..types import UNSET, Unset

T = TypeVar("T", bound="Cryptokey")


@_attrs_define
class Cryptokey:
    """
    Attributes:
        id (int):
        active (bool):
        published (bool):
        keytype (CryptokeyKeytype):
        algorithm (str):
        bits (int):
        dnskey (str):
        ds (list[str]):
        cds (list[str]):
        keytag (int | Unset):
        privatekey (str | Unset):
    """

    id: int
    active: bool
    published: bool
    keytype: CryptokeyKeytype
    algorithm: str
    bits: int
    dnskey: str
    ds: list[str]
    cds: list[str]
    keytag: int | Unset = UNSET
    privatekey: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        active = self.active

        published = self.published

        keytype = self.keytype.value

        algorithm = self.algorithm

        bits = self.bits

        dnskey = self.dnskey

        ds = self.ds

        cds = self.cds

        keytag = self.keytag

        privatekey = self.privatekey

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "active": active,
                "published": published,
                "keytype": keytype,
                "algorithm": algorithm,
                "bits": bits,
                "dnskey": dnskey,
                "ds": ds,
                "cds": cds,
            }
        )
        if keytag is not UNSET:
            field_dict["keytag"] = keytag
        if privatekey is not UNSET:
            field_dict["privatekey"] = privatekey

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        active = d.pop("active")

        published = d.pop("published")

        keytype = CryptokeyKeytype(d.pop("keytype"))

        algorithm = d.pop("algorithm")

        bits = d.pop("bits")

        dnskey = d.pop("dnskey")

        ds = cast(list[str], d.pop("ds"))

        cds = cast(list[str], d.pop("cds"))

        keytag = d.pop("keytag", UNSET)

        privatekey = d.pop("privatekey", UNSET)

        cryptokey = cls(
            id=id,
            active=active,
            published=published,
            keytype=keytype,
            algorithm=algorithm,
            bits=bits,
            dnskey=dnskey,
            ds=ds,
            cds=cds,
            keytag=keytag,
            privatekey=privatekey,
        )

        return cryptokey
