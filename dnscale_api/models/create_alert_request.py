from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.alert_scope_type import AlertScopeType
from ..models.alert_severity import AlertSeverity
from ..models.alert_status import AlertStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_channel import AlertChannel
    from ..models.alert_threshold_config import AlertThresholdConfig
    from ..models.create_alert_request_actions import CreateAlertRequestActions


T = TypeVar("T", bound="CreateAlertRequest")


@_attrs_define
class CreateAlertRequest:
    """
    Attributes:
        scope_type (AlertScopeType):
        scope_id (str):
        thresholds (list[int]):
        channels (list[AlertChannel]):
        threshold_config (AlertThresholdConfig | Unset):
        actions (CreateAlertRequestActions | Unset):
        status (AlertStatus | Unset):
        severity (AlertSeverity | Unset):
        cooldown_seconds (int | Unset):
    """

    scope_type: AlertScopeType
    scope_id: str
    thresholds: list[int]
    channels: list[AlertChannel]
    threshold_config: AlertThresholdConfig | Unset = UNSET
    actions: CreateAlertRequestActions | Unset = UNSET
    status: AlertStatus | Unset = UNSET
    severity: AlertSeverity | Unset = UNSET
    cooldown_seconds: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        scope_type = self.scope_type.value

        scope_id = self.scope_id

        thresholds = self.thresholds

        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()
            channels.append(channels_item)

        threshold_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.threshold_config, Unset):
            threshold_config = self.threshold_config.to_dict()

        actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        cooldown_seconds = self.cooldown_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "scope_type": scope_type,
                "scope_id": scope_id,
                "thresholds": thresholds,
                "channels": channels,
            }
        )
        if threshold_config is not UNSET:
            field_dict["threshold_config"] = threshold_config
        if actions is not UNSET:
            field_dict["actions"] = actions
        if status is not UNSET:
            field_dict["status"] = status
        if severity is not UNSET:
            field_dict["severity"] = severity
        if cooldown_seconds is not UNSET:
            field_dict["cooldown_seconds"] = cooldown_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_channel import AlertChannel
        from ..models.alert_threshold_config import AlertThresholdConfig
        from ..models.create_alert_request_actions import CreateAlertRequestActions

        d = dict(src_dict)
        scope_type = AlertScopeType(d.pop("scope_type"))

        scope_id = d.pop("scope_id")

        thresholds = cast(list[int], d.pop("thresholds"))

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = AlertChannel.from_dict(channels_item_data)

            channels.append(channels_item)

        _threshold_config = d.pop("threshold_config", UNSET)
        threshold_config: AlertThresholdConfig | Unset
        if isinstance(_threshold_config, Unset):
            threshold_config = UNSET
        else:
            threshold_config = AlertThresholdConfig.from_dict(_threshold_config)

        _actions = d.pop("actions", UNSET)
        actions: CreateAlertRequestActions | Unset
        if isinstance(_actions, Unset):
            actions = UNSET
        else:
            actions = CreateAlertRequestActions.from_dict(_actions)

        _status = d.pop("status", UNSET)
        status: AlertStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AlertStatus(_status)

        _severity = d.pop("severity", UNSET)
        severity: AlertSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = AlertSeverity(_severity)

        cooldown_seconds = d.pop("cooldown_seconds", UNSET)

        create_alert_request = cls(
            scope_type=scope_type,
            scope_id=scope_id,
            thresholds=thresholds,
            channels=channels,
            threshold_config=threshold_config,
            actions=actions,
            status=status,
            severity=severity,
            cooldown_seconds=cooldown_seconds,
        )

        return create_alert_request
