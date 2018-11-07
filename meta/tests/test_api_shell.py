# meta.tests.test_api_shell.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Test set to ensure the shell API is working as intended."""

# pylint:disable=redefined-outer-name
# pylint:disable=unused-import
# pylint:disable=unused-argument

import pytest
from pytest_mock import mocker

import meta.api.shell
import meta.shell


def test_default_command_execution(shell_mock):
    """Ensure that a command gets passed correctly to the underlying shell function."""
    meta.api.shell.execute("echo 'hello world'")
    shell_mock.assert_called_with("echo 'hello world'", silent=False)


def test_silent_command_execution(shell_mock):
    """Ensure that the api, if called silently, calls the backend shell silently."""
    meta.api.shell.execute("echo 'hello world'", silent=True)
    shell_mock.assert_called_with("echo 'hello world'", silent=True)


def test_command_execution_return(shell_mock):
    """Ensure that the shell output gets returned correctly."""
    assert meta.api.shell.execute("echo 'hello world'") == "hello world"
