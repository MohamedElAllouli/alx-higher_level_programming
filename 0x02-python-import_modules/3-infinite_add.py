#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("0")
    elif n == 1:
        print("{}".format(int(sys.argv[1])))
    elif n > 1:
        i = 0
        sume = 0
        for arg in sys.argv:
            if i != 0:
                sume = sume + int(arg)
            i = i + 1
        print("{}".format(sume))
