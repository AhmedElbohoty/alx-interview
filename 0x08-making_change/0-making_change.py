#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total
"""

positive_infinity = float('inf')


def makeChange(coins, total):
    '''
    Args:
        - coins: list of the values of the coins in your possession
        - total: the target

    Returns:
        - int: The fewest number of coins needed to meet total,
        - or -1 if total cannot be met by any number of coins you have.
    '''
    if total < 1:
        return 0

    counted = 0
    result = 0

    for coin in sorted(coins, reverse=True):
        while counted + coin <= total:
            counted += coin
            result += 1

    if counted == total:
        return result

    return -1
