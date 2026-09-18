from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.invoice import Invoice


T = TypeVar("T", bound="InvoicesData")


@_attrs_define
class InvoicesData:
    """
    Attributes:
        invoices (list[Invoice]):
        total (int):
    """

    invoices: list[Invoice]
    total: int

    def to_dict(self) -> dict[str, Any]:
        invoices = []
        for invoices_item_data in self.invoices:
            invoices_item = invoices_item_data.to_dict()
            invoices.append(invoices_item)

        total = self.total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "invoices": invoices,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice import Invoice

        d = dict(src_dict)
        invoices = []
        _invoices = d.pop("invoices")
        for invoices_item_data in _invoices:
            invoices_item = Invoice.from_dict(invoices_item_data)

            invoices.append(invoices_item)

        total = d.pop("total")

        invoices_data = cls(
            invoices=invoices,
            total=total,
        )

        return invoices_data
