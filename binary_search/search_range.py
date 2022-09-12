# LeetCode 34. Find First and Last Position of Element in Sorted Array

"""
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""


# First method: binary search, then if found, move out on each side
def search_range(nums, target):
    low = 0
    high = len(nums) - 1
    first_find = None

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            first_find = mid
            break
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1

    if first_find is None:
        return [-1, -1]
    else:
        start = first_find
        while start > 0:
            if nums[start - 1] == target:
                start -= 1
            else:
                break
        end = first_find
        while end < len(nums) - 1:
            if nums[end + 1] == target:
                end += 1
            else:
                break
        return [start, end]
