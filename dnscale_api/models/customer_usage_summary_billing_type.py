from enum import Enum


class CustomerUsageSummaryBillingType(str, Enum):
    METERED = "metered"
    SUBSCRIPTION = "subscription"

    def __str__(self) -> str:
        return str(self.value)
