from enum import Enum


class ErrorResponseStatus(str, Enum):
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
