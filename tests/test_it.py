# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import six

if six.PY3:
    pytest_plugins = ['pytester']
else:
    pytest_plugins = [b'pytester']


def test_it_does_nothing_when_no_restriction_is_set(testdir):
    testdir.makepyfile(
        test_one="""
        from unittest import TestCase

        def test_a():
            pass

        class ATest(TestCase):
            def test_a(self):
                pass

        class TestB(object):
            def test_a(self):
                pass

        def foo():
            '''
            >>> foo()
            1
            '''
            return 1
        """
    )
    out = testdir.runpytest('--doctest-modules')
    out.assert_outcomes(passed=4, failed=0)
