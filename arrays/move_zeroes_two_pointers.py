# LeetCode problem 283. Move Zeroes
# Below is my solution using two pointers: left and right.

def move_zeroes_two_pointers(nums):
    """
    Given an integer array nums, move all 0's to the end of it while
    maintaining the relative order of the non-zero elements.

    Note that you must do this IN-PLACE without making a copy of the array.

    Do not return anything, modify nums in-place instead.
    """
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[right] == 0:
            right -= 1
        elif nums[left] == 0:
            nums.pop(left)
            nums.insert(right, 0)
            right -= 1
        else:
            left += 1
