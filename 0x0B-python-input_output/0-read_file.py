#!/usr/bin/python3
""" reads a text file """


def read_file(filename=""):
    """reads a text file"""
    with open("my_file_0.txt", encoding="utf-8") as f:
        l = f.read()
        print(l, end="")
