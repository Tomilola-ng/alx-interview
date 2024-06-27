#!/usr/bin/python3

"""
    Create a function def pascal_triangle(n):
    That returns a list of lists of integers
    representing the Pascal’s triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer
"""

def pascal_triangle(n) -> int:
    """ Main Function """

    pascal_res = []

    if n <= 0:
        return pascal_res

    for x in range(n):
        if x == 0:
            res_row = [1]
        else:
            res_row = [1]
            for y in range(1, x):
                res_row.append(pascal_res[x-1][y-1] + pascal_res[x-1][y])
            res_row.append(1)
        pascal_res.append(res_row)

    return pascal_res
