from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.alert import Alert


T = TypeVar("T", bound="AlertData")


@_attrs_define
class AlertData:
    """
    Attributes:
        alert (Alert):
    """

    alert: Alert

    def to_dict(self) -> dict[str, Any]:
        alert = self.alert.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "alert": alert,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert import Alert

        d = dict(src_dict)
        alert = Alert.from_dict(d.pop("alert"))

        alert_data = cls(
            alert=alert,
        )

        return alert_data
