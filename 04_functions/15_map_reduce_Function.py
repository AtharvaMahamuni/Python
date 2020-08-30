from functools import reduce

nums = [12, 3, 4, 5, 23, 35, 22, 34, 62, 42, 6]

evens = list(filter(lambda n: n % 2 == 0, nums))
doubles = list(map(lambda n: n*2, evens))

print(doubles)
sum = reduce(lambda a, b: a+b, doubles)
print(sum)
