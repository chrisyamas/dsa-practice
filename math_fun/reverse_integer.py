# LeetCode (Medium level) Problem 7. Reverse Integer

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    """
    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit integer
    range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers
    (signed or unsigned).
    """
    if x < 0:
        negative = True
    else:
        negative = False

    x = str(abs(x))

    while True:
        if x == "0":
            break
        if x[-1] == "0":
            x = x[0:-1]
        else:
            break

    x = x[::-1]
    x = int(x)
    if negative:
        x = -x

    if x < (-2) ** 31 or x > (2 ** 31 - 1):
        return 0
    else:
        return x
