#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    if n == 1:
        print("0 argument.")
    elif n == 2:
        print("{} argument".format(n-1))
    else:
        print("{} arguments:".format(n-1))
    if n >= 2:
        for i in range(1, n):
            print("{}: {}".format(i, sys.argv[i]))
            
