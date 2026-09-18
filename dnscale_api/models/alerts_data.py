from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.alert import Alert


T = TypeVar("T", bound="AlertsData")


@_attrs_define
class AlertsData:
    """
    Attributes:
        alerts (list[Alert]):
    """

    alerts: list[Alert]

    def to_dict(self) -> dict[str, Any]:
        alerts = []
        for alerts_item_data in self.alerts:
            alerts_item = alerts_item_data.to_dict()
            alerts.append(alerts_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "alerts": alerts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert import Alert

        d = dict(src_dict)
        alerts = []
        _alerts = d.pop("alerts")
        for alerts_item_data in _alerts:
            alerts_item = Alert.from_dict(alerts_item_data)

            alerts.append(alerts_item)

        alerts_data = cls(
            alerts=alerts,
        )

        return alerts_data
