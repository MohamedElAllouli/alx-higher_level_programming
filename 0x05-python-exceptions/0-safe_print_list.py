#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            c = c + 1
        except IndexError:
            continue
    print("")
    return c
