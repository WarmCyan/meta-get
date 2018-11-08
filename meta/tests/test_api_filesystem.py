# meta.tests.test_api_filesystem.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Test set to ensure the interactions for filesystem commands work as intended."""

# pylint:disable=redefined-outer-name
# pylint:disable=unused-import
# pylint:disable=unused-argument

import os

import meta.shell
import pytest
from meta.api import filesystem
from pytest_mock import mocker

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


@pytest.fixture
def basic_file(abspath_mock):
    """A simple file example."""
    abspath_mock("/path/to/myfile.txt")
    return filesystem.File("/path/to/myfile.txt")


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


def test_file_deletion(basic_file, shell_mock):
    """Ensure that deleting a file calls the correct shell command."""
    basic_file.delete()
    shell_mock.assert_called_with("rm " + "/path/to/myfile.txt")


COPY_FILE_TEST_PARAMS = [
    ("../", "/path/myfile.txt", "myfile.txt"),
    ("newfile.txt", "/path/to/newfile.txt", "newfile.txt"),
    ("./newfile.txt", "/path/to/newfile.txt", "newfile.txt"),
    ("../newfile.txt", "/path/newfile.txt", "newfile.txt"),
    ("subpath/to/myfile.txt", "/path/to/subpath/to/myfile.txt", "myfile.txt"),
    ("./subpath/to/myfile.txt", "/path/to/subpath/to/myfile.txt", "myfile.txt"),
    ("subpath/to/", "/path/to/subpath/to/myfile.txt", "myfile.txt"),
]


@pytest.mark.parametrize(
    "passed_dest, expected_dest_path, expected_dest_name", COPY_FILE_TEST_PARAMS
)
def test_file_copy(
    basic_file, shell_mock, passed_dest, expected_dest_path, expected_dest_name
):
    """Ensure that copying a file calls the correct shell command."""
    basic_file.copy(passed_dest)
    shell_mock.assert_called_with("cp /path/to/myfile.txt " + expected_dest_path)


@pytest.mark.parametrize(
    "passed_dest, expected_dest_path, expected_dest_name", COPY_FILE_TEST_PARAMS
)
def test_file_copy_return(
    basic_file, passed_dest, expected_dest_path, expected_dest_name
):
    """Ensure that copying a file returns a file object pointing to the new file."""
    new_file = basic_file.copy(passed_dest)
    assert new_file.path == expected_dest_path
    assert new_file.name == expected_dest_name
