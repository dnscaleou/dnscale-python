"""Opt-in lifecycle test; creates and removes a uniquely named disposable zone."""

import os
from uuid import uuid4

import pytest

from dnscale import DNScale


@pytest.mark.skipif(os.getenv("DNSCALE_LIVE_TEST") != "1", reason="live API test is opt-in")
def test_live_zone_record_lifecycle() -> None:
    base_url = os.environ["DNSCALE_TEST_BASE_URL"]
    key = os.environ["DNSCALE_TEST_API_KEY"]
    with DNScale(key, base_url=base_url, max_retries=0) as dns:
        zone = dns.zones.create(f"sdk-{uuid4().hex}.example.com", type_="master", region="EU")
        try:
            assert dns.zones.get(zone.id).id == zone.id
            created = dns.records.create(zone.id, name="sdk", type_="TXT", content="first")
            assert any(r.id == created.id for r in dns.records.iter(zone.id, page_size=1))
            updated = dns.records.update(
                zone.id, created.id, name=created.name, type_="TXT", content="second"
            )
            assert dns.records.get(zone.id, updated.id).content == "second"
            dns.records.delete(zone.id, updated.id)
            assert not any(r.id == updated.id for r in dns.records.iter(zone.id))
        finally:
            dns.zones.delete(zone.id)
