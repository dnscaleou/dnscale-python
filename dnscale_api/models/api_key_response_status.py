from enum import Enum


class APIKeyResponseStatus(str, Enum):
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
