#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_n = []
    s = 0
    for i in range(0, list_length):
        try:
            s = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            s = 0
        except IndexError:
            print("out of range")
            s = 0
        except TypeError:
            print("wrong type")
            s = 0
        finally:
            list_n.append(s)
    return list_n
