#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    index = 0
    if matrix:

        for i in matrix:
            index = 1
            for j in i:
                if index == len(i):
                    print("{:d}".format(j), end="")
                if index < len(i):
                    print("{:d}".format(j), end=" ")
                index += 1
            print()
    else:
        print()
