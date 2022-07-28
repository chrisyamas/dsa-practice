# Leetcode problem 217. Contains Duplicate


def contains_duplicate(nums):
    """
    Given an integer array nums, return true if any value appears at least
    twice in the array, and return false if every element is distinct.
    """
    counts = {}
    for element in nums:
        if element in counts:
            return True
        else:
            counts[element] = 1
    return False


# # One-line solution from LeetCode user:
# return True if len(set(nums)) < len(nums) else False

