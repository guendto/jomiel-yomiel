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

# NOTES:
#    - Set VERSION_TIME to get %H%M appended to the semantic version
#

from setuptools import setup, find_packages
from yomiel.kore.setup import init as setup_init

setup_init(
    'yomiel',  # Must be done before the cmd imports below
    'comm/proto')

# pylint: disable=C0413
from yomiel.kore.setup.cmd import CustomCommand__bdist_wheel
from yomiel.kore.setup.cmd import CustomCommand__build_py
from yomiel.kore.setup.cmd import CustomCommand__sdist
from yomiel.kore.setup.cmd import CustomCommand__clean

from yomiel.kore.setup.version import get_semantic_version
from yomiel.kore.setup.file import read_file

GITHUB_ADDR = 'https://github.com/guendto/jomiel-yomiel/'
VERSION = '0.1.0'

# Tell kore.setup.cmd to use the specified semantic version string,
# instead.
#
from os import environ as env
env['USE_SEMANTIC_VERSION'] = VERSION

setup(
    name='yomiel',
    author='Toni Gündoğdu',
    author_email='<>',
    version=get_semantic_version(),
    description='Pretty printer for jomiel messages',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url=GITHUB_ADDR,
    packages=find_packages(exclude=[]),
    package_data={
        # Add comm/proto/*.py here because for some reason the at the
        # 'build' stage the script can't seem to be able to find the
        # generated *_pb2.py binding files -- even if build_py is called
        # first.
        'yomiel':
        ['config/logger/yomiel.yaml', 'VERSION', 'comm/proto/*.py'],
    },
    python_requires='>=3.5',
    install_requires=read_file('requirements.txt').splitlines(),
    entry_points={
        'console_scripts': ['yomiel=yomiel:main'],
    },
    cmdclass={
        'bdist_wheel': CustomCommand__bdist_wheel,
        'build_py': CustomCommand__build_py,
        'sdist': CustomCommand__sdist,
        'clean': CustomCommand__clean,
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
    project_urls={
        'Bug Reports': '%s/issues' % GITHUB_ADDR,
        'Source': GITHUB_ADDR,
    },
)

# vim: set ts=4 sw=4 tw=72 expandtab:
