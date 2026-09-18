from uuid import UUID

from dnscale_api.models.api_key_zone_scope import APIKeyZoneScope
from dnscale_api.models.api_key_zone_scope_record_access import APIKeyZoneScopeRecordAccess
from dnscale_api.models.create_api_key_request import CreateAPIKeyRequest


def test_dns_name_scope_serializes_in_create_request() -> None:
    zone_id = UUID("11111111-1111-4111-8111-111111111111")
    request = CreateAPIKeyRequest(
        name="ACME",
        scopes='["zones:read","records:write"]',
        zone_scopes=[
            APIKeyZoneScope(
                zone_id=zone_id,
                record_access=APIKeyZoneScopeRecordAccess.NAMES,
                record_names=["_acme-challenge", "_acme-challenge.api"],
            )
        ],
    )

    payload = request.to_dict()

    assert "zone_ids" not in payload
    assert payload["zone_scopes"] == [
        {
            "zone_id": str(zone_id),
            "record_access": "names",
            "record_names": ["_acme-challenge", "_acme-challenge.api"],
        }
    ]
