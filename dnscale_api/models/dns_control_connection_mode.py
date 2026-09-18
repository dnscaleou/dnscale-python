from enum import Enum


class DNSControlConnectionMode(str, Enum):
    READ_ONLY = "read_only"

    def __str__(self) -> str:
        return str(self.value)
