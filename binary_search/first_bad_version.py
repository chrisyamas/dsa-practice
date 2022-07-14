# Problem from LeetCode

# # The isBadVersion API is already defined for you.
# # def isBadVersion(version: int) -> bool:
def is_bad_version(version: int) -> bool:
    pass


def first_bad_version(n: int) -> int:
    """
    Suppose you have n versions [1, 2, ..., n] and you want to find out the
    first bad one, which causes all the following ones to be bad.

    You are given an API bool isBadVersion(version) which returns whether
    version is bad. Implement a function to find the first bad version.
    You should minimize the number of calls to the API.
    """
    # Similar logic as Binary Search
    # Search middle index, if bad then it either IS the first bad,
    # or the first bad is left of it, so assign it to earliest, then look left
    # if not bad, look right
    # after while loop breaks, return earliest
    low = 1
    high = n
    earliest = None
    while low <= high:
        mid = (low + high) // 2
        if is_bad_version(mid):
            earliest = mid
            high = mid - 1
        else:
            low = mid + 1
    return earliest
