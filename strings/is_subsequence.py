
def is_subsequence(s, t):
    """
    Given two strings s and t, return true if s is a subsequence of t,
    or false otherwise.
    A subsequence of a string is a new string that is formed from the original
    string by deleting some (can be none) of the characters without disturbing
    the relative positions of the remaining characters.
    (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
    """
    left_bound, right_bound = len(s), len(t)

    def rec_is_subsequence(left_index, right_index):
        # Base cases
        if left_index == left_bound:
            return True
        if right_index == right_bound:
            return False
        # Consume both strings or just the target
        if s[left_index] == t[right_index]:
            left_index += 1
        right_index += 1

        return rec_is_subsequence(left_index, right_index)

    return rec_is_subsequence(0, 0)
