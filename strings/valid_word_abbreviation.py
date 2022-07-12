def valid_word_abbreviation(word: str, abbr: str) -> bool:
    """
    Problem description from Leetcode:
    Given a string word and an abbreviation abbr, returns whether the string
    matches the given abbreviation. A substring is a contiguous non-empty
    sequence of characters within a string.

    EXAMPLE
    -------
    Input: word = "internationalization", abbr = "i12iz4n"
    Output: true
    Explanation: The word "internationalization" can be abbreviated as
    "i12iz4n" ("i nternational iz atio n").
    """
    word_index = 0
    abbr_index = 0

    while abbr_index < len(abbr):
        abbr_char = abbr[abbr_index]
        if abbr_char.isnumeric():
            if abbr_char == "0":
                return False
            else:
                sub_length = abbr_char
                if abbr_index == len(abbr) - 1:
                    abbr_index += 1
                while abbr_index < len(abbr) - 1:
                    abbr_index += 1
                    if abbr[abbr_index].isnumeric():
                        sub_length += abbr[abbr_index]
                    else:
                        break
                sub_length = int(sub_length)
                word_index += sub_length
        else:
            if word_index >= len(word) or abbr_char != word[word_index]:
                return False
            abbr_index += 1
            word_index += 1

    if word_index != len(word):
        return False
    return True


# More elegant solution from LeetCode user
def leetcode_valid_word_abbrev(word, abbr):
    """
    Solution from LeetCode user jzhanggg.
    """
    m, n = len(word), len(abbr)
    p = cnt = 0
    i = 0
    while i < n:
        if abbr[i].isdigit():
            if cnt == 0 and abbr[i] == '0':
                return False
            cnt = 10 * cnt + int(abbr[i])
        else:
            p += cnt
            if p >= m or word[p] != abbr[i]:
                return False
            p += 1
            cnt = 0
        i += 1
    return p + cnt == m