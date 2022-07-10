# LeetCode problem

def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of
    the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may
    not use the same element twice.

    You can return the answer in any order.
    """
    hashmap = {nums[i]: i for i in range(len(nums))}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]