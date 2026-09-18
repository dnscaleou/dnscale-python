"""Ergonomic entry point for the DNScale Python SDK."""

from dnscale_api.models.record import Record
from dnscale_api.models.record_type import RecordType
from dnscale_api.models.zone import Zone
from dnscale_api.models.zone_region import ZoneRegion
from dnscale_api.models.zone_status import ZoneStatus
from dnscale_api.models.zone_type import ZoneType

from .client import DEFAULT_BASE_URL, DNScale
from .errors import APIError, ProtocolError, RateLimitError

__all__ = (
    "APIError",
    "DEFAULT_BASE_URL",
    "DNScale",
    "ProtocolError",
    "RateLimitError",
    "Record",
    "RecordType",
    "Zone",
    "ZoneRegion",
    "ZoneStatus",
    "ZoneType",
)

__version__ = "0.1.0"
