
def fib_iterative(n: int) -> int:
    fib = {0: 0, 1: 1}
    i = 2
    while i <= n:
        fib[i] = fib[i - 1] + fib[i - 2]
        i += 1
    return fib[n]
