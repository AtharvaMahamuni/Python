from functools import reduce

nums = [12, 3, 4, 5, 23, 35, 22, 34, 62, 42, 6]

evens = list(filter(lambda n: n % 2 == 0, nums))
# here filter function is used to find even numbers
doubles = list(map(lambda n: n*2, evens))
# here map is used to make double of even number which are filtered
print(doubles)
sum = reduce(lambda a, b: a+b, doubles)
# here reduce function is used to make addition of doubled numbers
print(sum)
