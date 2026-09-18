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
