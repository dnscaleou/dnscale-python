from enum import Enum


class ZoneType(str, Enum):
    MASTER = "master"
    SLAVE = "slave"

    def __str__(self) -> str:
        return str(self.value)
