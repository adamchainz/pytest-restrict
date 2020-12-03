import sys

import pytest

if sys.version_info >= (3, 9):
    from pkgutil import resolve_name
else:
    from pkgutil_resolve_name import resolve_name

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
    bases = tuple(resolve_name(path) for path in types if path != "None")

    def check_type(item):
        klass = getattr(item, "cls", None)
        if klass is None:
            return allow_none
        return issubclass(klass, bases)

    return check_type
