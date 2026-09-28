# Generated client policy

`dnscale_api/` is generated from the bundled `openapi.yaml`; do not edit it manually.
`dnscale/` is the stable, handwritten layer and is preserved during regeneration.

From the repository root:

```bash
bash scripts/generate.sh
```

The script pins `openapi-python-client` so regeneration is deterministic. Review
the generated diff whenever the OpenAPI contract changes, then run the SDK tests
and build before committing both changes together.

Generator formatting ignores Git ignore rules within the generated output so
the same model files are formatted in standalone and monorepo checkouts. The
generated `provider_credentials.py` contains schema definitions, not secrets,
and must remain tracked despite the monorepo's broad credentials ignore rule.

Its inputs are the bundled `openapi.yaml` and `generator.yaml`. These are
maintainer-synchronized copies of the authoritative API contract and generator
configuration. Do not edit the copies to change API behaviour; propose API
changes to the maintainers first, then regenerate from the approved contract.
