# LeetCode problem 3. Longest Substring Without Repeating Characters

# My solution below is based on LeetCode's solution, modified to use Python's
# built-in dict object and with the variable `res` changed to `max_length`

# Below the function I have included an algorithmic explanation, as well as
# a more in-depth narrative description of the algorithm to help myself
# understand this particular sliding window approach more intuitively.

def length_of_longest_substring(s):
    """
    Given a string s, find the length of the longest substring
    without repeating characters.

    EXAMPLE 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    """
    chars = {}

    left = right = 0

    max_length = 0

    while right < len(s):
        r = s[right]
        if not chars.get(r):
            chars[r] = 1
        else:
            chars[r] += 1

        while chars[r] > 1:
            l = s[left]
            chars[l] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

        right += 1
    return max_length


# ---This function uses a version of the Sliding Window Technique---
# Initialize empty dictionary
# Initialize left and right index pointers at 0
# Initialize max_length var at 0
# Run loop while right pointer is less than length of string:
#   - If character at right index is not yet a key in chars dictionary,
#   add character to dictionary with value of 1.
#   - Otherwise (if it is in dict), increment its value by 1.
#   - Run nested loop while character's value in dictionary is greater than 1:
#       - Decrement its value by 1, and increment left pointer value by 1.
#   - Before completing outer loop iteration, check which is bigger:
#   the difference between the pointers plus one (right - left + 1), or
#   the current max_length. --> set max_length to larger value.
#   - Increment right pointer value by 1.
# After full pass (outer loop) has completed, return max_length.


# ---Narrative Description of the Algorithm---

# The right pointer ventures out into the string, encountering chars

# The distance between it and the left pointer is the window length

# Newly discovered characters are added to hash with value of 1

# Previously discovered characters have their value incremented by 1

# Left pointer movement triggered when right pointer encounters familiars

# In that case, left character's value in has is decremented by 1, and
# left pointer shifts one spot along in the string

# It will continue doing that until it has encountered a prior occurrence
# of the character that "right" is currently pointing at, such that that
# character's value in the hash has been reduced back to value of 1

# Once all that is over with the left pointer (if it even needed to occur),
# we know that the window length is equal to the difference between the right
# and left pointers PLUS ONE (to count all characters in INCLUSIVE range
# between left and right)

# The current window length is compared to the maximum length encountered so far,
# and if bigger, then maximum length is updated

# And the right pointer continues its journey by taking one more step further

# After right pointer has stepped completely through the string, the maximum length
# is returned by the function

