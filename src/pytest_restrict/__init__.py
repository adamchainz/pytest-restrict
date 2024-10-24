from __future__ import annotations

from pkgutil import resolve_name
from typing import Callable

import pytest
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.nodes import Item

MARKER_NAME = "restricted_type"


def pytest_addoption(parser: Parser) -> None:
    group = parser.getgroup("restrict", "pytest-restrict")
    group._addoption(
        "--restrict-types",
        dest="restrict_types",
        type=str,
        default="",
        help="A comma-separated list of paths to allowed test class bases.",
    )


def pytest_configure(config: Config) -> None:
    config.addinivalue_line(
        "markers",
        MARKER_NAME + ": automatically added by pytest-restrict for bad test types.",
    )


def pytest_collection_modifyitems(config: Config, items: list[Item]) -> None:
    restrict_types: str = config.getoption("restrict_types")
    if not restrict_types:
        return

    type_list = restrict_types.split(",")

    check_type = create_check_type(type_list)

    for item in items:
        if not check_type(item):
            item.add_marker(MARKER_NAME)


def pytest_runtest_setup(item: Item) -> None:
    marked_as_restricted = len(list(item.iter_markers(name=MARKER_NAME))) > 0
    if marked_as_restricted:
        pytest.fail("Test is not a type allowed by --restrict-types.")


def create_check_type(types: list[str]) -> Callable[[Item], bool]:
    allow_none = "None" in types
    bases = tuple(resolve_name(path) for path in types if path != "None")

    def check_type(item: Item) -> bool:
        klass = getattr(item, "cls", None)
        if klass is None:
            return allow_none
        return issubclass(klass, bases)

    return check_type
