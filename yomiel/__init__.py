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


def main():
    """main"""
    from yomiel.kore.path import set_proto_path
    set_proto_path(__file__, 'comm/proto/')

    from yomiel.app import App

    App(module_name=__name__,
        pkg_resources_name=__name__,
        config_module='yomiel.cache').run()


def lg():  # pylint: disable=C0103
    """Returns the logger instance used to print to the logging
    subsystem to record new events.

    The subsystem is configured via a separate logger YAML configuration
    file. The configuration supports different logger identities.

    To use this function (lg):

        from jomiel import lg
        lg().debug('foo=%s' % foo)

    Returns
        The logger instance

    """
    from yomiel.cache import opts  # pylint: disable=E0611
    import logging as lg
    return lg.getLogger(opts.logger_ident)


# vim: set ts=4 sw=4 tw=72 expandtab:
