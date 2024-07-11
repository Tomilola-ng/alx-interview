#!/usr/bin/python3

"""
Minimum Operations to Obtain H Characters

This module provides a method to calculate the fewest number of operations
needed to generate exactly 'n' H characters in a file.

Function:
    def min_operations(target_count: int) -> int
"""

<<<<<<< HEAD

def min_operations(target_count: int) -> int:
=======
def minOperations(target_count: int) -> int:
>>>>>>> c984ca537978e2f3005fd0cc4cc1165f9832f99a
    """
    Calculate the minimum number of operations required to achieve exactly
    'target_count' H characters in a file.

    Args:
    target_count (int): The desired number of H characters.

    Returns:
    int: The minimum number of operations, or 0 if it's impossible to achieve
         'target_count' H characters.
    """
    operation_count = 0
    factor = 2

    while target_count > 1:
        while target_count % factor == 0:
            operation_count += factor
            target_count //= factor
        factor += 1

    return operation_count
