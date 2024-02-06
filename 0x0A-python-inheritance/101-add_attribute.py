#!/usr/bin/python3
"""Defines a module 101-add_attribute"""


def add_attribute(obj: object, attr_name: str, attr_value: object):
    """
    add_attribute function
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__setattr__(attr_name, attr_value)
