
def is_isomorphic(s, t):
    """
    Given two strings s and t, determine if they are isomorphic.
    Two strings s and t are isomorphic if the characters in s
    can be replaced to get t.

    All occurrences of a character must be replaced with another
    character while preserving the order of characters. No two characters
    may map to the same character, but a character may map to itself.
    """
    mapping_s_t = {}
    mapping_t_s = {}

    for c1, c2 in zip(s, t):
        
        # Case 1: No mapping exists is either of the dictionaries
        if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
            mapping_s_t[c1] = c2
            mapping_t_s[c2] = c1

        # Case 2: Either mapping doesn't exist in one dictionary or mapping
        #  exists but doesn't match in either or both of the dictionaries
        elif mapping_s_t.get(c1) != c2 or mapping_t_s(c2) != c1:
            return False

    return True
