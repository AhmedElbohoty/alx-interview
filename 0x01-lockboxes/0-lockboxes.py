#!/usr/bin/python3
'''
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    '''
    Args:
       - boxes: is a list of lists
    '''
    if not isinstance(boxes, list):
        return False

    if len(boxes) == 0:
        return False

    opened_boxes = set()
    opened_boxes.add(0)

    for index, keys in enumerate(boxes):
        for key in keys:
            if len(opened_boxes) == len(boxes):
                return True

            if key in keys and key != index:
                opened_boxes.add(key)

    return len(opened_boxes) == len(boxes)
