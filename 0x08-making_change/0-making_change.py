#!/usr/bin/python3
# pylint: disable=invalid-name

"""
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.
"""


def makeChange(coins, total):
    """
        main function
        - using dynamic programming
    """
    cache_dp = [total + 1] * (total + 1)
    cache_dp[0] = 0

    for i in range(1, total + 1):
        for j in coins:
            if i - j >= 0:
                cache_dp[i] = min(cache_dp[i], cache_dp[i - j] + 1)

    return cache_dp[total] if cache_dp[total] != total + 1 else -1
