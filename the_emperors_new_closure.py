#!/usr/bin/env python
from utils import fill_me_in
import pytest


def caller(f):
    return f()


def test_a_closure():
    x = 4
    y = 5

    def adder():
        return x + y
    assert fill_me_in() == caller(adder), "Building the house around the couch"


def test_now_closure_eyes_a_bit_and_squint():
    x = 4
    y = 5

    def adder():
        x += y
        return x
    with pytest.raises(fill_me_in()):
        caller(adder)


def test_throwing_a_tarp_over_him():
    x = [4]
    y = 5

    def adder():
        x[0] += y

    caller(adder)
    assert fill_me_in() == x[0], "Now he's angry and keeps running into stuff"
