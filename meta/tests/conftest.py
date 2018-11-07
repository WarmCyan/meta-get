# meta.tests.common_fixtures.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Set of fixtures that multiple test files use."""

# pylint:disable=redefined-outer-name
# pylint:disable=unused-import
# pylint:disable=unused-argument

import pytest
from pytest_mock import mocker


@pytest.fixture
def shell_mock(mocker):
    """Basic mock for the backend shell execution function.

    Note that this mock should not be used if return value is needed."""
    execution_mock = mocker.patch("meta.shell.execute", autospec=True)
    execution_mock.return_value = "hello world"
    return execution_mock
