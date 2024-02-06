#!/usr/bin/python3
"""Defines a module 101-add_attribute"""


def add_attribute(obj : object, attr_name : str , attr_value : object):
    obj.__setattr__(attr_name, attr_value)
