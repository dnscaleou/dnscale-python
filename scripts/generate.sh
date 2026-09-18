#!/usr/bin/env bash
set -euo pipefail
sdk_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
uvx --from openapi-python-client==0.28.4 --with ruff==0.12.12 \
  openapi-python-client generate --path "${sdk_root}/openapi.yaml" \
  --config "${sdk_root}/generator.yaml" --meta none \
  --output-path "${sdk_root}/dnscale_api" --overwrite --fail-on-warning
touch "${sdk_root}/dnscale_api/py.typed"
