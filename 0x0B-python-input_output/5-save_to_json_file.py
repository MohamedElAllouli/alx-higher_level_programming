#!/usr/bin/python3
"""writes an Object to a text file,"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file,"""
    json.dump(my_obj, filename)
