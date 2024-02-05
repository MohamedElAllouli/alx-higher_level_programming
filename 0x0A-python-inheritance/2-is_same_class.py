#!/usr/bin/python3
""" object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """   object is exactly an instance of the specified class
    args:
        @obj: object
        @a_class: instance
    Return: true or false"""
    return type(obj) is a_class
