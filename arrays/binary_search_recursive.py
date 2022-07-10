# Solution courtesy of Geeks for Geeks

def binary_search_rec(array, search_val):
    """
    Returns index of x in arr if present,
    else returns -1.
    """
    def bs_rec(arr, lo, hi, x):
        if hi >= lo:
            mid = (hi + lo) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return bs_rec(arr, lo, mid - 1, x)
            elif arr[mid] < x:
                return bs_rec(arr, mid + 1, hi, x)

        else:
            return -1
    return bs_rec(array, 0, len(array) - 1, search_val)
