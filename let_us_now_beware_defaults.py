#!/usr/bin/env python
from utils import fill_me_in


def test_we_know_what_a_default_is():
    def add_one(x=0):
        x += 1
        return x
    assert add_one() == 1
    assert add_one(1) == 2
    assert fill_me_in() == add_one(), "Well, yeah."


def test_where_defaults_live():
    def append_x_to_list(x, l=[]):
        l.append(x)
        return l

    assert append_x_to_list(9) == [9]
    assert append_x_to_list(8, [0, 7]) == [0, 7, 8]
    assert fill_me_in() == append_x_to_list(9), "No, Mr Default, I expect you to"


def test_its_not_just_for_lists():
    def add_key_value_to_dict(k, v, d={}):
        d[k] = v
        return d
    assert add_key_value_to_dict(9, 10) == {9: 10}
    assert fill_me_in() == add_key_value_to_dict(6, 10)

    class Foo(object):
        pass

    def add_attr_to_a_user_defined_object_why_not(att, val, o=Foo()):
        setattr(o, att, val)
        return o

    assert add_attr_to_a_user_defined_object_why_not('foo', 'bar').foo == 'bar'
    again = add_attr_to_a_user_defined_object_why_not('baz', 'qux')
    assert fill_me_in() == again.foo
