#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    """Minimum operations"""
    if n <= 1:
        return 0
    i = 2
    result = 0
    while i <= n:
        if n % i == 0:
            result += i
            n = n / i
            i = i - 1
        i = i + 1
    return int(result)
