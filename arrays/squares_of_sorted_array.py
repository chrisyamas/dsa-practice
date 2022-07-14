# LeetCode Problem 977. Squares of Sorted Array

def sorted_squares(nums):
    """
    Given an integer array nums sorted in non-decreasing order, return an array
    of the squares of each number sorted in non-decreasing order.

    (Note: non-decreasing order allows for possibility of adjacent,
    identical elements.)
    """
    # Do not need to put comprehension in square brackets because sorted
    # function returns iterable in list form, so it will convert the general
    # expression in the parentheses to a list object.
    return sorted(x*x for x in nums)
