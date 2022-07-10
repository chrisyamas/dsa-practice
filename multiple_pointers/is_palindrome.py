
def is_palindrome(s: str) -> bool:
    """
    Basic string palindrome checker.
    """
    def check_palindrome(string, i, j):
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1

        return True
    return check_palindrome(s, 0, len(s) - 1)


def valid_palindrome(s: str) -> bool:
    """
    A phrase is a palindrome if, after converting all uppercase letters into
    lowercase letters and removing all non-alphanumeric characters, it reads
    the same forward and backward. Alphanumeric characters include letters
    and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.
    """
    s = [x.lower() for x in s if x.isalnum()]
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True


def is_palindrome_one_delete_permitted(s: str) -> bool:
    """
    Given a string s, returns true if the s can be palindrome
    after deleting at most one character from it.
    """
    def check(string, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    i = 0
    j = len(s) - 1
    while i < j:
        # If mismatched pair, try both deletions:
        if s[i] != s[j]:
            return check(s, i + 1, j) or check(s, i, j - 1)
        i += 1
        j -= 1

    return True


# Very elegant solution to above one-delete-permitted version
# from a programmer in LeetCode comments section
def is_palindrome_elegant_version(s: str) -> bool:
    """
    Given a string s, returns true if the s can be palindrome
    after deleting at most one character from it.
    """
    def check(lo, hi, removed=False):
        while lo < hi:
            if s[lo] != s[hi]:
                if removed:
                    return False
                return check(lo + 1, hi, True) or check(lo, hi - 1, True)
            lo += 1
            hi -= 1
        return True
    return check(0, len(s) - 1)


if __name__ == '__main__':
    pass
