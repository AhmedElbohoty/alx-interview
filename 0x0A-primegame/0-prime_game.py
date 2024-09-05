#!/usr/bin/python3
''' Prime Game '''


def getPrimes(n):
    '''
     Get the count of primes using Sieve of Eratosthenes algorithm
     Args:
         n (int)
    '''
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    return primes


def isWinner(x, nums):
    '''
    Determine the winner of the Prime Game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of n values for each round.

    Returns:
        str or None: The name of the player that won the most rounds.
        If the winner cannot be determined, returns None.
    '''
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = getPrimes(max_num)

    counts = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        counts[i] = counts[i-1] + (1 if primes[i] else 0)

    maria_wins = sum(counts[n] % 2 == 1 for n in nums)
    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'

    return None
