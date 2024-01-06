#!/usr/bin/python3
def no_c(my_string):
    newstring = ""

    if my_string:
        for char in my_string:
            if char != "C" and char != "c":
                newstring += char
    return newstring
