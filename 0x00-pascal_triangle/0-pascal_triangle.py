#!/usr/bin/python3
"""
Create list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Creates list of lists of integers representing the Pascal’s triangle of n

    Return:
        - Empty list if n <= 0
        - Else, list of lists
    """
    res = []
    for row in range(1, n + 1):
        pascal_row = []
        for col in range(1, row + 1):
            pascal_row.append(calc_value(row, col))
        res.append(pascal_row)

    return res


def calc_value(r, c):
    """
    Calculates value at row and col index

    Args:
        - r: row index
        - c: column index
    """
    # Base case
    if c == 1:
        return 1
    if r == c:
        return 1

    return calc_value(r - 1, c - 1) + calc_value(r - 1, c)
