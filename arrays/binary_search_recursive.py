# Solution courtesy of Geeks for Geeks

def binary_search_rec(array, search_val):
    """
    Returns index of x in arr if present,
    else returns -1.
    """
    def bs_rec(arr, lo, hi, x):
        # Check if high index greater than or equal to low index
        # i.e. there are still elements to consider
        if hi >= lo:
            
            # Calculate middle index of current array section
            mid = (hi + lo) // 2

            # Check if middle element is search value
            if arr[mid] == x:
                # Returns middle element if found to be search value
                return mid

            # Check if middle element is greater than search value
            elif arr[mid] > x:
                # Run search on lower half of current array section
                return bs_rec(arr, lo, mid - 1, x)

            # Check if middle element is less than search value
            elif arr[mid] < x:
                # Run search on upper half of current array section
                return bs_rec(arr, mid + 1, hi, x)

        # All array elements have been searched without value found
        else:
            return -1
    return bs_rec(array, 0, len(array) - 1, search_val)
