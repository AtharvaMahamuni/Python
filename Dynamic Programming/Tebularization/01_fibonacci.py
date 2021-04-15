
def fib(n):
    table = [0 for x in range(n+1)]
    table[1] = 1

    for i in range(n):
        table[i+1] += table[i]
        if i != n-1:
            table[i+2] += table[i]

    return table[n]


print(fib(5))
print(fib(6))
print(fib(7))
print(fib(50))
print(fib(150))

# Output:
# 5
# 8
# 13
# 12586269025
# 9969216677189303386214405760200
