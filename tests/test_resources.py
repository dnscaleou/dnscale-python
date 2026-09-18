from __future__ import annotations

import asyncio
import json
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime

import httpx
import pytest

from dnscale import APIError, DNScale, ProtocolError, RateLimitError
from dnscale.transport import _retry_delay
from dnscale_api.models.update_record_by_name_request import UpdateRecordByNameRequest

ZONE_ID = "00000000-0000-4000-8000-000000000001"


def record(content: str = "first", identifier: str = "opaque/+id=") -> dict:
    return {
        "id": identifier,
        "name": "_acme-challenge.example.com.",
        "type": "TXT",
        "content": content,
        "ttl": 300,
        "disabled": False,
    }


def client(handler, **kwargs) -> DNScale:
    return DNScale(
        "test",
        transport=httpx.MockTransport(handler),
        async_transport=httpx.MockTransport(handler),
        **kwargs,
    )


def test_retry_after_above_budget_is_surfaced_without_retry() -> None:
    attempts = []

    def handler(request):
        attempts.append(request)
        return httpx.Response(
            429,
            headers={"Retry-After": "120"},
            json={"status": "error", "error": {"code": "RATE_LIMITED", "message": "wait"}},
        )

    with client(handler) as dns, pytest.raises(RateLimitError) as error:
        dns.zones.list()
    assert len(attempts) == 1
    assert error.value.retry_after == "120"

    async def exercise():
        async with client(handler) as dns:
            with pytest.raises(RateLimitError):
                await dns.zones.alist()

    asyncio.run(exercise())
    assert len(attempts) == 2


def test_retry_after_http_date_is_not_shortened() -> None:
    future = datetime.now(timezone.utc) + timedelta(seconds=120)
    response = httpx.Response(429, headers={"Retry-After": format_datetime(future)})
    assert 118 <= _retry_delay(response, 1, 0.25) <= 120


@pytest.mark.parametrize("value", ["invalid", "nan", "inf"])
def test_invalid_retry_after_uses_backoff(value) -> None:
    assert _retry_delay(httpx.Response(503, headers={"Retry-After": value}), 1, 0.25) == 0.25


def test_html_error_keeps_status_and_request_id() -> None:
    with (
        client(
            lambda _: httpx.Response(
                502, text="<html>proxy failure</html>", headers={"X-Request-ID": "proxy-1"}
            ),
            max_retries=0,
        ) as dns,
        pytest.raises(APIError) as error,
    ):
        dns.zones.list()
    assert error.value.status_code == 502
    assert error.value.request_id == "proxy-1"


def test_record_iterators_follow_actual_page_counts() -> None:
    offsets = []

    def handler(request):
        offset = int(request.url.params["offset"])
        offsets.append(offset)
        return httpx.Response(
            200,
            json={
                "status": "success",
                "data": {
                    "records": [record(str(offset))],
                    "pagination": {
                        "offset": offset,
                        "limit": 1,
                        "count": 1,
                        "total": 2,
                        "has_more": offset == 0,
                    },
                },
            },
        )

    with client(handler) as dns:
        assert [r.content for r in dns.records.iter(ZONE_ID)] == ["0", "1"]

    async def exercise():
        async with client(handler) as dns:
            return [r.content async for r in dns.records.aiter(ZONE_ID)]

    assert asyncio.run(exercise()) == ["0", "1"]
    assert offsets == [0, 1, 0, 1]


def test_iterator_rejects_no_progress() -> None:
    response = {
        "status": "success",
        "data": {
            "zones": [],
            "pagination": {"offset": 0, "limit": 100, "count": 0, "total": 1, "has_more": True},
        },
    }
    with client(lambda _: httpx.Response(200, json=response)) as dns:
        with pytest.raises(ProtocolError, match="empty page"):
            list(dns.zones.iter())
        with pytest.raises(ValueError, match="page_size"):
            list(dns.zones.iter(page_size=0))


def test_record_lifecycle_serialization_and_content_scoped_delete() -> None:
    requests = []

    def handler(request):
        requests.append(request)
        if request.method == "DELETE":
            assert request.url.params["content"] == "new + / & value"
            return httpx.Response(204)
        body = json.loads(request.content)
        if request.method == "PUT":
            assert request.url.params["content"] == "first"
        return httpx.Response(
            201 if request.method == "POST" else 200,
            json={"status": "success", "data": {"record": record(body["content"])}},
        )

    with client(handler) as dns:
        created = dns.records.create(
            ZONE_ID, name="_acme-challenge", type_="TXT", content="first", ttl=300, comment=None
        )
        assert created.content == "first"
        updated = dns.records.update_by_name(
            ZONE_ID,
            created.name,
            "TXT",
            content=created.content,
            body=UpdateRecordByNameRequest(content="new + / & value", ttl=300),
        )
        dns.records.delete_by_name(ZONE_ID, updated.name, "TXT", content=updated.content)
        with pytest.raises(ValueError):
            dns.records.delete_by_name(ZONE_ID, updated.name, "TXT", content="")
    assert len(requests) == 3
    assert json.loads(requests[0].content)["comment"] is None


@pytest.mark.parametrize("method", ["POST", "PUT", "PATCH", "DELETE"])
def test_no_mutation_is_retried(method) -> None:
    attempts = []

    def handler(request):
        attempts.append(request)
        return httpx.Response(
            503,
            json={"status": "error", "error": {"code": "UNAVAILABLE", "message": "unavailable"}},
        )

    with client(handler) as dns:
        assert dns.client.get_httpx_client().request(method, "/zones").status_code == 503
    assert len(attempts) == 1


def test_async_record_helpers_preserve_selectors_and_returned_ids() -> None:
    methods = []

    def handler(request):
        methods.append(request.method)
        if request.method == "DELETE":
            assert request.url.params["content"] == "second"
            return httpx.Response(204)
        if request.method == "PUT":
            assert request.url.params["content"] == "first"
        content = json.loads(request.content)["content"]
        return httpx.Response(
            201 if request.method == "POST" else 200,
            json={"status": "success", "data": {"record": record(content, content)}},
        )

    async def exercise():
        async with client(handler) as dns:
            created = await dns.records.acreate(ZONE_ID, name="www", type_="TXT", content="first")
            updated = await dns.records.aupdate_by_name(
                ZONE_ID,
                created.name,
                "TXT",
                content=created.content,
                body=UpdateRecordByNameRequest(content="second"),
            )
            assert updated.id != created.id
            await dns.records.adelete_by_name(ZONE_ID, updated.name, "TXT", content=updated.content)

    asyncio.run(exercise())
    assert methods == ["POST", "PUT", "DELETE"]
