pytest_plugins = ["pytester"]


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
    out = testdir.runpytest("--doctest-modules")
    out.assert_outcomes(passed=4, failed=0)


def test_it_allows_one_class(testdir):
    testdir.makepyfile(
        test_one="""
        from unittest import TestCase

        class ATest(TestCase):
            def test_a(self):
                pass
        """
    )
    out = testdir.runpytest("--restrict-types", "unittest.TestCase")
    out.assert_outcomes(passed=1, failed=0)


def test_it_restricts_one_class(testdir):
    testdir.makepyfile(
        test_one="""
        class TestA(object):
            def test_a(self):
                pass
        """
    )
    out = testdir.runpytest("--restrict-types", "unittest.TestCase")
    assert out.ret > 0
    out.stdout.fnmatch_lines(
        ["*Failed: Test is not a type allowed by --restrict-types."]
    )


def test_it_allows_one_function(testdir):
    testdir.makepyfile(
        test_one="""
        def test_a():
            pass
        """
    )
    out = testdir.runpytest("--restrict-types", "None")
    out.assert_outcomes(passed=1, failed=0)


def test_it_restricts_one_function(testdir):
    testdir.makepyfile(
        test_one="""
        def test_a():
            pass
        """
    )
    out = testdir.runpytest("--restrict-types", "unittest.TestCase")
    assert out.ret > 0
    out.stdout.fnmatch_lines(
        ["*Failed: Test is not a type allowed by --restrict-types."]
    )


def test_it_restricts_multiple_types_allowed(testdir):
    testdir.makepyfile(
        my_test_base="""
        from unittest import TestCase

        class A(TestCase):
            pass

        class B(TestCase):
            pass
        """,
        test_one="""
        from my_test_base import A, B

        class ATest(A):
            def test_one(self):
                pass

        class BTest(B):
            def test_one(self):
                pass
        """,
    )
    out = testdir.runpytest("--restrict-types", "my_test_base.A,my_test_base.B")
    out.assert_outcomes(passed=2, failed=0)


def test_it_restricts_multiple_types_not_allowed(testdir):
    testdir.makepyfile(
        my_test_base="""
        from unittest import TestCase

        class A(TestCase):
            pass

        class B(TestCase):
            pass
        """,
        test_one="""
        from unittest import TestCase

        class MyTests(TestCase):
            def test_one(self):
                pass
        """,
    )
    out = testdir.runpytest("--restrict-types", "my_test_base.A,my_test_base.B")
    assert out.ret > 0
    out.stdout.fnmatch_lines(
        ["*Failed: Test is not a type allowed by --restrict-types."]
    )
