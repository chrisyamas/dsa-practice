# LeetCode problem 283. Move Zeroes
# Below is my solution using only one pointer: i.

def move_zeroes_one_pointer(nums):
    """
    Given an integer array nums, move all 0's to the end of it while
    maintaining the relative order of the non-zero elements.

    Note that you must do this IN-PLACE without making a copy of the array.

    Do not return anything, modify nums in-place instead.
    """
    count = 0
    i = 0
    length = len(nums)

    while i < length:
        if nums[i] == 0:
            nums.pop(i)
            count += 1
            length -= 1
        else:
            i += 1

    for i in range(count):
        nums.append(0)
