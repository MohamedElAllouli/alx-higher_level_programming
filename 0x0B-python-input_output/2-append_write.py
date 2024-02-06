#!/usr/bin/python3
""" writes a string to a text file """


def append_write(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
