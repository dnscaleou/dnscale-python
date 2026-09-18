from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.health import Health


T = TypeVar("T", bound="HealthData")


@_attrs_define
class HealthData:
    """
    Attributes:
        health (Health):
    """

    health: Health

    def to_dict(self) -> dict[str, Any]:
        health = self.health.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "health": health,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.health import Health

        d = dict(src_dict)
        health = Health.from_dict(d.pop("health"))

        health_data = cls(
            health=health,
        )

        return health_data
