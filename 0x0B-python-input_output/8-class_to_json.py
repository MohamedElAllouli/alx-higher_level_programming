#!/usr/bin/python3
"""class_to_json module.
Contains a function that returns a dictionary.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data
    """
    return obj.__dict__
