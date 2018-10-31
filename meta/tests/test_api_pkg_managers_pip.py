# meta.tests.test_api_pkg_managers_pip.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Test set to ensure the PIP API is working as intended."""

# pylint:disable=redefined-outer-name
# pylint:disable=unused-argument

import pytest

import meta.api.pkg_managers.pip

# --------------------------------------
#   Fixtures
# --------------------------------------


@pytest.fixture
def shell_mock(mocker):
    """Mock for the backend shell execution function."""
    execution_mock = mocker.patch("meta.shell.execute", autospec=True)
    execution_mock.return_value = "executed"
    return execution_mock


# --------------------------------------
#   Tests
# --------------------------------------


def test_default_command_execution(shell_mock):
    """Ensure that a command gets passed correctly to the underlying shell function."""
    meta.api.pkg_managers.pip.__execute("freeze")
    shell_mock.assert_called_with("pip freeze", silent=False)


def test_silent_command_execution(shell_mock):
    """Ensure that the api, if called silently, calls the backend shell silently."""
    meta.api.pkg_managers.pip.__execute("freeze", silent=True)
    shell_mock.assert_called_with("pip freeze", silent=True)


def test_command_execution_return(shell_mock):
    """Ensure that the shell output gets returned correctly."""
    assert meta.api.pkg_managers.pip.__execute("freeze") == "executed"


def test_install_command(shell_mock):
    """Ensure that the install command gets passed correctly to the underlying shell function."""
    meta.api.pkg_managers.pip.install("numpy")
    shell_mock.assert_called_with("pip install numpy", silent=False)


def test_silent_install(shell_mock):
    """Ensure that the install command, if called silently gets passed correctly to the underlying shell function."""
    meta.api.pkg_managers.pip.install("numpy", silent=True)
    shell_mock.assert_called_with("pip install numpy", silent=True)