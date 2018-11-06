# meta.tests.test_api_filesystem.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Test set to ensure the interactions for filesystem commands work as intended."""

# pylint:disable=redefined-outer-name
# pylint:disable=unused-import
# pylint:disable=unused-argument

import pytest
from pytest_mock import mocker

import meta.shell
from meta.api import filesystem

# --------------------------------------
#   Fixtures
# --------------------------------------


@pytest.fixture
def shell_mock(mocker):
    """Mock for the backend shell execution function."""
    execution_mock = mocker.patch("meta.shell.execute", autospec=True)
    execution_mock.return_value = "hello world"
    return execution_mock


# --------------------------------------
#   Tests
# --------------------------------------


def test_default_command_execution(shell_mock):
    """Ensure that a command gets passed correctly to the underlying shell function."""
    meta.api.shell.execute("echo 'hello world'")
    shell_mock.assert_called_with("echo 'hello world'", silent=False)


@pytest.mark.parametrize(
    "given_path, expected_name, expected_path",
    [
        ("./myfile", "myfile", "./myfile"),
        ("/myfile", "myfile", "/myfile"),
        ("/path/to/myfile", "myfile", "/path/to/myfile"),
        ("path/to/myfile", "myfile", "./path/to/myfile"),
        ("myfile", "myfile", "./myfile"),
        ("myfile.txt", "myfile.txt.", "./myfile.txt"),
    ],
)
def test_file_path_initialization(given_path, expected_name, expected_path):
    """Ensure that file path and name are correctly assigned based on the given path."""
    test_file = filesystem.File(given_path)
    assert test_file.path == expected_path
    assert test_file.name == expected_name


@pytest.mark.parametrize(
    "given_path, expected_name, expected_path",
    [
        ("./myfolder", "myfolder", "./myfolder"),
        ("./myfolder/", "myfolder", "./myfolder"),
        ("/myfolder", "myfolder", "/myfolder"),
        ("/myfolder/", "myfolder", "/myfolder"),
        ("/path/to/myfolder", "myfolder", "/path/to/myfolder"),
        ("/path/to/myfolder/", "myfolder", "/path/to/myfolder"),
        ("path/to/myfolder", "myfolder", "./path/to/myfolder"),
        ("path/to/myfolder/", "myfolder", "./path/to/myfolder"),
        ("myfolder", "myfolder", "./myfolder"),
        ("myfolder/", "myfolder", "./myfolder"),
    ],
)
def test_folder_path_initialization(given_path, expected_name, expected_path):
    """Ensure that the folder path and name are correctly assigned."""
    test_folder = filesystem.Folder(given_path)
    assert test_folder.path == expected_path
    assert test_folder.name == expected_name
