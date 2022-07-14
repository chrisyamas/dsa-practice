# LeetCode Problem 189. Rotete Array
# This is my original solution, but it seems to have a suboptimal runtime

def rotate(nums, k):
    """
    Given an array, rotate the array to the right by k steps,
    where k is non-negative.

    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]

    NOTE: Do not return anything, modify nums IN-PLACE instead.
    """
    for i in range(k):
        element = nums.pop()
        nums.insert(0, element)
