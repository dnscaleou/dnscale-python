from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.invoices_response_status import InvoicesResponseStatus

if TYPE_CHECKING:
    from ..models.invoices_data import InvoicesData


T = TypeVar("T", bound="InvoicesResponse")


@_attrs_define
class InvoicesResponse:
    """
    Attributes:
        status (InvoicesResponseStatus):
        data (InvoicesData):
    """

    status: InvoicesResponseStatus
    data: InvoicesData

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoices_data import InvoicesData

        d = dict(src_dict)
        status = InvoicesResponseStatus(d.pop("status"))

        data = InvoicesData.from_dict(d.pop("data"))

        invoices_response = cls(
            status=status,
            data=data,
        )

        return invoices_response
