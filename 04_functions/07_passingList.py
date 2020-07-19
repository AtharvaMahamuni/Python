
even = 0
odd = 0


def check(lst):
    for i in lst:
        if i % 2 == 0:
            global even
            even += 1
        else:
            global odd
            odd += 1
    # return (even, odd)


list = [12, 45, 76, 23, 21, 44, 56, 4, 26, 36, 31, 79]
check(list)

print("Even: {}  Odd:{}".format(even, odd))
