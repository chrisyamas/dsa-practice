# LeetCode Problem 1523. Count Odd Numbers in an Interval Range

def count_odds(low, high):
    """
    Given two non-negative integers low and high.
    Return the COUNT of odd numbers between low and high (inclusive).
    """
    count = (high - low) // 2
    if low % 2 or high % 2:
        count += 1
    return count
