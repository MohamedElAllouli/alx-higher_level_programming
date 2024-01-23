#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        s = a / b
    except ZeroDivisionError:
        s = None
    finally:
        print("Inside result: {}".format(s))
        return s
