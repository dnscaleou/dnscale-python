from enum import Enum


class DNSControlSnapshotDiffChangeType(str, Enum):
    ADDED_RECORD_SET = "added_record_set"
    PROVIDER_METADATA_CHANGED = "provider_metadata_changed"
    REMOVED_RECORD_SET = "removed_record_set"
    TTL_CHANGED = "ttl_changed"
    VALUE_CHANGED = "value_changed"

    def __str__(self) -> str:
        return str(self.value)
