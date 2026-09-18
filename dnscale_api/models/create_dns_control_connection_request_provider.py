from enum import Enum


class CreateDNSControlConnectionRequestProvider(str, Enum):
    CLOUDFLARE = "cloudflare"
    ROUTE53 = "route53"

    def __str__(self) -> str:
        return str(self.value)
