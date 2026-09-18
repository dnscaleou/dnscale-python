from enum import Enum


class DNSControlAuthFieldType(str, Enum):
    PASSWORD = "password"
    SELECT = "select"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
