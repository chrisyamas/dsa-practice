# LeetCode problem 242. Valid Anagram
"""
Given two strings s and t, return true if t is an anagram of s,
and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.
"""


def is_anagram(s: str, t: str) -> bool:
    def get_string_hash(string):
        string_hash = {}
        for char in s:
            if string_hash.get(char):
                string_hash[char] += 1
            else:
                string_hash[char] = 1
        return string_hash

    s_hash = get_string_hash(s)
    t_hash = get_string_hash(t)
    if s_hash == t_hash:
        return True
    return False
