#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for l, k in list(a_dictionary.items()):
        if k is value:
            a_dictionary.pop(l)
    return a_dictionary
