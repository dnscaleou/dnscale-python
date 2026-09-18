from enum import Enum


class RecordType(str, Enum):
    A = "A"
    AAAA = "AAAA"
    ALIAS = "ALIAS"
    CAA = "CAA"
    CNAME = "CNAME"
    HTTPS = "HTTPS"
    MX = "MX"
    NAPTR = "NAPTR"
    NS = "NS"
    PTR = "PTR"
    SOA = "SOA"
    SRV = "SRV"
    SVCB = "SVCB"
    TLSA = "TLSA"
    TXT = "TXT"

    def __str__(self) -> str:
        return str(self.value)
