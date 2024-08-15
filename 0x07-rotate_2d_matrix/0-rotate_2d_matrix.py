#!/usr/bin/python3
'''
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    - Prototype: def rotate_2d_matrix(matrix):
    - Do not return anything. The matrix must be edited in-place.
    - You can assume the matrix will have 2 dimensions and will not be empty.
'''


def rotate_2d_matrix(matrix):
    '''Rotate it 90 degrees clockwise'''
    length = len(matrix)

    # Transpose the matrix
    for i in range(length):
        for j in range(i + 1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(length):
        matrix[i].reverse()
