# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals


__version__ = '1.0.0'


def pytest_addoption(parser):
    group = parser.getgroup('restrict', 'Restricts the test types allowed')
    group._addoption(
        '--restrict-types', action='store', dest='restrict_types',
        default=None, type=str,
        help="""A comma separated list of test types"""
    )


def pytest_collection_modifyitems(session, config, items):
    if not config.getoption('restrict_types'):
        return
