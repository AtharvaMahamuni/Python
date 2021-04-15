
def canSum(target, numbers):
    table = [False for x in range(target + 1)]
    table[0] = True

    for i in range(len(table)):
        if table[i] == True:
            for num in numbers:
                if i + num <= target:
                    table[i+num] = True

    return table[target]


print(canSum(7, [5, 3, 4]))  # True
print(canSum(7, [4, 2]))  # False
print(canSum(8, [4, 2]))  # True
print(canSum(8, [6, 5, 7]))  # False
print(canSum(300, [7, 14]))  # False
print(canSum(300, [7, 14, 5]))  # True
