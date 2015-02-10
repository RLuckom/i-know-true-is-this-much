#!/usr/bin/env python
"""The secret life of bools"""
from utils import fill_me_in


def test_understanding_tests():
    """Are you sitting comfortably? Then we'll begin."""
    assert fill_me_in(), 'Assertions must be True'


def test_can_we_make_some_extra_true():
    assert fill_me_in() is True + 1, "What happens now?"


def test_minus_true_is_not_false():
    x = [0, 1, 2]
    assert fill_me_in() == x[False:-True], "Isn't Faramir from Minus Truth?"


def test_true_is_not_other_than_it_is():
    x = {}
    x[True] = 'foo'
    x[1] = 'bar'
    assert fill_me_in() == x[True], "That's just how the cookie vanishes"


def test_well_we_definitely_know_what_true_is_not():
    assert fill_me_in() == type(True), "I kid, I kid. Of course Santa is real!"
    assert isinstance(True, int) == fill_me_in(), "On the other hand..."
