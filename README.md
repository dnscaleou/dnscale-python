# DNScale Python SDK

The official Python client for the DNScale API. It supports Python 3.10 and newer,
provides synchronous and asynchronous calls, and is generated from the public
OpenAPI contract in `docs/openapi.yaml`.

The package is not published to PyPI yet. Install it from this repository while
the `0.1.x` API is being stabilized:

```bash
pip install ./sdks/python
```

After the first release, the distribution name will be `dnscale-sdk`:

```bash
pip install dnscale-sdk
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

Do not edit `dnscale_api` by hand. Regenerate it from the repository root after
changing the OpenAPI contract:

```bash
cd docs && npm run validate
cd .. && ./scripts/generate-python-sdk.sh
```

The generator version is pinned in the script. To verify the package:

```bash
python -m pytest sdks/python/tests
ruff check sdks/python/dnscale sdks/python/tests
ruff format --check sdks/python/dnscale sdks/python/tests
uv build --directory sdks/python
```
