===============
pytest-restrict
===============

.. image:: https://img.shields.io/travis/adamchainz/pytest-restrict.svg
        :target: https://travis-ci.org/adamchainz/pytest-restrict

.. image:: https://img.shields.io/pypi/v/pytest-restrict.svg
        :target: https://pypi.python.org/pypi/pytest-restrict

Pytest plugin to restrict the test types allowed.

Features
--------

This plugin allows you to restrict the test types allowed to ensure they
inherit from one of a given list of classes. You might need this on large
projects where you have custom test classes that developers might forget about.

About
-----

I developed this feature in a closed source Nose plugin whilst working on the
big Django project at YPlan. We had some custom enhancements and fixes on top
of the Django test classes, but developers sometimes forgot about using them
and instead used the built-in ``unittest`` classes, or the plain Django ones.
Our solution was to just make the test runner blow up if it encountered
non-whitelisted test types. This is a Pytest port of that plugin.

Usage
-----

Install from pip with:

.. code-block:: bash

    pip install pytest-restrict

Python 3.4+ supported.

Pytest will automatically find the plugin and use it when you run ``py.test``,
however by default there are no restrictions. To restrict the test types,
provide ``--restrict-types`` as a comma-separated list of import paths to
allowable test case base classes, for example:

.. code-block:: bash

    # Allow only test cases that inherit from Django
    py.test --restrict-types django.test.TestCase,django.test.SimpleTestCase

If you wish to allow function tests and other non-class test types (e.g.
doctests), provide the special string 'None', for example:

.. code-block:: sh

    # Allow function tests and our custom tests
    py.test --restrict-types None,myproject.test.TestCase
