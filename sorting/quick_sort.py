# Implementation courtesy of Geeks for Geeks
# Has a pointer to keep track of the elements smaller than the pivot
# At very end of partition() func, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot

def partition(left, right, nums):
    # Pivot is last element and pointer is first element
    piv, ptr = nums[right], left
    for i in range(left, right):
        if nums[i] <= piv:
            #
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    nums[ptr], nums[right] = nums[right], nums[ptr]
    return ptr


def quicksort(left, right, numbers):
    """
    Uses partition() as helper. Big O of N*log(N).

    Params
    ------
    left: typically first index of 0
    right: typically last index of len(numbers) - 1
    numbers: list being sorted
    """
    if len(numbers) == 1:
        return numbers
    if left < right:
        pivot = partition(left, right, numbers)
        quicksort(left, pivot - 1, numbers)
        quicksort(pivot + 1, right, numbers)
    return numbers
