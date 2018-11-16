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
def listdir_blank_mock(mocker):
    """Mock for os.listdir, returning just a blank array."""
    listdir_mock = mocker.patch("os.listdir", autospec=True)
    listdir_mock.return_value = []
    return listdir_mock


@pytest.fixture
def chdir_mock(mocker):
    """Mock to avoid changing to a non-existant directory."""
    dir_mock = mocker.patch("os.chdir", autospec=True)
    return dir_mock


@pytest.fixture
def basic_file(abspath_mock):
    """A simple file example."""
    abspath_mock("/path/to/myfile.txt")
    return filesystem.File("/path/to/myfile.txt")


@pytest.fixture
def basic_folder(abspath_mock, listdir_blank_mock):
    """A simple folder example."""
    abspath_mock("/path/to/myfolder")
    return filesystem.Folder("/path/to/myfolder")


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
def test_folder_path_initialization(
    abspath_mock, listdir_blank_mock, given_path, actual_path
):
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
    basic_file,
    abspath_mock,
    chdir_mock,
    shell_mock,
    passed_dest,
    expected_dest_path,
    expected_dest_name,
):
    """Ensure that copying a file calls the correct shell command."""
    abspath_mock(expected_dest_path)
    basic_file.copy(passed_dest)
    shell_mock.assert_called_with("cp /path/to/myfile.txt " + expected_dest_path)


@pytest.mark.parametrize(
    "passed_dest, expected_dest_path, expected_dest_name", COPY_FILE_TEST_PARAMS
)
def test_file_copy_return(
    basic_file,
    abspath_mock,
    chdir_mock,
    shell_mock,
    passed_dest,
    expected_dest_path,
    expected_dest_name,
):
    """Ensure that copying a file returns a file object pointing to the new file."""
    abspath_mock(expected_dest_path)
    new_file = basic_file.copy(passed_dest)
    assert new_file.path == expected_dest_path
    assert new_file.name == expected_dest_name


COPY_FOLDER_TEST_PARAMS = [
    ("../", "/path/myfolder", "myfolder"),
    ("newfolder", "/path/to/newfolder", "newfolder"),
    ("./newfolder", "/path/to/newfolder", "newfolder"),
    ("../newfolder", "/path/newfolder", "newfolder"),
    ("subpath/to/myfolder", "/path/to/subpath/to/myfolder", "myfolder"),
    ("./subpath/to/myfolder", "/path/to/subpath/to/myfolder", "myfolder"),
    ("subpath/to/", "/path/to/subpath/to/myfolder", "myfolder"),
]


@pytest.mark.parametrize(
    "passed_dest, expected_dest_path, expected_dest_name", COPY_FOLDER_TEST_PARAMS
)
def test_folder_copy(
    basic_folder,
    abspath_mock,
    chdir_mock,
    shell_mock,
    passed_dest,
    expected_dest_path,
    expected_dest_name,
):
    """Ensure that copying a folder calls the correct shell command."""
    abspath_mock(expected_dest_path)
    basic_folder.copy(passed_dest)
    shell_mock.assert_called_with("cp -R /path/to/myfolder " + expected_dest_path)


@pytest.mark.parametrize(
    "passed_dest, expected_dest_path, expected_dest_name", COPY_FOLDER_TEST_PARAMS
)
def test_folder_copy_return(
    basic_folder,
    abspath_mock,
    chdir_mock,
    shell_mock,
    passed_dest,
    expected_dest_path,
    expected_dest_name,
):
    """Ensure that copying a folder returns a folder object pointing to the new folder."""
    abspath_mock(expected_dest_path)
    new_folder = basic_folder.copy(passed_dest)
    assert new_folder.path == expected_dest_path
    assert new_folder.name == expected_dest_name


@pytest.mark.parametrize(
    "passed_dest, expected_dest_path", [i[0:2] for i in COPY_FOLDER_TEST_PARAMS]
)
def test_folder_move(
    abspath_mock, chdir_mock, shell_mock, basic_folder, passed_dest, expected_dest_path
):
    """Ensure moving a folder results in the correct shell command."""
    abspath_mock(expected_dest_path)
    basic_folder.move(passed_dest)
    shell_mock.assert_called_with("mv /path/to/myfolder " + expected_dest_path)
