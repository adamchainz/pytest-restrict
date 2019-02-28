from importlib import import_module

import pytest

__version__ = '3.0.0'


def pytest_addoption(parser):
    group = parser.getgroup('restrict', 'Restricts the test types allowed')
    group._addoption(
        '--restrict-types', dest='restrict_types',
        type=str, default='',
        help="""A list of test types"""
    )


def pytest_collection_modifyitems(session, config, items):
    restrict_types = config.getoption('restrict_types')
    if not restrict_types:
        return

    type_list = restrict_types.split(',')

    check_type = create_check_type(type_list)

    errors = []
    for item in items:
        if not check_type(item):
            errors.append(item)

    if errors:
        error_msgs = [error_msg(item, type_list) for item in errors]
        raise pytest.UsageError(*error_msgs)


def create_check_type(types):
    allow_none = ('None' in types)
    bases = tuple(import_string(path) for path in types if path != 'None')

    def check_type(item):
        klass = getattr(item, 'cls', None)
        if klass is None:
            return allow_none
        return issubclass(klass, bases)

    return check_type


def error_msg(item, restrict_types):
    return '{} does not inherit from allowed pytest-restrict bases ({})'.format(
        item.nodeid,
        ','.join(restrict_types),
    )


def import_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImportError if the import failed.
    """
    try:
        module_path, class_name = dotted_path.rsplit('.', 1)
    except ValueError as err:
        msg = "%s doesn't look like a module path" % dotted_path
        raise ImportError(msg) from err

    module = import_module(module_path)

    try:
        return getattr(module, class_name)
    except AttributeError as err:
        msg = 'Module "%s" does not define a "%s" attribute/class' % (
            module_path, class_name)
        raise ImportError(msg) from err
