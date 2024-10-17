#!/usr/bin/python3
""" Given a number n,  minOperations method calculates the fewest number of
 operations needed to result in exactly n H characters in the file.
"""


def is_prime(num: int) -> bool:
    """Check prime numbers"""
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def minOperations(n: int) -> int:
    """Calculate the min ops"""
    memo = []
    prime_factors = []
    i = 2

    while True:
        if n == 0 or n < i:
            sum = 0
            for i in prime_factors:
                sum += i
            return sum
        if i in memo or is_prime(i):
            if i not in memo:
                memo.append(i)
            if n % i == 0:
                prime_factors.append(i)
                n = n / i
                i = 1
        i += 1
