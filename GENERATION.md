# Generated client policy

`dnscale_api/` is generated from `docs/openapi.yaml`; do not edit it manually.
`dnscale/` is the stable, handwritten layer and is preserved during regeneration.

From the repository root:

```bash
cd docs && npm run validate
cd .. && ./scripts/generate-python-sdk.sh
```

The script pins `openapi-python-client` so regeneration is deterministic. Review
the generated diff whenever the OpenAPI contract changes, then run the SDK tests
and build before committing both changes together.

Generator formatting ignores Git ignore rules within the generated output so
the same model files are formatted in standalone and monorepo checkouts. The
generated `provider_credentials.py` contains schema definitions, not secrets,
and must remain tracked despite the monorepo's broad credentials ignore rule.

In a standalone SDK checkout, run `bash scripts/generate.sh`. Its inputs are the
bundled `openapi.yaml` and `generator.yaml`. The monorepo script synchronizes
these copies before invoking the same generator. Do not edit the copies to
change API behaviour; update the authoritative contract first.
