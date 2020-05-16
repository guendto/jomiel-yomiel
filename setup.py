#!/usr/bin/env python
#
# jomiel-yomiel
#
# Copyright
#  2019-2020 Toni Gündoğdu
#
#
# SPDX-License-Identifier: Apache-2.0
#
"""setup.py for jomiel-yomiel."""
# Supported env. definitions:
#   - VERSION_TIME to append "%H%M" to the version number
#
PACKAGE_NAME = "yomiel"
GITHUB_ADDR = "https://github.com/guendto/jomiel-%s/" % PACKAGE_NAME
VERSION = "0.1.0"

from sys import path

path.insert(0, ".")

# Initialize by calling kore.setup:init(). Do this before importing the
# custom commands below.

from yomiel.kore.setup import init as setup_init

setup_init(
    name=PACKAGE_NAME,
    bootstrap_path="%s/comm/proto/bin/bootstrap" % PACKAGE_NAME,
    proto_root_dir="%s/comm/proto/" % PACKAGE_NAME,
    bindings_dir="bindings",  # yomiel/data/bindings (*_pb2.py files)
    data_dir="data",  # yomiel/data (VERSION file, etc.)
)

from yomiel.kore.setup.cmd import CustomCommand__bdist_wheel
from yomiel.kore.setup.cmd import CustomCommand__build_py
from yomiel.kore.setup.cmd import CustomCommand__clean

# from yomiel.kore.setup.cmd import CustomCommand__sdist

from yomiel.kore.setup.version import get_semantic_version
from yomiel.kore.setup.file import read_file

requirements = read_file("requirements.in").splitlines()


# kore.setup.cmd.*: use the specified version string, instead.
#
from os import environ as env

env["USE_SEMANTIC_VERSION"] = VERSION

# setup()
#
from setuptools import setup, find_namespace_packages

setup(
    name=PACKAGE_NAME,
    author="Toni Gündoğdu",
    author_email="<>",
    version=get_semantic_version(),
    description="Pretty printer for jomiel messages",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url=GITHUB_ADDR,
    packages=find_namespace_packages(include=["yomiel.*"], exclude=[])
    + ["yomiel"],
    # Note how we append "yomiel" to the "packages" list after looking
    # up the namespace packages. We do this because of the way we have
    # structured the project. find_namepace_packages() fails to add any
    # of the ./yomiel/*.py files.
    #
    include_package_data=True,
    # There are plenty of confusing and conflicting resources around,
    # many of which offer different ideas on how you should use:
    #   - include_package_data
    #   - MANIFEST.in
    #   - setup.py
    #
    # Throw the protobuf compilation into the mix and you'll begin to
    # wonder why even bother with packaging at all.
    #
    # After spending far more time than anyone ever should -- for
    # something as simple as this -- it seems that we have found
    # ourselves a winner combo through great many trials and errors.
    # And that, is good enough for me.
    #   -- the author
    #
    python_requires=">=3.6",
    install_requires=requirements,
    setup_requires=[
        # Add anything in requirements.in that uses the "python_version"
        # environment marker (namely importlib.* that are needed for
        # building the wheel on py36).
        #
        pkg
        for pkg in requirements
        if "python_version" in pkg
    ],
    entry_points={"console_scripts": ["yomiel=yomiel.__main__:main"]},
    cmdclass={
        "bdist_wheel": CustomCommand__bdist_wheel,
        "build_py": CustomCommand__build_py,
        #        "sdist": CustomCommand__sdist,
        "clean": CustomCommand__clean,
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
    ],
    project_urls={
        "Bug Reports": "%s/issues" % GITHUB_ADDR,
        "Source": GITHUB_ADDR,
    },
)

# vim: set ts=4 sw=4 tw=72 expandtab:
