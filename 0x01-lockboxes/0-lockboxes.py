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
    opened_boxes = set()

    for keys in boxes:
        if len(opened_boxes) == len(boxes) - 1:
            return True

        for key in keys:
            if key <= len(boxes):
                opened_boxes.add(key)

    return False
