

def reverse_string(s):
    """
    Write a function that reverses a string. The input string is given
    as an array of characters s. You must do this by modifying the input
    array in-place with O(1) extra memory.

    Do not return anything, modify s in-place instead.
    """
    # Solution uses two pointers, left and right
    # While left less than right, swap elements at the respective indices,
    # then move inward by one for each index
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
