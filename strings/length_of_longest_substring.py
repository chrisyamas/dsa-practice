# LeetCode problem


def length_of_longest_substring(s):
    """
    Given a string s, find the length of the longest substring
    without repeating characters.

    EXAMPLE 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    """
    chars = [0] * 128
    left = right = 0
    res = 0

    while right < len(s):
        r = s[right]
        chars[ord(r)] += 1

        while chars[ord(r)] > 1:
            l = s[left]
            chars[ord(l)] -= 1
            left += 1

        res = max(res, right - left + 1)

        right += 1
    return res
