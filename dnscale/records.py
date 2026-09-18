"""Convenience methods for record CRUD."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from uuid import UUID

from dnscale_api import AuthenticatedClient
from dnscale_api.api.records import (
    create_record,
    delete_record,
    delete_records_by_name_and_type,
    get_record,
    list_records,
    update_record,
    update_record_by_name_and_type,
)
from dnscale_api.models.create_record_request import CreateRecordRequest
from dnscale_api.models.record import Record
from dnscale_api.models.record_response import RecordResponse
from dnscale_api.models.record_type import RecordType
from dnscale_api.models.records_data import RecordsData
from dnscale_api.models.records_response import RecordsResponse
from dnscale_api.models.update_record_by_name_request import UpdateRecordByNameRequest
from dnscale_api.types import UNSET, Unset

from .errors import expect, unwrap
from .pagination import next_offset, validate_page_size
from .zones import _uuid


def _record_body(
    *,
    name: str,
    record_type: RecordType | str,
    content: str,
    ttl: int,
    priority: int | None | Unset,
    disabled: bool,
    comment: str | None | Unset,
) -> CreateRecordRequest:
    return CreateRecordRequest(
        name=name,
        type_=RecordType(record_type),
        content=content,
        ttl=ttl,
        priority=priority,
        disabled=disabled,
        comment=comment,
    )


class Records:
    """Typed record operations bound to a DNScale client."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def iter(self, zone_id: str | UUID, *, page_size: int = 100) -> Iterator[Record]:
        """Lazily fetch all records, including server-limited pages."""
        validate_page_size(page_size)
        offset = 0
        while True:
            page = self.list(zone_id, offset=offset, limit=page_size)
            following = next_offset(page.pagination, offset, len(page.records))
            yield from page.records
            if following is None:
                return
            offset = following

    async def aiter(self, zone_id: str | UUID, *, page_size: int = 100) -> AsyncIterator[Record]:
        validate_page_size(page_size)
        offset = 0
        while True:
            page = await self.alist(zone_id, offset=offset, limit=page_size)
            following = next_offset(page.pagination, offset, len(page.records))
            for record in page.records:
                yield record
            if following is None:
                return
            offset = following

    def update_by_name(
        self,
        zone_id: str | UUID,
        name: str,
        type_: RecordType | str,
        *,
        body: UpdateRecordByNameRequest,
        content: str | Unset = UNSET,
    ) -> Record:
        """Update by owner name/type. See API semantics for multi-value RRsets."""
        response = update_record_by_name_and_type.sync_detailed(
            _uuid(zone_id),
            name,
            RecordType(type_),
            client=self._client,
            body=body,
            content=content,
        )
        return expect(unwrap(response), RecordResponse).data.record

    async def aupdate_by_name(
        self,
        zone_id: str | UUID,
        name: str,
        type_: RecordType | str,
        *,
        body: UpdateRecordByNameRequest,
        content: str | Unset = UNSET,
    ) -> Record:
        response = await update_record_by_name_and_type.asyncio_detailed(
            _uuid(zone_id),
            name,
            RecordType(type_),
            client=self._client,
            body=body,
            content=content,
        )
        return expect(unwrap(response), RecordResponse).data.record

    def delete_by_name(
        self,
        zone_id: str | UUID,
        name: str,
        type_: RecordType | str,
        *,
        content: str | Unset = UNSET,
    ) -> None:
        """Delete one value when content is supplied; otherwise delete the whole RRset."""
        if content == "":
            raise ValueError("content must be non-empty; omit it to delete the whole RRset")
        unwrap(
            delete_records_by_name_and_type.sync_detailed(
                _uuid(zone_id), name, RecordType(type_), client=self._client, content=content
            )
        )

    async def adelete_by_name(
        self,
        zone_id: str | UUID,
        name: str,
        type_: RecordType | str,
        *,
        content: str | Unset = UNSET,
    ) -> None:
        if content == "":
            raise ValueError("content must be non-empty; omit it to delete the whole RRset")
        unwrap(
            await delete_records_by_name_and_type.asyncio_detailed(
                _uuid(zone_id), name, RecordType(type_), client=self._client, content=content
            )
        )

    def list(self, zone_id: str | UUID, *, offset: int = 0, limit: int = 50) -> RecordsData:
        response = list_records.sync_detailed(
            _uuid(zone_id), client=self._client, offset=offset, limit=limit
        )
        return expect(unwrap(response), RecordsResponse).data

    async def alist(self, zone_id: str | UUID, *, offset: int = 0, limit: int = 50) -> RecordsData:
        response = await list_records.asyncio_detailed(
            _uuid(zone_id), client=self._client, offset=offset, limit=limit
        )
        return expect(unwrap(response), RecordsResponse).data

    def get(self, zone_id: str | UUID, record_id: str) -> Record:
        response = get_record.sync_detailed(_uuid(zone_id), record_id, client=self._client)
        return expect(unwrap(response), RecordResponse).data.record

    async def aget(self, zone_id: str | UUID, record_id: str) -> Record:
        response = await get_record.asyncio_detailed(_uuid(zone_id), record_id, client=self._client)
        return expect(unwrap(response), RecordResponse).data.record

    def create(
        self,
        zone_id: str | UUID,
        *,
        name: str,
        type_: RecordType | str,
        content: str,
        ttl: int = 3600,
        priority: int | None | Unset = UNSET,
        disabled: bool = False,
        comment: str | None | Unset = UNSET,
    ) -> Record:
        response = create_record.sync_detailed(
            _uuid(zone_id),
            client=self._client,
            body=_record_body(
                name=name,
                record_type=type_,
                content=content,
                ttl=ttl,
                priority=priority,
                disabled=disabled,
                comment=comment,
            ),
        )
        return expect(unwrap(response), RecordResponse).data.record

    async def acreate(
        self,
        zone_id: str | UUID,
        *,
        name: str,
        type_: RecordType | str,
        content: str,
        ttl: int = 3600,
        priority: int | None | Unset = UNSET,
        disabled: bool = False,
        comment: str | None | Unset = UNSET,
    ) -> Record:
        response = await create_record.asyncio_detailed(
            _uuid(zone_id),
            client=self._client,
            body=_record_body(
                name=name,
                record_type=type_,
                content=content,
                ttl=ttl,
                priority=priority,
                disabled=disabled,
                comment=comment,
            ),
        )
        return expect(unwrap(response), RecordResponse).data.record

    def update(
        self,
        zone_id: str | UUID,
        record_id: str,
        *,
        name: str,
        type_: RecordType | str,
        content: str,
        ttl: int = 3600,
        priority: int | None | Unset = UNSET,
        disabled: bool = False,
        comment: str | None | Unset = UNSET,
    ) -> Record:
        response = update_record.sync_detailed(
            _uuid(zone_id),
            record_id,
            client=self._client,
            body=_record_body(
                name=name,
                record_type=type_,
                content=content,
                ttl=ttl,
                priority=priority,
                disabled=disabled,
                comment=comment,
            ),
        )
        return expect(unwrap(response), RecordResponse).data.record

    async def aupdate(
        self,
        zone_id: str | UUID,
        record_id: str,
        *,
        name: str,
        type_: RecordType | str,
        content: str,
        ttl: int = 3600,
        priority: int | None | Unset = UNSET,
        disabled: bool = False,
        comment: str | None | Unset = UNSET,
    ) -> Record:
        response = await update_record.asyncio_detailed(
            _uuid(zone_id),
            record_id,
            client=self._client,
            body=_record_body(
                name=name,
                record_type=type_,
                content=content,
                ttl=ttl,
                priority=priority,
                disabled=disabled,
                comment=comment,
            ),
        )
        return expect(unwrap(response), RecordResponse).data.record

    def delete(self, zone_id: str | UUID, record_id: str) -> None:
        response = delete_record.sync_detailed(_uuid(zone_id), record_id, client=self._client)
        unwrap(response)

    async def adelete(self, zone_id: str | UUID, record_id: str) -> None:
        response = await delete_record.asyncio_detailed(
            _uuid(zone_id), record_id, client=self._client
        )
        unwrap(response)
