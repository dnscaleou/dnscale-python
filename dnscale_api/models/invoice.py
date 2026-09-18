from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Invoice")


@_attrs_define
class Invoice:
    """
    Attributes:
        id (UUID):
        customer_id (UUID):
        stripe_invoice_id (str):
        amount_paid (int): Minor currency units (for example, euro cents).
        amount_due (int): Minor currency units (for example, euro cents).
        currency (str):
        status (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        subscription_id (None | Unset | UUID):
        invoice_url (None | str | Unset):
        invoice_pdf (None | str | Unset):
        period_start (datetime.datetime | None | Unset):
        period_end (datetime.datetime | None | Unset):
        description (None | str | Unset):
        billing_reason (None | str | Unset):
    """

    id: UUID
    customer_id: UUID
    stripe_invoice_id: str
    amount_paid: int
    amount_due: int
    currency: str
    status: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    subscription_id: None | Unset | UUID = UNSET
    invoice_url: None | str | Unset = UNSET
    invoice_pdf: None | str | Unset = UNSET
    period_start: datetime.datetime | None | Unset = UNSET
    period_end: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    billing_reason: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        customer_id = str(self.customer_id)

        stripe_invoice_id = self.stripe_invoice_id

        amount_paid = self.amount_paid

        amount_due = self.amount_due

        currency = self.currency

        status = self.status

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        subscription_id: None | str | Unset
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        elif isinstance(self.subscription_id, UUID):
            subscription_id = str(self.subscription_id)
        else:
            subscription_id = self.subscription_id

        invoice_url: None | str | Unset
        if isinstance(self.invoice_url, Unset):
            invoice_url = UNSET
        else:
            invoice_url = self.invoice_url

        invoice_pdf: None | str | Unset
        if isinstance(self.invoice_pdf, Unset):
            invoice_pdf = UNSET
        else:
            invoice_pdf = self.invoice_pdf

        period_start: None | str | Unset
        if isinstance(self.period_start, Unset):
            period_start = UNSET
        elif isinstance(self.period_start, datetime.datetime):
            period_start = self.period_start.isoformat()
        else:
            period_start = self.period_start

        period_end: None | str | Unset
        if isinstance(self.period_end, Unset):
            period_end = UNSET
        elif isinstance(self.period_end, datetime.datetime):
            period_end = self.period_end.isoformat()
        else:
            period_end = self.period_end

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        billing_reason: None | str | Unset
        if isinstance(self.billing_reason, Unset):
            billing_reason = UNSET
        else:
            billing_reason = self.billing_reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "customer_id": customer_id,
                "stripe_invoice_id": stripe_invoice_id,
                "amount_paid": amount_paid,
                "amount_due": amount_due,
                "currency": currency,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if invoice_url is not UNSET:
            field_dict["invoice_url"] = invoice_url
        if invoice_pdf is not UNSET:
            field_dict["invoice_pdf"] = invoice_pdf
        if period_start is not UNSET:
            field_dict["period_start"] = period_start
        if period_end is not UNSET:
            field_dict["period_end"] = period_end
        if description is not UNSET:
            field_dict["description"] = description
        if billing_reason is not UNSET:
            field_dict["billing_reason"] = billing_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        customer_id = UUID(d.pop("customer_id"))

        stripe_invoice_id = d.pop("stripe_invoice_id")

        amount_paid = d.pop("amount_paid")

        amount_due = d.pop("amount_due")

        currency = d.pop("currency")

        status = d.pop("status")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_subscription_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_id_type_0 = UUID(data)

                return subscription_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subscription_id = _parse_subscription_id(d.pop("subscription_id", UNSET))

        def _parse_invoice_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invoice_url = _parse_invoice_url(d.pop("invoice_url", UNSET))

        def _parse_invoice_pdf(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invoice_pdf = _parse_invoice_pdf(d.pop("invoice_pdf", UNSET))

        def _parse_period_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_start_type_0 = isoparse(data)

                return period_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        period_start = _parse_period_start(d.pop("period_start", UNSET))

        def _parse_period_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_end_type_0 = isoparse(data)

                return period_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        period_end = _parse_period_end(d.pop("period_end", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_billing_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_reason = _parse_billing_reason(d.pop("billing_reason", UNSET))

        invoice = cls(
            id=id,
            customer_id=customer_id,
            stripe_invoice_id=stripe_invoice_id,
            amount_paid=amount_paid,
            amount_due=amount_due,
            currency=currency,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            subscription_id=subscription_id,
            invoice_url=invoice_url,
            invoice_pdf=invoice_pdf,
            period_start=period_start,
            period_end=period_end,
            description=description,
            billing_reason=billing_reason,
        )

        return invoice
