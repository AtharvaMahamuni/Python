
def howSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers)

        if remainderResult != None:
            numList = [num]
            return remainderResult + numList
    return None


print(howSum(7, [2, 3]))
print(howSum(9, [2, 3, 4]))
print(howSum(8, [2, 3, 4]))
print(howSum(5, [2, 4]))
print(howSum(0, [1, 2, 3]))
print(howSum(36, [7, 6, 3, 2, 5]))
print(howSum(300, [7, 14]))
