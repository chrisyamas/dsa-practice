# A FURTHER optimized solution to LeetCode problem
# 3. Longest Substring Without Repeating Characters

# The function in length_of_longest_substring.py has a time complexity
# of O(N), it will require at most 2N steps.

# The below solution is optimized to require only N steps.


def length_of_longest_substring(s):
    max_length = 0
    index_map = {}
    i = 0

    for j in range(len(s)):
        if s[j] in index_map:
            i = max(index_map[s[j]], i)

        max_length = max(max_length, j - 1 + 1)
        index_map[s[j]] = j + 1

    return max_length
