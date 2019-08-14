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
    from yomiel.cache import logger_paths, opts  # pylint: disable=E0611
    from yomiel.kore.log import log_init

    (logger_file, logger_idents) = log_init(logger_paths)

    from yomiel import lg

    lg().debug('subsys/log: configuration file loaded from \'%s\'',
               logger_file)

    if opts.logger_idents:
        print(''.join('%s' % [ident for ident in logger_idents]))
        from yomiel.kore.app import exit_normal
        exit_normal()

    lg().info('log subsystem initiated')


# vim: set ts=4 sw=4 tw=72 expandtab:
