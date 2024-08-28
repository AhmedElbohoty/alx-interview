#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
    grid: A list of list of integers representing the island.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                # Check if there's a land cell to the left
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                # Check if there's a land cell to the above
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
