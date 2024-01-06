#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if element < 0:
        return my_list
    if element > len(my_list) - 1:
        return my_list
    my_list[idx] = element
    return my_list
