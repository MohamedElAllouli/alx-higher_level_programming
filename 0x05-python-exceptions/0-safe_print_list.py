#!/user/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        s = 0
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            s = s + 1
        print("")
    except IndexError:
        print("")
    return s
