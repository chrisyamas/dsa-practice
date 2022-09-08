# LeetCode Problem 1207. Unique Number of Occurrences

"""
Given an array of integers arr, return true if the number
of occurrences of each value in the array is unique,
or false otherwise.
"""


# First Successful Attempt
def hash_unique_occurrences(arr):
    count_hash = {}
    for x in arr:
        if x in count_hash:
            count_hash[x] += 1
        else:
            count_hash[x] = 1
    counts_list = list(count_hash.values())
    return len(counts_list) == len(set(counts_list))


# Uses count() method
def hash_and_count_method_unique_occurrences(arr):
    count_hash = {}
    for i in set(arr):
        # If an item in set has count in array already encountered, return false
        if arr.count(i) in count_hash.values():
            return False
        # Otherwise, add the count to the hash to track all counts
        else:
            count_hash[i] = arr.count(i)
    return True
