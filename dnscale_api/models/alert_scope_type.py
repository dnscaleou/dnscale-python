from enum import Enum


class AlertScopeType(str, Enum):
    ACCOUNT = "account"
    ZONE = "zone"

    def __str__(self) -> str:
        return str(self.value)
