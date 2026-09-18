from enum import Enum


class AlertChannelType(str, Enum):
    EMAIL = "email"
    PAGERDUTY = "pagerduty"
    SLACK = "slack"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
