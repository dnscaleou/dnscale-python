from enum import Enum


class DNSControlProviderAuthType(str, Enum):
    ACCESS_KEYS = "access_keys"
    API_KEY = "api_key"
    API_TOKEN = "api_token"
    OAUTH = "oauth"

    def __str__(self) -> str:
        return str(self.value)
