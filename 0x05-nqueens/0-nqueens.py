#!/usr/bin/python3
'''
The N queens puzzle is the challenge of placing N non-attacking queens on N×N
chessboard. Write a program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of arguments, print Usage:
nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new line,
and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line,
and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
'''
import sys

solutions = []


def main(n):
    '''
    Args:
        n (int): board width and height
    '''
    col = set()
    pos_diag = set()  # (r + c)
    neg_diag = set()  # (r - c)

    res = []
    board = [[0] * n for _ in range(n)]

    def backtrack(r):
        '''
        Back track
        '''
        # Base case
        if r == n:
            print_solutions(board)
            return

        for c in range(n):
            if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            col.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = 1

            backtrack(r + 1)

            col.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = 0

    backtrack(0)
    return res


def print_solutions(board):
    '''
    Print all solutions for NxN board
    Args:
        board (nxn)
    '''
    solution = []
    for index, row in enumerate(board):
        solution.append([index, row.index(1)])

    print(solution)


if __name__ == "__main__":
    args = sys.argv

    if len(args) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    main(N)
