#!/usr/bin/env python
"""A greenhouse full of decorators."""
import pytest
from utils import fill_me_in
# You'll need this soon!
from types import FunctionType


def test_higher_order_functions():
    """In Python (and many other languages!), functions are first-class objects.
    This means they can be passed as objects, assigned to variables, and even
    given properties. These tests demonstrate 'higher order functions,'
    functions that operate on other functions and output modified versions of
    those functions."""
    def caller_wrapper(f):
        def f_wrapped(*args, **kwargs):
            return f(*args, **kwargs)
        return f_wrapped

    def add_one(n):
        return n + 1

    assert fill_me_in() == type(caller_wrapper(add_one))
    assert fill_me_in() == caller_wrapper(add_one)(1)

    def mummify_function(f, n):
        def add_one_wrap(f):
            def wrapped_function():
                return f
            return wrapped_function
        for x in xrange(n):
            f = add_one_wrap(f)
        return f

    add_one_wrapped_5_times = fill_me_in()
    assert add_one_wrapped_5_times()()()()()(1) == 2


def test_decorators():
    """Python has a special syntax for replacing a function with a
    wrapped version of that function. A 'decorator function' is a higher-order
    function that accepts a function as its argument and returns a function.
    You can then put @<decorator name> above the definition of your function and
    it will automatically be replaced with a wrapped version. This example shows
    the use of a decorator for sanitizing input, which is something that might
    have to be done the same way for a number of otherwise different
    functions."""
    def validate_int_decorator(f):
        def validated_f(*args):
            for arg in args:
                if not isinstance(arg, int) or isinstance(arg, bool):
                    raise TypeError("argument must be int!")
            return f(*args)
        return validated_f

    @validate_int_decorator
    def add_one(n):
        return n + 1

    assert fill_me_in() == type(add_one)
    assert fill_me_in() == add_one(4)

    with pytest.raises(fill_me_in()):
        add_one('4')
