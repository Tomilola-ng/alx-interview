#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(rounds, numbers):
    """
    Determines the overall winner of a prime number selection game.

    Args:
        rounds (int): Number of game rounds to be played.
        numbers (list of int): List where each value represents the range
        of numbers from 1 to n in each round.

    Returns:
        str: The name of the player with the most victories ("Ben" or "Maria").
        If it's a tie or no winner can be determined, returns None.
    """
    # Validate input
    if rounds <= 0 or not numbers:
        return None
    if rounds != len(numbers):
        return None

    # Track scores for each player
    ben_score = 0
    maria_score = 0

    # Array to store prime number indicators, based on the maximum number
    max_number = max(numbers)
    prime_array = [1] * (max_number + 1)

    # Mark non-prime numbers (0 and 1) explicitly
    prime_array[0], prime_array[1] = 0, 0

    # Use Sieve of Eratosthenes to mark non-prime numbers in the array
    for i in range(2, len(prime_array)):
        mark_non_primes(prime_array, i)

    # Iterate through each round and tally wins for each player
    for num in numbers:
        if sum(prime_array[:num + 1]) % 2 == 0:
            ben_score += 1  # Ben wins if prime count is even
        else:
            maria_score += 1  # Maria wins if prime count is odd

    # Determine the overall winner
    if ben_score > maria_score:
        return "Ben"
    if maria_score > ben_score:
        return "Maria"
    return None


def mark_non_primes(array, num):
    """
    Marks multiples of a prime number as non-prime in the given list.

    Args:
        array (list of int): Array where prime numbers are marked with 1.
        num (int): Prime number for which multiples are to be marked.

    Returns:
        None.
    """
    # Mark multiples of 'num' as non-prime (set to 0)
    for i in range(2, len(array)):
        try:
            array[i * num] = 0
        except (ValueError, IndexError):
            break  # Stop if index goes out of bounds


if __name__ == "__main__":
    print("Winner: {}".format(determine_winner(5, [2, 5, 1, 4, 3])))
