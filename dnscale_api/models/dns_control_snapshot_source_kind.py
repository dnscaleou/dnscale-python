from enum import Enum


class DNSControlSnapshotSourceKind(str, Enum):
    PROVIDER_API = "provider_api"

    def __str__(self) -> str:
        return str(self.value)
