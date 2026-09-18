from enum import Enum


class CreateCryptokeyRequestKeytype(str, Enum):
    CSK = "csk"
    KSK = "ksk"
    ZSK = "zsk"

    def __str__(self) -> str:
        return str(self.value)
