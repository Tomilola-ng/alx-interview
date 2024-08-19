#!/usr/bin/python3

"""
    Test 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
        Rotates the given 2D matrix 90 degrees clockwise in-place.
    """
    # Step 1: Transpose the matrix
    for i in range(len(matrix)):
        # Swap each row with each other row
        for j in range(i, len(matrix)):
            # Swap each element in the row with each other element in the row
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for count, obj in enumerate(matrix):
        # Reverse each element in the row
        matrix[count].reverse()
