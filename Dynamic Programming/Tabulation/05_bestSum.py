def bestSum(targetSum, numbers):
    table = [None for x in range(targetSum + 1)]
    table[0] = []

    for i in range(targetSum+1):
        if table[i] != None:
            for num in numbers:
                if i + num <= targetSum:
                    combination = table[i] + [num]
                    # If this current combination is shorter then it is already stored
                    if table[i + num] == None:
                        table[i+num] = combination
                    else:
                        if len(combination) < len(table[i + num]):
                            table[i+num] = combination
    return table[targetSum]


print(bestSum(7, [2, 3]))  # [3, 2, 2]
print(bestSum(9, [2, 3, 4]))  # [4, 3, 2]
print(bestSum(8, [2, 3, 4]))  # [4, 4]
print(bestSum(5, [2, 4]))  # None
print(bestSum(0, [1, 2, 3]))  # []
print(bestSum(36, [7, 6, 3, 2, 5]))  # [2, 6, 7, 7, 7, 7]
print(bestSum(300, [7, 14]))  # None
print(bestSum(300, [7, 14, 15]))
# [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
