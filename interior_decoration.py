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
    You can then put @<decorator name> above the definition of your
    function and it will automatically be replaced with a wrapped version.
    This example shows the use of a decorator for sanitizing input, which
    is something that might have to be done the same way for a number of
    otherwise different functions."""
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


def decorators_can_take_arguments():
    """Sometimes you want to pass an argument to a decorator. A contrived
    example would be if you wanted a decorator that validated that the input
    was of a type to be specified individually for each decorated function.
    There are two ways to do this. The first is a higher-order function that
    returns the decorator function you want. The second is a class with a call
    method. We'll start with a higher-order function."""

    def input_must_be_a(arg_type):
        def decorator(f):
            def decorated(*args):
                for arg in args:
                    if not isinstance(arg, arg_type):
                        raise TypeError("{} must be type {}".format(arg,
                                                                    arg_type))
                return f(*args)
            return decorated
        return decorator

    @input_must_be_a(list)
    def append_one(some_list):
        return some_list.append(1)

    assert fill_me_in() == append_one([])
    with pytest.raises(fill_me_in()):
        append_one('4')

    # Another way to do the same thing is to use a class that implements
    # a __call__ method. First, we'll demonstrate that ordinary functions
    # are simply objects with __call__ methods:

    assert fill_me_in() == sum([9, 0])
    assert fill_me_in() == sum.__call__([9, 0])

    class NewSum(object):

        def __call__(some_list):
            ret = 0
            for x in some_list:
                ret += x
            return ret

    sum_function = NewSum()

    assert fill_me_in() == sum_function([9, 0])
    assert fill_me_in() == sum_function.__call__([9, 0])

    # To use a class with a __call__ method as a decorator, implement
    # the __call__ method as the decorator function, and use the
    # __init__ function to assign the arguments to the decorator to
    # instance variables.

    class now_input_must_be_a(object):

        def __init__(self, arg_type):
            self._arg_type = arg_type

        def __call__(self, f):
            arg_type = self._arg_type

            def decorated(*args):
                for arg in args:
                    if not isinstance(arg, arg_type):
                        raise TypeError("{} must be type {}".format(arg,
                                                                    arg_type))
                return f(*args)
            return decorated

    @now_input_must_be_a(list)
    def second_append_one(some_list):
        return some_list.append(1)

    assert fill_me_in() == second_append_one([])
    with pytest.raises(fill_me_in()):
        second_append_one('4')
