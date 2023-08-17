#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        for j in range(len(i)):
            if j == len(i) - 1:
                print("{:d}".format(i[j]), end="\n")
            else:
                print("{:d}".format(i[j]), end=" ")
