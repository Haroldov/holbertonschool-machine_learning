#!/usr/bin/env python3
"""Mod for compute matrix shape."""

def matrix_shape(matrix):
    """Func to compute matrix shape."""
    dims = []
    while True:
        dims.append(len(matrix))
        matrix = matrix[0]
        if type(matrix) is not list:
            break
        
    return dims
