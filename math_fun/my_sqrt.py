# LeetCode 69. Sqrt(x)


# Initial Brute Force Solution
def slow_my_sqrt(x):
    for i in range(x + 1):
        if i * i > x:
            return i - 1
        elif i * i == x:
            return i


