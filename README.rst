===============
pytest-restrict
===============

.. image:: https://img.shields.io/github/workflow/status/adamchainz/pytest-restrict/CI/master?style=for-the-badge
   :target: https://github.com/adamchainz/pytest-restrict/actions?workflow=CI

.. image:: https://img.shields.io/pypi/v/pytest-restrict.svg?style=for-the-badge
   :target: https://pypi.org/project/pytest-restrict/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

Pytest plugin to restrict the test types allowed.

Features
========

This plugin allows you to restrict the test types allowed to ensure they
inherit from one of a given list of classes. You might need this on large
projects where you have custom test classes that developers might forget about.

About
=====

I developed this feature in a closed source Nose plugin whilst working on the
big Django project at YPlan. We had some custom enhancements and fixes on top
of the Django test classes, but developers sometimes forgot about using them
and instead used the built-in ``unittest`` classes, or the plain Django ones.
Our solution was to just make the test runner blow up if it encountered
non-whitelisted test types. This is a Pytest port of that plugin.

Installation
============

Install from pip with:

.. code-block:: bash

    python -m pip install pytest-restrict

Python 3.5 to 3.9 supported.

----

**Testing a Django project?**
Check out my book `Speed Up Your Django Tests <https://gumroad.com/l/suydt>`__ which covers loads of best practices so you can write faster, more accurate tests.

----

Usage
=====

Pytest will automatically find the plugin and use it when you run ``pytest``,
however by default there are no restrictions. To restrict the test types,
provide ``--restrict-types`` as a comma-separated list of import paths to
allowable test case base classes, for example:

.. code-block:: sh

    # Allow only test cases that inherit from Django
    pytest --restrict-types django.test.TestCase,django.test.SimpleTestCase

If you wish to allow function tests and other non-class test types (e.g.
doctests), provide the special string 'None', for example:

.. code-block:: sh

    # Allow function tests and our custom tests
    pytest --restrict-types None,myproject.test.TestCase

This is most useful as a default set with ``addopts`` in your ``pytest.ini``
(`docs <https://docs.pytest.org/en/latest/customize.html#adding-default-options>`__):

.. code-block:: ini

    [pytest]
    addopts = --restrict-types django.test.TestCase,django.test.SimpleTestCase
