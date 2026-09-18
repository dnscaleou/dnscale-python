from enum import Enum


class ZoneRegion(str, Enum):
    EU = "EU"
    EU_GLOBAL = "EU_GLOBAL"
    GLOBAL = "GLOBAL"

    def __str__(self) -> str:
        return str(self.value)
