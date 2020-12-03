from importlib import import_module

import pytest

MARKER_NAME = "restricted_type"


def pytest_addoption(parser):
    group = parser.getgroup("restrict", "Restricts the test types allowed")
    group._addoption(
        "--restrict-types",
        dest="restrict_types",
        type=str,
        default="",
        help="A comma-separated list of paths to allowed test class bases.",
    )


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        MARKER_NAME + ": automatically added by pytest-restrict for bad test types.",
    )


def pytest_collection_modifyitems(session, config, items):
    restrict_types = config.getoption("restrict_types")
    if not restrict_types:
        return

    type_list = restrict_types.split(",")

    check_type = create_check_type(type_list)

    for item in items:
        if not check_type(item):
            item.add_marker(MARKER_NAME)


def pytest_runtest_setup(item):
    marked_as_restricted = len(list(item.iter_markers(name=MARKER_NAME))) > 0
    if marked_as_restricted:
        pytest.fail("Test is not a type allowed by --restrict-types.")


def create_check_type(types):
    allow_none = "None" in types
    bases = tuple(import_string(path) for path in types if path != "None")

    def check_type(item):
        klass = getattr(item, "cls", None)
        if klass is None:
            return allow_none
        return issubclass(klass, bases)

    return check_type


def import_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImportError if the import failed.
    """
    try:
        module_path, class_name = dotted_path.rsplit(".", 1)
    except ValueError as err:
        msg = "%s doesn't look like a module path" % dotted_path
        raise ImportError(msg) from err

    module = import_module(module_path)

    try:
        return getattr(module, class_name)
    except AttributeError as err:
        msg = 'Module "{}" does not define a "{}" attribute/class'.format(
            module_path,
            class_name,
        )
        raise ImportError(msg) from err
