# LeetCode 69. Sqrt(x)


# A simple brute force solution for finding the square root of x.
def slow_my_sqrt(x):
    # Iterate over numbers from 0 to x.
    for i in range(x + 1):
        # Check if the square of the number is greater than x.
        if i * i > x:
            # If so, return the previous number as the integer square root.
            return i - 1
        # Check if the square of the number is exactly equal to x.
        elif i * i == x:
            # If so, return this number as the integer square root.
            return i


# Logarithmic solution
from math import e, log


def log_my_sqrt(x):
    if x < 2:
        return x
    left = int(e ** (0.5 * log(x)))
    right = left + 1
    return left if right * right > x else right


# Binary search solution
def binary_search_my_sqrt(x):
    if x < 2:
        return x
    left, right = 2, x // 2
    while left <= right:
        pivot = left + (right - left) // 2
        num = pivot * pivot
        if num > x:
            right = pivot - 1
        elif num < x:
            left = pivot + 1
        else:
            return pivot
    return right
