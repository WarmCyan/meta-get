# meta.tests.test_autotracker.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Test set to ensure the internal autotracker functionality functions correctly."""

# pylint:disable=redefined-outer-name
# pylint:disable=unused-import

import pytest

import meta.autotracker

# --------------------------------------
#   Fixtures
# --------------------------------------


@pytest.fixture
def sample_autotracker():
    """Simple autotracker containing some files, packages, and dependencies."""
    tracker = meta.autotracker.Autotracker()
    tracker.files = ["~/thing.txt", "~/thing2.txt"]
    tracker.dependencies = ["that-other-package"]
    tracker.packages = [
        {"name": "pytest", "pkg_manager": "pip", "version": "", "user_install": True}
    ]
    return tracker


# --------------------------------------
#   Tests
# --------------------------------------


def test_contained_file_exists(sample_autotracker):
    """Ensure that the autotracker correctly reports that it is tracking a file."""
    assert sample_autotracker.check_file("~/thing.txt")


def test_noncontained_file_exists(sample_autotracker):
    """Ensure that the autotracker correctly reports that it is not tracking a file."""
    assert not sample_autotracker.check_file("~/otherthing.txt")


def test_contained_dependency_exists(sample_autotracker):
    """Ensure that the autotracker correctly reports that it is tracking a dependency."""
    assert sample_autotracker.check_dependency("that-other-package")


def test_noncontained_dependency_exists(sample_autotracker):
    """Ensure that the autotracker correctly reports that it is not tracking a dependency."""
    assert not sample_autotracker.check_dependency("that-other-other-package")


def test_contained_package_exists(sample_autotracker):
    """Ensure that the autotracker correctly reports that it is tracking a package."""
    assert sample_autotracker.check_package("pip", "pytest")


def test_noncontained_package_exists(sample_autotracker):
    """Ensure that the autotracker correctly reports that it is not tracking a package."""
    assert not sample_autotracker.check_package("pip", "numpy")


def test_contained_package_alt_pkgmanger_exists(sample_autotracker):
    """Ensure that similarly named packages of different package managers are treated separately"""
    assert not sample_autotracker.check_package("pacman", "pytest")


def test_filename_change(sample_autotracker):
    """Ensure that filename change requests are appropriately handled."""
    sample_autotracker.change_filepath("~/thing.txt", "~/thing3.txt")
    assert not sample_autotracker.check_file("~/thing.txt")
    assert sample_autotracker.check_file("~/thing3.txt")
