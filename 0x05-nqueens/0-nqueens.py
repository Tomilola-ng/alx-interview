#!/usr/bin/python3
"""
    N-Queens puzzle solver using backtracking.
"""

import sys


def is_safe(board, row, col):
    """ Check if it's safe to place a queen at board[row][col]. """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True  # If no conflicts are found, return True


def solve_nqueens(N, row, board):
    """ Use backtracking to find all solutions for N-Queens. """
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return  # Exit the function

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col  # Place a queen at board[row][col]
            solve_nqueens(N, row + 1, board)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)  # Exit with error code 1 (general error)

try:
    N = int(sys.argv[1])  # Convert the first argument to an integer
except ValueError:
    print("N must be a number")
    sys.exit(1)  # Exit with error code 1 (general error)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)  # Exit with error code 1 (general error)

board = [-1] * N  # Board is represented as a list of -1s
solve_nqueens(N, 0, board)
