#!/usr/bin/python3
""" reads a text file """


def read_file(filename=""):
    """reads a text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
