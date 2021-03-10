

def fib(n):
    a = 0
    b = 1
    c = a
    print(a, end=" ")
    print(b, end=" ")
    for i in range(0, n-2):
        print(a+b, end=" ")
        c = a+b
        a = b
        b = c


fib(10)
