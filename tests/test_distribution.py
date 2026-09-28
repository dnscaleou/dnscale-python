"""Checks for the public distribution name and installed package contents."""

from importlib.metadata import metadata
from pathlib import Path

import dnscale
import dnscale_api


def test_distribution_metadata() -> None:
    package = metadata("dnscale")
    assert package["Name"] == "dnscale"
    assert package["Version"] == dnscale.__version__
    assert "Repository, https://github.com/dnscaleou/dnscale-python" in package.get_all(
        "Project-URL", []
    )


def test_both_import_packages_include_type_markers() -> None:
    for package in (dnscale, dnscale_api):
        assert package.__file__ is not None
        assert Path(package.__file__).with_name("py.typed").is_file()
