"""Pagination guards shared by synchronous and asynchronous iterators."""

from dnscale_api.models.pagination import Pagination

from .errors import ProtocolError


def validate_page_size(page_size: int) -> None:
    if not 1 <= page_size <= 100:
        raise ValueError("page_size must be between 1 and 100")


def next_offset(page: Pagination, offset: int, count: int) -> int | None:
    if page.offset != offset or page.count != count:
        raise ProtocolError("DNScale returned inconsistent pagination metadata")
    if not page.has_more:
        return None
    if count == 0:
        raise ProtocolError("DNScale pagination has_more is true on an empty page")
    return offset + count
