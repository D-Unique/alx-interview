#!/usr/bin/python3
"""
 This module defines a function that generates pascal_triangle of n
"""

def pascal_triangle(n):
    """
    Represent Pascal's triangle of size n.

    Return a list of integers contain in the
    generated triangle
    """
   
    if n <= 0:
        return []

    a = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = a[i - 1][j - 1] + a[i - 1][j]
        a.append(row)

    return a
