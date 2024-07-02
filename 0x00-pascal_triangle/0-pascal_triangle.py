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
    memo = {}
    if not isinstance(n, int) or n <= 0:
        return []

    res = []
    for row in range(1, n + 1):
        pascal_row = []
        for col in range(1, row + 1):
            pascal_row.append(calc_value(row, col, memo))
        res.append(pascal_row)

    return res


def calc_value(r, c, memo):
    """
    Calculates value at row and col index

    Args:
        - r: row index
        - c: column index
    """
    # Base case
    if c == 1 or r == c:
        return 1

    if (r, c) in memo:
        return memo[(r, c)]

    else:
        result = calc_value(r - 1, c - 1, memo) + calc_value(r - 1, c, memo)
        memo[(r, c)] = result
        return result
