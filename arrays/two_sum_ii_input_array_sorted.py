# LeetCode Problem 167. Two Sum II - Input Array is Sorted

def two_sum_input_arr_sorted(numbers, target):
    """
    Given a 1-indexed array of integers numbers that is already sorted in
    non-decreasing order, find two numbers such that they add up to a specific
    target number. Let these two numbers be numbers[index1] and numbers[index2]
    where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as
    an integer array [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution. You may
    not use the same element twice.

    Your solution must use only constant extra space.
    """
    # Iterate through indices of numbers list using for loop
    # for each i, conduct binary search to find complement
    # once found, return [i + 1, mid + 1]
    for i in range(len(numbers) - 1):
        low = i + 1
        high = len(numbers) - 1
        complement = target - numbers[i]
        while low <= high:
            mid = (low + high) // 2
            if numbers[mid] == complement:
                return [i + 1, mid + 1]
            elif numbers[mid] < complement:
                low = mid + 1
            else:
                high = mid - 1