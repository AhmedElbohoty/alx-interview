#!/usr/bin/python3
import random

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))


print(":")
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1], [2], [3], [4], [], [5], [6]]
print(canUnlockAll(boxes))


boxes = [[1], [2], [3], [4], [0]]
print(canUnlockAll(boxes))

boxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [], [], [], [], [], [], [], []]
print(canUnlockAll(boxes))

boxes = [[1, 2], [3, 4], [5], [6, 7], [], [8], [9], [], [], []]
print(canUnlockAll(boxes))

boxes = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [0]]
print(canUnlockAll(boxes))

boxes = [[], [], [], [], [], [], [], [], [], [1]]
print(canUnlockAll(boxes))

boxes = [[1, 2, 3], [4, 5], [6], [7, 8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19]]
print(canUnlockAll(boxes))

boxes = [
    [1, 2, 3],
    [4, 5],
    [6],
    [7, 8],
    [9],
    [10],
    [11],
    [12],
    [13],
    [14],
    [15],
    [16],
    [17],
    [18],
    [19],
    [0],
    [],
    [],
    [],
    []
]
print(canUnlockAll(boxes))
