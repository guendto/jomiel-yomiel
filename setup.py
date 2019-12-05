#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# jomiel-yomiel
#
# Copyright
#  2019 Toni Gündoğdu
#
#
# SPDX-License-Identifier: Apache-2.0
#
"""setup.py for jomiel-yomiel."""

# Enable VERSION_TIME to append "%H%M" to the version number.
#

from sys import path

path.insert(0, ".")

from setuptools import setup, find_packages
from yomiel.kore.setup import init as setup_init

setup_init(  # Do this before the import lines for "cmd" below.
    "yomiel", "comm/proto"
)

from yomiel.kore.setup.cmd import CustomCommand__bdist_wheel
from yomiel.kore.setup.cmd import CustomCommand__build_py
from yomiel.kore.setup.cmd import CustomCommand__sdist
from yomiel.kore.setup.cmd import CustomCommand__clean

from yomiel.kore.setup.version import get_semantic_version
from yomiel.kore.setup.file import read_file

GITHUB_ADDR = "https://github.com/guendto/jomiel-yomiel/"
VERSION = "0.1.0"

# Tell kore.setup.cmd to use the specified semantic version string,
# instead.
#
from os import environ as env

env["USE_SEMANTIC_VERSION"] = VERSION

setup(
    name="yomiel",
    author="Toni Gündoğdu",
    author_email="<>",
    version=get_semantic_version(),
    description="Pretty printer for jomiel messages",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url=GITHUB_ADDR,
    packages=find_packages(exclude=[]),
    package_data={
        "yomiel": [
            "config/logger/yomiel.yaml",
            "VERSION",
            # Issue:
            #   - The 'build' stage fails to find the generated *_pb2.py
            #   files, even when 'build_py' target is built first
            # Workaround:
            #   - Force the inclusion of 'comm/proto/*.py files here so that
            #   they are included
            #
            "comm/proto/*.py",
        ],
    },
    python_requires=">=3.6",
    install_requires=[
        "configargparse",
        "protobuf",
        "pyzmq",
        "ruamel.yaml",
    ],
    entry_points={"console_scripts": ["yomiel=yomiel:main"]},
    cmdclass={
        "bdist_wheel": CustomCommand__bdist_wheel,
        "build_py": CustomCommand__build_py,
        "sdist": CustomCommand__sdist,
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
