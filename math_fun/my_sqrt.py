# LeetCode 69. Sqrt(x)


# Initial Brute Force Solution
def slow_my_sqrt(x):
    for i in range(x + 1):
        if i * i > x:
            return i - 1
        elif i * i == x:
            return i


# Logarithmic solution
from math import e, log


def log_my_sqrt(x):
    if x < 2:
        return x
    left = int(e ** (0.5 * log(x)))
    right = left + 1
    return left if right * right > x else right
