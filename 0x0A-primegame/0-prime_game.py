#!/usr/bin/python3
"""Module that defines a function to determine the winner of a prime number game."""

def determine_winner(rounds, nums):
    """Evaluates the winner of the prime number game after several rounds."""
    maria_wins = 0
    ben_wins = 0

    for num in nums:
        available_numbers = list(range(1, num + 1))
        primes_list = find_primes(1, num)

        if not primes_list:
            ben_wins += 1
            continue

        maria_turn = True

        while True:
            if not primes_list:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            smallest_prime = primes_list.pop(0)
            available_numbers.remove(smallest_prime)

            available_numbers = [n for n in available_numbers if n % smallest_prime != 0]

            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Winner: Maria"
    elif ben_wins > maria_wins:
        return "Winner: Ben"
    else:
        return None


def is_prime(n):
    """Checks whether a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(start, end):
    """Returns a list of prime numbers within a given range."""
    return [n for n in range(start, end + 1) if is_prime(n)]


# Sample Test Script

if __name__ == "__main__":
    print("Winner: {}".format(determine_winner(5, [2, 5, 1, 4, 3])))
