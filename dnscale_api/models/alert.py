from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.alert_scope_type import AlertScopeType
from ..models.alert_severity import AlertSeverity
from ..models.alert_status import AlertStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_actions import AlertActions
    from ..models.alert_channel import AlertChannel
    from ..models.alert_threshold_config import AlertThresholdConfig


T = TypeVar("T", bound="Alert")


@_attrs_define
class Alert:
    """
    Attributes:
        id (str):
        scope_type (AlertScopeType):
        scope_id (str):
        thresholds (list[int]):
        channels (list[AlertChannel]):
        actions (AlertActions):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        threshold_config (AlertThresholdConfig | Unset):
        status (AlertStatus | Unset):
        severity (AlertSeverity | Unset):
        cooldown_seconds (int | Unset):
        last_triggered_at (datetime.datetime | None | Unset):
    """

    id: str
    scope_type: AlertScopeType
    scope_id: str
    thresholds: list[int]
    channels: list[AlertChannel]
    actions: AlertActions
    created_at: datetime.datetime
    updated_at: datetime.datetime
    threshold_config: AlertThresholdConfig | Unset = UNSET
    status: AlertStatus | Unset = UNSET
    severity: AlertSeverity | Unset = UNSET
    cooldown_seconds: int | Unset = UNSET
    last_triggered_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        scope_type = self.scope_type.value

        scope_id = self.scope_id

        thresholds = self.thresholds

        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()
            channels.append(channels_item)

        actions = self.actions.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        threshold_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.threshold_config, Unset):
            threshold_config = self.threshold_config.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        cooldown_seconds = self.cooldown_seconds

        last_triggered_at: None | str | Unset
        if isinstance(self.last_triggered_at, Unset):
            last_triggered_at = UNSET
        elif isinstance(self.last_triggered_at, datetime.datetime):
            last_triggered_at = self.last_triggered_at.isoformat()
        else:
            last_triggered_at = self.last_triggered_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "scope_type": scope_type,
                "scope_id": scope_id,
                "thresholds": thresholds,
                "channels": channels,
                "actions": actions,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if threshold_config is not UNSET:
            field_dict["threshold_config"] = threshold_config
        if status is not UNSET:
            field_dict["status"] = status
        if severity is not UNSET:
            field_dict["severity"] = severity
        if cooldown_seconds is not UNSET:
            field_dict["cooldown_seconds"] = cooldown_seconds
        if last_triggered_at is not UNSET:
            field_dict["last_triggered_at"] = last_triggered_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_actions import AlertActions
        from ..models.alert_channel import AlertChannel
        from ..models.alert_threshold_config import AlertThresholdConfig

        d = dict(src_dict)
        id = d.pop("id")

        scope_type = AlertScopeType(d.pop("scope_type"))

        scope_id = d.pop("scope_id")

        thresholds = cast(list[int], d.pop("thresholds"))

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = AlertChannel.from_dict(channels_item_data)

            channels.append(channels_item)

        actions = AlertActions.from_dict(d.pop("actions"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        _threshold_config = d.pop("threshold_config", UNSET)
        threshold_config: AlertThresholdConfig | Unset
        if isinstance(_threshold_config, Unset):
            threshold_config = UNSET
        else:
            threshold_config = AlertThresholdConfig.from_dict(_threshold_config)

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

        def _parse_last_triggered_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_triggered_at_type_0 = isoparse(data)

                return last_triggered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_triggered_at = _parse_last_triggered_at(d.pop("last_triggered_at", UNSET))

        alert = cls(
            id=id,
            scope_type=scope_type,
            scope_id=scope_id,
            thresholds=thresholds,
            channels=channels,
            actions=actions,
            created_at=created_at,
            updated_at=updated_at,
            threshold_config=threshold_config,
            status=status,
            severity=severity,
            cooldown_seconds=cooldown_seconds,
            last_triggered_at=last_triggered_at,
        )

        return alert
