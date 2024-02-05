#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """  function that returns the list of available
    attributes and methods of an object
    args: object
    Return: list of objects"""
    return dir(obj)
