from enum import Enum


class APIKeyZoneScopeRecordAccess(str, Enum):
    ALL = "all"
    NAMES = "names"

    def __str__(self) -> str:
        return str(self.value)
