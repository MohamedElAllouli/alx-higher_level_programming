#!/user/bin/python3
def safe_print_list(my_list=[], x=0):
    s = 0
    for i in range(0, x):
        try:
            #ijijii
            print("{}".format(my_list[i]), end="")
            s = s + 1
        except IndexError:
            continue
    print("")
    return s
