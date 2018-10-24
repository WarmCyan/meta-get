# setup.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Setup script for the meta package."""

from setuptools import setup

setup(
    name="meta-get",
    version="0.1.0",
    author="Nathan Martindale",
    author_email="nathanamartindale@gmail",
    description="a meta package manager",
    license="GPLv3",
    packages=["meta"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "testfixtures", "pytest-mock"],
)
