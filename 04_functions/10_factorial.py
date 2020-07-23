def fact(n):
    f = 1

    for i in range(1, n+1):
        f = f*i
    return f


num = fact(5)

print("factorial is: ", num)
