from enum import Enum


class ZoneStatus(str, Enum):
    ACTIVE = "active"
    ERROR = "error"
    PAUSED = "paused"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
