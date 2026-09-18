"""Convenience methods for zone CRUD."""

from __future__ import annotations

from uuid import UUID

from dnscale_api import AuthenticatedClient
from dnscale_api.api.zones import create_zone, delete_zone, get_zone, list_zones, update_zone
from dnscale_api.models.create_zone_request import CreateZoneRequest
from dnscale_api.models.update_zone_request import UpdateZoneRequest
from dnscale_api.models.zone import Zone
from dnscale_api.models.zone_region import ZoneRegion
from dnscale_api.models.zone_response import ZoneResponse
from dnscale_api.models.zone_status import ZoneStatus
from dnscale_api.models.zone_type import ZoneType
from dnscale_api.models.zones_data import ZonesData
from dnscale_api.models.zones_response import ZonesResponse
from dnscale_api.types import UNSET, Unset

from .errors import expect, unwrap


def _uuid(value: str | UUID) -> UUID:
    return value if isinstance(value, UUID) else UUID(value)


class Zones:
    """Typed zone operations bound to a DNScale client."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def list(self, *, offset: int = 0, limit: int = 10) -> ZonesData:
        response = list_zones.sync_detailed(client=self._client, offset=offset, limit=limit)
        return expect(unwrap(response), ZonesResponse).data

    async def alist(self, *, offset: int = 0, limit: int = 10) -> ZonesData:
        response = await list_zones.asyncio_detailed(
            client=self._client, offset=offset, limit=limit
        )
        return expect(unwrap(response), ZonesResponse).data

    def get(self, zone_id: str | UUID) -> Zone:
        response = get_zone.sync_detailed(_uuid(zone_id), client=self._client)
        return expect(unwrap(response), ZoneResponse).data.zone

    async def aget(self, zone_id: str | UUID) -> Zone:
        response = await get_zone.asyncio_detailed(_uuid(zone_id), client=self._client)
        return expect(unwrap(response), ZoneResponse).data.zone

    def create(
        self,
        name: str,
        *,
        type_: ZoneType | str | Unset = UNSET,
        region: ZoneRegion | str | Unset = UNSET,
        status: ZoneStatus | str | Unset = UNSET,
    ) -> Zone:
        body = CreateZoneRequest(
            name=name,
            type_=type_ if isinstance(type_, Unset) else ZoneType(type_),
            region=region if isinstance(region, Unset) else ZoneRegion(region),
            status=status if isinstance(status, Unset) else ZoneStatus(status),
        )
        response = create_zone.sync_detailed(client=self._client, body=body)
        return expect(unwrap(response), ZoneResponse).data.zone

    async def acreate(
        self,
        name: str,
        *,
        type_: ZoneType | str | Unset = UNSET,
        region: ZoneRegion | str | Unset = UNSET,
        status: ZoneStatus | str | Unset = UNSET,
    ) -> Zone:
        body = CreateZoneRequest(
            name=name,
            type_=type_ if isinstance(type_, Unset) else ZoneType(type_),
            region=region if isinstance(region, Unset) else ZoneRegion(region),
            status=status if isinstance(status, Unset) else ZoneStatus(status),
        )
        response = await create_zone.asyncio_detailed(client=self._client, body=body)
        return expect(unwrap(response), ZoneResponse).data.zone

    def update(
        self,
        zone_id: str | UUID,
        *,
        name: str,
        type_: ZoneType | str | Unset = UNSET,
        region: ZoneRegion | str | Unset = UNSET,
        status: ZoneStatus | str | Unset = UNSET,
    ) -> Zone:
        body = UpdateZoneRequest(
            name=name,
            type_=type_ if isinstance(type_, Unset) else ZoneType(type_),
            region=region if isinstance(region, Unset) else ZoneRegion(region),
            status=status if isinstance(status, Unset) else ZoneStatus(status),
        )
        response = update_zone.sync_detailed(_uuid(zone_id), client=self._client, body=body)
        return expect(unwrap(response), ZoneResponse).data.zone

    async def aupdate(
        self,
        zone_id: str | UUID,
        *,
        name: str,
        type_: ZoneType | str | Unset = UNSET,
        region: ZoneRegion | str | Unset = UNSET,
        status: ZoneStatus | str | Unset = UNSET,
    ) -> Zone:
        body = UpdateZoneRequest(
            name=name,
            type_=type_ if isinstance(type_, Unset) else ZoneType(type_),
            region=region if isinstance(region, Unset) else ZoneRegion(region),
            status=status if isinstance(status, Unset) else ZoneStatus(status),
        )
        response = await update_zone.asyncio_detailed(
            _uuid(zone_id), client=self._client, body=body
        )
        return expect(unwrap(response), ZoneResponse).data.zone

    def delete(self, zone_id: str | UUID) -> None:
        response = delete_zone.sync_detailed(_uuid(zone_id), client=self._client)
        unwrap(response)

    async def adelete(self, zone_id: str | UUID) -> None:
        response = await delete_zone.asyncio_detailed(_uuid(zone_id), client=self._client)
        unwrap(response)
