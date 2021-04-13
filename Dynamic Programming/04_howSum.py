# Classical implementation
# def howSum(targetSum, numbers):
#     if targetSum == 0:
#         return []
#     if targetSum < 0:
#         return None

#     for num in numbers:
#         remainder = targetSum - num
#         remainderResult = howSum(remainder, numbers)

#         if remainderResult != None:
#             numList = [num]
#             return remainderResult + numList
#     return None


# DP implementation with memoization:

def howSum(targetSum, numbers, memo={}):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    if targetSum in memo.keys():
        return memo[targetSum]

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers, memo)
        if remainderResult != None:
            numList = [num]
            memo[targetSum] = remainderResult + numList
            return memo[targetSum]
    memo[targetSum] = None
    return None


print(howSum(7, [2, 3], {}))
print(howSum(9, [2, 3, 4], {}))
print(howSum(8, [2, 3, 4], {}))
print(howSum(5, [2, 4], {}))
print(howSum(0, [1, 2, 3], {}))
print(howSum(36, [7, 6, 3, 2, 5], {}))
print(howSum(300, [7, 14], {}))
print(howSum(300, [7, 14, 15], {}))


# print(howSum(7, [2, 3]))
# print(howSum(9, [2, 3, 4]))
# print(howSum(8, [2, 3, 4]))
# print(howSum(5, [2, 4]))
# print(howSum(0, [1, 2, 3]))
# print(howSum(36, [7, 6, 3, 2, 5]))
# print(howSum(300, [7, 14]))
