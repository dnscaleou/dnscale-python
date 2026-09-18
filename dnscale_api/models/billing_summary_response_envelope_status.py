from enum import Enum


class BillingSummaryResponseEnvelopeStatus(str, Enum):
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
