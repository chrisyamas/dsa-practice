
def pivot_index(nums):
    """
    Given an array of integers nums, calculates the pivot index of this array.
    The pivot index is the index where the sum of all the numbers strictly to
    the left of the index is equal to the sum of all the numbers strictly to
    the index's right. If the index is on the left edge of the array, then the
    left sum is 0 because there are no elements to the left. This also applies
    to the right edge of the array.

    Param
    -----
    nums: a list of integers

    Return
    ------
    the leftmost pivot index (or -1 if so such index exists)
    """
    total_sum = sum(nums)
    left_sum = 0
    for i, x in enumerate(nums):
        if left_sum == (total_sum - left_sum - x):
            return i
        left_sum += x
    return -1


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 9, 1, 2, 2, 1]
    result = pivot_index(numbers)
    print(result)
