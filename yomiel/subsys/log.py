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
"""TODO."""


def init():
    """Initiates the logging subsystem."""

    from yomiel.kore.log import log_init
    from yomiel.cache import logger_paths  # pylint: disable=E0611

    logger_file = log_init(logger_paths)

    from yomiel import lg
    lg().debug('subsys/log: configuration file loaded from \'%s\'',
               logger_file)
    lg().info('log subsystem initiated')


# vim: set ts=4 sw=4 tw=72 expandtab:
