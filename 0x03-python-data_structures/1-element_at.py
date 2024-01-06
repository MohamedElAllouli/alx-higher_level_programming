#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        exit(None)
    if idx > len(my_list):
        exit(None)
    return my_list[idx]
