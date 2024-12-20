#!/usr/bin/python3
"""this is a module docstring"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Arg:
        matrix: List[List[int]], the matrix to rotate
    """
    n = len(matrix)

    # Transpose the matrix manually using Simultaneous Assignment
    # In other instances you can use numpy though, Quite easier to use
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
