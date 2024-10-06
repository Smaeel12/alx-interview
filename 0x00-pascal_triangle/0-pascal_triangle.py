#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n: int):
    """Returns a list of lists of integers representing *
    the Pascal's triangle of n"""
    if (n <= 0):
        return []

    rows = [[1]]
    for r in range(1, n):
        p = r - 1
        rows.append([1 if c == 0 or c == r else rows[p][c - 1] + rows[p][c]
                    for c in range(r + 1)])
    return rows
