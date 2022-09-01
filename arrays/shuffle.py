# LeetCode Problem 1470. Shuffle the Array

"""
Given the array nums consisting of 2n elements in the form
[x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""


# My first solution
def shuffle(nums, n):
    a = nums[0:n]
    b = nums[n:2 * n]
    new_nums = []
    for i in range(len(a)):
        new_nums.append(a[i])
        new_nums.append(b[i])
    return new_nums


