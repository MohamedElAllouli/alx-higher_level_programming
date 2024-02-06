#!/usr/bin/python3
""" reads a text file """


def read_file(filename=""):
    """reads a text file"""
    with open("my_file_0.txt", encoding="UTF8") as f:
        print(f.read(), end="")
