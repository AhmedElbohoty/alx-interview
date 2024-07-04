#!/usr/bin/python3
'''
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH =>
Paste => HHHHHHHHH

Number of operations: 6
'''


def minOperations(n):
    """ Args:
      - n (number): Number of operations.
    """

    if n == 1:
        return 0

    operations = 0

    for i in range(2, n + 1):
        print("i", i)
        while n % i == 0:
            print('n', n)
            operations += i
            n = n // i
        print('==========')

    print(operations)
    return operations
