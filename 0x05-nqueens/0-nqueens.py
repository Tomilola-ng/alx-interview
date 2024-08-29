#!/usr/bin/python3

"""
    N-Queens puzzle solver utilizing a backtracking algorithm.
"""
import sys

possible_solutions = []
"""Holds all the valid solutions for the N-Queens problem.
"""
board_size = 0
"""Size of the chessboard (N x N).
"""
positions = None
"""Represents all possible positions on the chessboard.
"""


def parse_input():
    """Fetches and verifies the command-line argument.

    Returns:
        int: The size of the chessboard.
    """
    global board_size
    board_size = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be an integer")
        sys.exit(1)
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    return board_size


def are_attacking(pos1, pos2):
    """Determines if two queens threaten each other.

    Args:
        pos1 (list or tuple): Position of the first queen.
        pos2 (list or tuple): Position of the second queen.

    Returns:
        bool: True if the queens can attack each other, otherwise False.
    """
    if (pos1[0] == pos2[0]) or (pos1[1] == pos2[1]):
        return True
    return abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


def solution_exists(candidate):
    """Checks if a candidate solution is already in the list of solutions.

    Args:
        candidate (list of integers): A potential solution.

    Returns:
        bool: True if the solution exists, otherwise False.
    """
    global possible_solutions
    for existing_solution in possible_solutions:
        match_count = 0
        for existing_pos in existing_solution:
            for candidate_pos in candidate:
                if (existing_pos[0] == candidate_pos[0] and
                        existing_pos[1] == candidate_pos[1]):
                    match_count += 1
        if match_count == board_size:
            return True
    return False


def generate_solution(row, candidate):
    """Generates valid solutions for the N-Queens problem.

    Args:
        row (int): The current row being evaluated.
        candidate (list of lists of integers): A potential solution being constructed.
    """
    global possible_solutions, board_size
    if row == board_size:
        new_candidate = candidate.copy()
        if not solution_exists(new_candidate):
            possible_solutions.append(new_candidate)
    else:
        for col in range(board_size):
            index = (row * board_size) + col
            test_positions = zip(
                [positions[index]] * len(candidate), candidate)
            conflicting_positions = map(
                lambda x: are_attacking(x[0], x[1]), test_positions)
            candidate.append(positions[index].copy())
            if not any(conflicting_positions):
                generate_solution(row + 1, candidate)
            candidate.pop()


def find_solutions():
    """Calculates all possible solutions for the N-Queens problem."""
    global positions, board_size
    positions = list(
        map(
            lambda x: [
                x // board_size, x % board_size], range(
                board_size ** 2)))
    generate_solution(0, [])


board_size = parse_input()
find_solutions()
for solution in possible_solutions:
    print(solution)
