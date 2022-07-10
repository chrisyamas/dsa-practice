
def fib(n, memo={}):
    if n == 0 or n == 1:
        return n
    if not memo.get(n):
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
    return memo[n]


if __name__ == '__main__':
    result = fib(19)
    print(result)
