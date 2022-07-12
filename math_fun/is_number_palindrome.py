
def is_number_palindrome(x: int) -> bool:
    """
    Problem Description from LeetCode:
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.
    For example, 121 is a palindrome while 123 is not.

    ADDITIONAL EXAMPLE
    ------------------
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left,
    it becomes 121-. Therefore, it is not a palindrome.
    """
    if x < 0:
        return False
    x = str(x)
    left = 0
    right = len(x) - 1

    while left <= right:
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1

    return True


# Solution from LeetCode user Skiper228
def fast_short_elegant_is_num_palindrome(x: int) -> bool:
    """
    Uses reverse indexing.
    """
    return str(x) == str(x)[::-1]
