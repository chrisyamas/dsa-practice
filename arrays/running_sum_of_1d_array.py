def running_sum(nums):
    """
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.
    """
    # If we want to still have nums available:
    run_sum = [x for x in nums]
    for index in range(1, len(run_sum)):
        run_sum[index] += run_sum[index - 1]
    return run_sum

    # Else we could convert nums to run_sum by simply not creating run_sum
    # as a separate array, and just operating on nums in the same way and
    # return nums.


if __name__ == '__main__':
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    number_list_result = running_sum(number_list)
    print(f"Running sum of number_list = {number_list_result}")

