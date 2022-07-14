# LeetCode Problem 27. Remove Element

def remove_element(nums, val):
    """
    Given an integer array nums and an integer val, remove all occurrences
    of val in nums in-place. Return new length of nums.

    (LeetCode version accounts for fact that it is impossible to change length
    of array in some languages, so this problem description is modified to
    account for the fact that Python is not constrained by that limitation.)
    """
    i = 0
    length = len(nums)
    while i < length:
        if nums[i] == val:
            nums.pop(i)
            length -= 1
        else:
            i += 1
    return length
