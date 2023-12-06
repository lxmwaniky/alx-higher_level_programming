#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for int_list in matrix:
        for integer in int_list:
            condition = integer != int_list[-1]
            print('{:d}'.format(integer), end=' ' if condition else '')
        print('')
