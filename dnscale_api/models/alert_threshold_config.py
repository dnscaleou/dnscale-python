from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertThresholdConfig")


@_attrs_define
class AlertThresholdConfig:
    """
    Attributes:
        qps_warning (int | Unset):
        qps_critical (int | Unset):
        nxdomain_ratio_warning (float | Unset):
        nxdomain_ratio_critical (float | Unset):
        servfail_ratio_warning (float | Unset):
        servfail_ratio_critical (float | Unset):
        query_drop_threshold (float | Unset):
        refused_qps_warning (int | Unset):
        refused_qps_critical (int | Unset):
    """

    qps_warning: int | Unset = UNSET
    qps_critical: int | Unset = UNSET
    nxdomain_ratio_warning: float | Unset = UNSET
    nxdomain_ratio_critical: float | Unset = UNSET
    servfail_ratio_warning: float | Unset = UNSET
    servfail_ratio_critical: float | Unset = UNSET
    query_drop_threshold: float | Unset = UNSET
    refused_qps_warning: int | Unset = UNSET
    refused_qps_critical: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        qps_warning = self.qps_warning

        qps_critical = self.qps_critical

        nxdomain_ratio_warning = self.nxdomain_ratio_warning

        nxdomain_ratio_critical = self.nxdomain_ratio_critical

        servfail_ratio_warning = self.servfail_ratio_warning

        servfail_ratio_critical = self.servfail_ratio_critical

        query_drop_threshold = self.query_drop_threshold

        refused_qps_warning = self.refused_qps_warning

        refused_qps_critical = self.refused_qps_critical

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if qps_warning is not UNSET:
            field_dict["qps_warning"] = qps_warning
        if qps_critical is not UNSET:
            field_dict["qps_critical"] = qps_critical
        if nxdomain_ratio_warning is not UNSET:
            field_dict["nxdomain_ratio_warning"] = nxdomain_ratio_warning
        if nxdomain_ratio_critical is not UNSET:
            field_dict["nxdomain_ratio_critical"] = nxdomain_ratio_critical
        if servfail_ratio_warning is not UNSET:
            field_dict["servfail_ratio_warning"] = servfail_ratio_warning
        if servfail_ratio_critical is not UNSET:
            field_dict["servfail_ratio_critical"] = servfail_ratio_critical
        if query_drop_threshold is not UNSET:
            field_dict["query_drop_threshold"] = query_drop_threshold
        if refused_qps_warning is not UNSET:
            field_dict["refused_qps_warning"] = refused_qps_warning
        if refused_qps_critical is not UNSET:
            field_dict["refused_qps_critical"] = refused_qps_critical

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        qps_warning = d.pop("qps_warning", UNSET)

        qps_critical = d.pop("qps_critical", UNSET)

        nxdomain_ratio_warning = d.pop("nxdomain_ratio_warning", UNSET)

        nxdomain_ratio_critical = d.pop("nxdomain_ratio_critical", UNSET)

        servfail_ratio_warning = d.pop("servfail_ratio_warning", UNSET)

        servfail_ratio_critical = d.pop("servfail_ratio_critical", UNSET)

        query_drop_threshold = d.pop("query_drop_threshold", UNSET)

        refused_qps_warning = d.pop("refused_qps_warning", UNSET)

        refused_qps_critical = d.pop("refused_qps_critical", UNSET)

        alert_threshold_config = cls(
            qps_warning=qps_warning,
            qps_critical=qps_critical,
            nxdomain_ratio_warning=nxdomain_ratio_warning,
            nxdomain_ratio_critical=nxdomain_ratio_critical,
            servfail_ratio_warning=servfail_ratio_warning,
            servfail_ratio_critical=servfail_ratio_critical,
            query_drop_threshold=query_drop_threshold,
            refused_qps_warning=refused_qps_warning,
            refused_qps_critical=refused_qps_critical,
        )

        return alert_threshold_config
