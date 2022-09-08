# LeetCode Problem 1207. Unique Number of Occurrences

"""
Given an array of integers arr, return true if the number
of occurrences of each value in the array is unique,
or false otherwise.
"""


# First Attempt: Failed (needs to be debugged)
def unique_occurrences(arr):
    count_hash = {}
    for x in arr:
        if x in count_hash:
            count_hash[x] += 1
        else:
            count_hash[x] = 1
    counts_list = list(count_hash.keys())
    return counts_list == set(counts_list)
