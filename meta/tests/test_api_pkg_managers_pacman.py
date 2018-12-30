# meta.tests.test_api_pkg_managers_pacman.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Test set to ensure the Pacman API is working as intended."""

# pylint:disable=redefined-outer-name
# pylint:disable=unused-argument

import meta.api.pkg_managers.pacman
import meta.current


def test_install_single(shell_mock, common_autotracker):
    """Ensure the correct command is used for installing a single package."""
    meta.api.pkg_managers.pacman.install("testpackage")
    shell_mock.assert_called_with("sudo pacman -S testpackage", silent=False)
    assert meta.current.PACKAGE_AUTOTRACKER.check_package("pacman", "testpackage")

def test_install_multiple(shell_mock, common_autotracker):
    """Ensure the correct command is used for installing a package list."""
    meta.api.pkg_managers.pacman.install("testpackage1", "testpackage2")
    shell_mock.assert_called_with("sudo pacman -S testpackage1 testpackage2", silent=False)
    assert meta.current.PACKAGE_AUTOTRACKER.check_package("pacman", "testpackage1")
    assert meta.current.PACKAGE_AUTOTRACKER.check_package("pacman", "testpackage2")


def test_remove(shell_mock):
    """Ensure the correct command is used for removing a single package."""
    meta.api.pkg_managers.pacman.uninstall("testpackage")
    shell_mock.assert_called_with("sudo pacman -R testpackage", silent=False)
