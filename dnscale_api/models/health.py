from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.health_status import HealthStatus

T = TypeVar("T", bound="Health")


@_attrs_define
class Health:
    """
    Attributes:
        status (HealthStatus):
        timestamp (datetime.datetime):
        version (str):
    """

    status: HealthStatus
    timestamp: datetime.datetime
    version: str

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        timestamp = self.timestamp.isoformat()

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "timestamp": timestamp,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = HealthStatus(d.pop("status"))

        timestamp = isoparse(d.pop("timestamp"))

        version = d.pop("version")

        health = cls(
            status=status,
            timestamp=timestamp,
            version=version,
        )

        return health
