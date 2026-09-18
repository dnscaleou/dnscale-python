from enum import Enum


class DNSControlConnectionStatus(str, Enum):
    DISABLED = "disabled"
    ERROR = "error"
    PENDING = "pending"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
