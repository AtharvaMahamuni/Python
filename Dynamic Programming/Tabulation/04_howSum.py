
def howSum(targetSum, numbers):
    table = [None for x in range(targetSum + 1)]
    table[0] = []

    for i in range(targetSum+1):
        if table[i] != None:
            for num in numbers:
                if i + num <= targetSum:
                    table[i + num] = table[i] + [num]

    return table[targetSum]


print(howSum(7, [2, 3]))  # [3, 2, 2]
print(howSum(9, [2, 3, 4]))  # [3, 2, 2, 2]
print(howSum(8, [2, 3, 4]))  # [2, 2, 2, 2]
print(howSum(5, [2, 4]))  # None
print(howSum(0, [1, 2, 3]))  # []
print(howSum(36, [7, 6, 3, 2, 5]))
# [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(howSum(300, [7, 14]))  # None
print(howSum(300, [7, 14, 15]))
# [15, 15, 15, 15, 15, 15, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
