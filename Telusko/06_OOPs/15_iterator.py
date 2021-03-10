nums = [7, 8, 9, 5]

it = iter(nums)

print(it.__next__())  # It will print 7
print(it.__next__())  # It will print8

print(next(it))  # It will print 9
