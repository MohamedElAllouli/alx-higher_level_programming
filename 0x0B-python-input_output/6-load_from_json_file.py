#!/usr/bin/python3
"""writes an Object to a text file,"""


import json


def load_from_json_file(filename):
    """read an Object to a text file,"""
    with open(filename, 'r', encoding='utf-8') as f:
        x = json.load(f)
        return x
