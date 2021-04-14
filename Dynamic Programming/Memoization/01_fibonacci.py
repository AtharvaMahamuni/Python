
# classic
'''
def fib(n):
    if n <= 2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
'''

# DP implementation
# Type I = Memoization


def fib(n, memo={}):
    if n in memo.keys():
        return memo[n]
    elif n <= 2:
        return 1
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]


print(fib(5))
print(fib(6))
print(fib(7))
print(fib(50))
print(fib(150))
