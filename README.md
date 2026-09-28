# DNScale Python SDK

The official Python client for the DNScale API. It supports Python 3.10 and newer,
provides synchronous and asynchronous calls, and is generated from the public
OpenAPI contract bundled as [openapi.yaml](openapi.yaml).

## Installation

Install a published release from PyPI:

```bash
python -m pip install dnscale
```

The distribution and import name are both `dnscale`; the source repository is
`dnscale-python`. Before the first PyPI release, or to work from source, clone
this repository and install from its root:

```bash
python -m pip install .
```

## Quick start

Create an API key in the DNScale dashboard and pass it directly or export it as
`DNSCALE_API_KEY`.

```python
from dnscale import DNScale

with DNScale() as dns:
    zones = dns.zones.list(limit=25)
    for zone in zones.zones:
        print(zone.id, zone.name)

    created = dns.records.create(
        zones.zones[0].id,
        name="www",
        type_="A",
        content="192.0.2.10",
        ttl=300,
    )
    print(created.id)
```

The same resources provide async methods prefixed with `a`:

```python
from dnscale import DNScale


async def list_zone_names() -> list[str]:
    async with DNScale() as dns:
        result = await dns.zones.alist(limit=100)
        return [zone.name for zone in result.zones]
```

`DNScale` retries transient failures for `GET`, `HEAD`, and `OPTIONS` requests.
It never automatically retries mutations such as record or zone creation. Set
`max_retries=0` to disable retries.
If `Retry-After` exceeds the 30-second retry waiting budget, the response is
surfaced immediately instead of retrying before the server permits it. HTTP-date
and numeric delay values are supported. Network errors remain `httpx` errors.

## Pagination and record identity

`list()` returns one page. Use lazy iterators to traverse all pages:

```python
with DNScale() as dns:
    for zone in dns.zones.iter():
        for record in dns.records.iter(zone.id):
            print(zone.name, record.name, record.content)
```

Async equivalents are `zones.aiter()` and `records.aiter(zone_id)`. Iterators
honour the returned page size and reject inconsistent pagination. Offset-based
listing is not an atomic snapshot if another client changes the zone concurrently.

Record IDs are opaque and content-derived: use the **returned ID after an
update**. By-name helpers can avoid retaining an ID:

```python
from dnscale_api.models import UpdateRecordByNameRequest

with DNScale() as dns:
    updated = dns.records.update_by_name(
        zone_id, "_acme-challenge.example.com.", "TXT",
        content="old-value",  # select this value in a multi-value RRset
        body=UpdateRecordByNameRequest(content="new-value", ttl=300),
    )
    dns.records.delete_by_name(zone_id, updated.name, "TXT", content="new-value")
```

Omitting `content` from `delete_by_name()` deletes the **entire RRset**. Empty
content is rejected by the helper to prevent accidental whole-RRset deletion.
Async variants are `aupdate_by_name()` and `adelete_by_name()`.

## Errors

The convenience resources convert the API's error envelope into exceptions:

```python
from dnscale import APIError, DNScale, RateLimitError

try:
    with DNScale() as dns:
        dns.zones.get("00000000-0000-0000-0000-000000000000")
except RateLimitError as error:
    print(error.retry_after)
except APIError as error:
    print(error.status_code, error.code, error.message, error.request_id)
```

Network and timeout failures remain standard `httpx` exceptions.

## Complete generated API

The `dnscale` layer offers concise zone and record CRUD. Every public endpoint is
also available through the generated `dnscale_api` package, including alerts,
DNSSEC, usage, billing, users, invitations, API keys, activity, and DNS Control.

```python
from dnscale import DNScale
from dnscale_api.api.usage import get_current_usage

with DNScale(api_key="your-api-key") as dns:
    response = get_current_usage.sync(client=dns.client)
    print(response)
```

Each generated operation has `sync`, `sync_detailed`, `asyncio`, and
`asyncio_detailed` variants. Request and response models live in
`dnscale_api.models`.

## Development

From this repository's root, install development dependencies and regenerate
the client. Python 3.10+ and [uv](https://docs.astral.sh/uv/) are required.
Do not edit `dnscale_api` by hand.

```bash
python -m pip install -e '.[dev]'
bash scripts/generate.sh
```

The generator version is pinned in the script. To verify the package:

```bash
python -m pytest
ruff check dnscale tests
ruff format --check dnscale tests
uv build
```

The generator is pinned; see [GENERATION.md](GENERATION.md) for the contract
update policy. Commit the reviewed generated changes with their input changes.

Live verification is explicitly opt-in and creates/deletes a unique test zone:

```bash
export DNSCALE_TEST_BASE_URL=https://your-sandbox.example/v1
export DNSCALE_TEST_API_KEY=your-disposable-account-key
DNSCALE_LIVE_TEST=1 python -m pytest tests/test_live.py
```

The test uses separate credentials from `DNSCALE_API_KEY`. Use a disposable
account with zone and record read/write scopes. No real domain delegation is
needed. Tests are skipped when `DNSCALE_LIVE_TEST` is not `1`.

Report bugs and feature requests in the
[issue tracker](https://github.com/dnscaleou/dnscale-python/issues).
