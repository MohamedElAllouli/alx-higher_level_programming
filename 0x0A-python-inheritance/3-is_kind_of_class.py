#!/usr/bin/python3
""" object is exactly an instance of the specified class"""


def is_kind_of_class(obj, a_class):
    """   object is exactly an instance of the specified class
    args:
        @obj: object
        @a_class: instance
    Return: true or false"""
    return isinstance(obj, a_class)
