"""Convenience methods for record CRUD."""

from __future__ import annotations

from uuid import UUID

from dnscale_api import AuthenticatedClient
from dnscale_api.api.records import (
    create_record,
    delete_record,
    get_record,
    list_records,
    update_record,
)
from dnscale_api.models.create_record_request import CreateRecordRequest
from dnscale_api.models.record import Record
from dnscale_api.models.record_response import RecordResponse
from dnscale_api.models.record_type import RecordType
from dnscale_api.models.records_data import RecordsData
from dnscale_api.models.records_response import RecordsResponse
from dnscale_api.types import UNSET, Unset

from .errors import expect, unwrap
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
