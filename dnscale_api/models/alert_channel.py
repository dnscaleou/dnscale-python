from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.alert_channel_type import AlertChannelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertChannel")


@_attrs_define
class AlertChannel:
    """
    Attributes:
        type_ (AlertChannelType):
        email_to (list[str] | Unset):
        slack_url (None | str | Unset):
        webhook_url (None | str | Unset):
        pager_key (None | str | Unset):
        enabled (bool | Unset):  Default: True.
    """

    type_: AlertChannelType
    email_to: list[str] | Unset = UNSET
    slack_url: None | str | Unset = UNSET
    webhook_url: None | str | Unset = UNSET
    pager_key: None | str | Unset = UNSET
    enabled: bool | Unset = True

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        email_to: list[str] | Unset = UNSET
        if not isinstance(self.email_to, Unset):
            email_to = self.email_to

        slack_url: None | str | Unset
        if isinstance(self.slack_url, Unset):
            slack_url = UNSET
        else:
            slack_url = self.slack_url

        webhook_url: None | str | Unset
        if isinstance(self.webhook_url, Unset):
            webhook_url = UNSET
        else:
            webhook_url = self.webhook_url

        pager_key: None | str | Unset
        if isinstance(self.pager_key, Unset):
            pager_key = UNSET
        else:
            pager_key = self.pager_key

        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if email_to is not UNSET:
            field_dict["email_to"] = email_to
        if slack_url is not UNSET:
            field_dict["slack_url"] = slack_url
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url
        if pager_key is not UNSET:
            field_dict["pager_key"] = pager_key
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = AlertChannelType(d.pop("type"))

        email_to = cast(list[str], d.pop("email_to", UNSET))

        def _parse_slack_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slack_url = _parse_slack_url(d.pop("slack_url", UNSET))

        def _parse_webhook_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        webhook_url = _parse_webhook_url(d.pop("webhook_url", UNSET))

        def _parse_pager_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pager_key = _parse_pager_key(d.pop("pager_key", UNSET))

        enabled = d.pop("enabled", UNSET)

        alert_channel = cls(
            type_=type_,
            email_to=email_to,
            slack_url=slack_url,
            webhook_url=webhook_url,
            pager_key=pager_key,
            enabled=enabled,
        )

        return alert_channel
