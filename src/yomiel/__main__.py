#
# jomiel-yomiel
#
# Copyright
#  2019-2020 Toni Gündoğdu
#
#
# SPDX-License-Identifier: Apache-2.0
#
"""TODO."""


def main():
    """main"""
    from sys import path

    path.append(".")

    from yomiel.app import App
    from yomiel import __version__

    pkg_name = "yomiel"
    data_dir = "%s.data" % pkg_name

    App(
        package_name=pkg_name,
        package_data_dir=data_dir,
        config_module="%s.cache" % pkg_name,
        version=__version__,
    ).run()


if __name__ == "__main__":
    try:
        main()
    except ModuleNotFoundError as error:
        from yomiel.kore.error import if_proto_bindings_missing

        if_proto_bindings_missing(error)

# vim: set ts=4 sw=4 tw=72 expandtab:
