
# Classical Solution
# def canSum(targetSum, numbers):
#     if targetSum == 0:
#         return True
#     if targetSum < 0:
#         return False

#     for i in numbers:
#         # if i <= targetSum: #This condition is possible at 2 places.
#         if (canSum(targetSum - i, numbers)) == True:
#             return True
#     return False


# DP Impelentation with memoization
def canSum(targetSum, numbers, memo={}):
    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        # if i <= targetSum: #This condition is possible at 2 places.
        if (canSum(remainder, numbers, memo)) == True:
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


print(canSum(7, [5, 3, 4, 7], {}))  # True
print(canSum(7, [4, 2], {}))  # False
print(canSum(8, [4, 2], {}))  # True
print(canSum(8, [6, 5, 7], {}))  # False
print(canSum(300, [7, 14], {}))  # False
