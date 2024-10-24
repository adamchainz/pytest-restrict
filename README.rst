===============
pytest-restrict
===============

.. image:: https://img.shields.io/github/actions/workflow/status/adamchainz/pytest-restrict/main.yml.svg?branch=main&style=for-the-badge
   :target: https://github.com/adamchainz/pytest-restrict/actions?workflow=CI

.. image:: https://img.shields.io/badge/Coverage-100%25-success?style=for-the-badge
   :target: https://github.com/adamchainz/pygments-git/actions?workflow=CI

.. image:: https://img.shields.io/pypi/v/pytest-restrict.svg?style=for-the-badge
   :target: https://pypi.org/project/pytest-restrict/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

Pytest plugin to restrict the test types allowed.

----

**Testing a Django project?**
Check out my book `Speed Up Your Django Tests <https://adamchainz.gumroad.com/l/suydt>`__ which covers loads of ways to write faster, more accurate tests.

----

Features
========

This plugin allows you to restrict the test types allowed to ensure they inherit from one of a given list of classes.
Useful on projects where you have custom test classes that developers may forget about.

Installation
============

Install with:

.. code-block:: bash

    python -m pip install pytest-restrict

Python 3.9 to 3.13 supported.

Usage
=====

Pytest will automatically find the plugin and use it when you run ``pytest``, however by default there are no restrictions.
To restrict the test types, provide ``--restrict-types`` as a comma-separated list of import paths to allowed test base classes.
The import paths are passed to |pkgutil.resolve_name()|__, for which you should prefer the form ``<module.path>:<classname>``.
It’s best to set ``--restrict-types`` within |addopts|__ in your pytest configuration file.

.. |addopts| replace:: ``addopts``
__ https://docs.pytest.org/en/latest/reference/reference.html#confval-addopts

For example, to restrict tests to Django’s `test case classes <https://docs.djangoproject.com/en/stable/topics/testing/tools/#provided-test-case-classes>`__ within ``pytest.ini``:

.. |pkgutil.resolve_name()| replace:: ``pkgutil.resolve_name()``
__ https://docs.python.org/3/library/pkgutil.html#pkgutil.resolve_name

.. code-block:: ini

    [pytest]
    addopts = --restrict-types django.test:SimpleTestCase

To allow function tests and other non-class test types (such as doctests), provide the special string “None”:

.. code-block:: ini

    [pytest]
    addopts = --restrict-types None,django.test:SimpleTestCase

History
=======

I developed this feature in a closed source Nose plugin whilst working on the big Django project at YPlan.
We had some custom enhancements and fixes on top of the Django test classes, but developers sometimes forgot about using them and instead used the built-in ``unittest`` classes, or the plain Django ones.
Our solution was to just make the test runner error if it encountered non-whitelisted test types.

This package is a pytest port of that plugin.
