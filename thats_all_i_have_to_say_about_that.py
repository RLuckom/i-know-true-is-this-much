#!/usr/bin/env python
from utils import fill_me_in


def test_____________huh():
    assert fill_me_in() == "Know what I like?"                       " Lacunae."

    too_quiet = ["Doesn't", 'this', 'list', 'contain' 'six', 'elements?']
    assert fill_me_in() == len(too_quiet)
    assert fill_me_in() == too_quiet[3]
