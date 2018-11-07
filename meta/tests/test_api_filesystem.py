# meta.tests.test_api_filesystem.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Test set to ensure the interactions for filesystem commands work as intended."""

# pylint:disable=redefined-outer-name
# pylint:disable=unused-import
# pylint:disable=unused-argument

import os

import pytest
from pytest_mock import mocker

import meta.shell
from meta.api import filesystem

# --------------------------------------
#   Fixtures
# --------------------------------------


@pytest.fixture
def abspath_mock(mocker):
    """Mock for the absolute path converter."""
    path_mock = mocker.patch("os.path.abspath", autospec=True)

    def should_return(actual_abs_path):
        path_mock.return_value = actual_abs_path

    return should_return


# --------------------------------------
#   Tests
# --------------------------------------


# NOTE: most tests assuming the actual file "myfile.txt" is located at "/path/to/"
@pytest.mark.parametrize(
    "given_path, actual_path",
    [
        ("./myfile.txt", "/path/to/myfile.txt"),
        ("/myfile.txt", "/myfile.txt"),
        ("/path/to/myfile.txt", "/path/to/myfile.txt"),
        ("subpath/to/myfile.txt", "/path/to/subpath/to/myfile.txt"),
        ("./subpath/to/myfile.txt", "/path/to/subpath/to/myfile.txt"),
        ("myfile.txt", "/path/to/myfile.txt"),
    ],
)
def test_file_path_initialization(abspath_mock, given_path, actual_path):
    """Ensure that file path and name are correctly assigned based on the given path."""
    abspath_mock(actual_path)
    test_file = filesystem.File(given_path)
    assert test_file.path == actual_path
    assert test_file.name == "myfile.txt"


# NOTE: most tests assuming the actual folder "myfolder" is located at "/path/to/"
@pytest.mark.parametrize(
    "given_path, actual_path",
    [
        ("./myfolder", "/path/to/myfolder"),
        ("./myfolder/", "/path/to/myfolder"),
        ("/myfolder", "/path/to/myfolder"),
        ("/myfolder/", "/path/to/myfolder"),
        ("/path/to/myfolder", "/path/to/myfolder"),
        ("/path/to/myfolder/", "/path/to/myfolder"),
        ("subpath/to/myfolder", "/path/to/subpath/to/myfolder"),
        ("subpath/to/myfolder/", "/path/to/subpath/to/myfolder"),
        ("myfolder", "/path/to/myfolder"),
        ("myfolder/", "/path/to/myfolder"),
    ],
)
def test_folder_path_initialization(abspath_mock, given_path, actual_path):
    """Ensure that the folder path and name are correctly assigned."""
    abspath_mock(actual_path)
    test_folder = filesystem.Folder(given_path)
    assert test_folder.path == actual_path
    assert test_folder.name == "myfolder"
