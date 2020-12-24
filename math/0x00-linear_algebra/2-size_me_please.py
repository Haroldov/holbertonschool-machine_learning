#!/usr/bin/env python3

def matrix_shape(matrix):
    dims = []
    while True:
        dims.append(len(matrix))
        matrix = matrix[0]
        if type(matrix) is not list:
            break
        
    return dims
