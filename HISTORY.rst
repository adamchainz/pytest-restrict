.. :changelog:

History
=======

Pending Release
---------------

.. Insert new release notes below this line

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
