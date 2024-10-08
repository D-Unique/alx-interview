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

    a = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if (j < i):
                if (j == 0):
                    a[i].append(1)
                else:
                    a[i].append(a[i-1][j] + a[i-1][j-1])
            elif (j == i):
                a[i].append(1)
    return a
