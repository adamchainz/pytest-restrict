=========
Changelog
=========

4.7.0 (2024-10-24)
------------------

* Drop Python 3.8 support.

* Support Python 3.13.

4.6.0 (2023-07-10)
------------------

* Drop Python 3.7 support.

4.5.0 (2023-06-16)
------------------

* Support Python 3.12.

4.4.0 (2022-05-11)
------------------

* Support Python 3.11.

4.3.0 (2022-01-10)
------------------

* Drop Python 3.6 support.

* Improve group name in ``pytest --help``.

4.2.0 (2021-08-12)
------------------

* Add type hints.

4.1.0 (2021-05-10)
------------------

* Support Python 3.10.

* Stop distributing tests to reduce package size. Tests are not intended to be
  run outside of the tox setup in the repository. Repackagers can use GitHub's
  tarballs per tag.

* Drop Python 3.5 support.

4.0.0 (2020-12-03)
------------------

* Support Python 3.9.
* Move license from BSD to MIT License.
* Rewrite internals to use a marker and fail tests at setup time. This
  allows pytest-restrict to work with pytest-xdist.
* Error message has changed to be shorter: "Failed: Test is not a type allowed
  by --restrict-types."
* Use Python 3.9's ``pkgutil.resolve_name()``, or its backport in the
  `pkgutil_resolve_name
  package <https://pypi.org/project/pkgutil_resolve_name/>`__.

  Thanks Tom Grainger for the backport.

3.1.0 (2019-12-19)
------------------

* Update Python support to 3.5-3.8, as 3.4 has reached its end of life.
* Converted setuptools metadata to configuration file. This meant removing the
  ``__version__`` attribute from the package. If you want to inspect the
  installed version, use
  ``importlib.metadata.version("pytest-restrict")``
  (`docs <https://docs.python.org/3.8/library/importlib.metadata.html#distribution-versions>`__ /
  `backport <https://pypi.org/project/importlib-metadata/>`__).

3.0.0 (2018-02-28)
------------------

* Drop Python 2 support, only Python 3.4+ is supported now.

2.0.0 (2016-04-29)
------------------

* Changed the format of ``--restrict-types`` to take a comma-separated list of
  import paths rather than space separated, which fixes the parsing of e.g.
  ``py.test --restrict-types my.TestCase run/these/test_files.py``.

1.0.0 (2016-04-17)
------------------

* First release on PyPI
