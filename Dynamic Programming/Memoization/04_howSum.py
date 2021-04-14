# Classical implementation
'''
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
'''


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
            # Here I am adding the num into the remainderResult because I want to add the number which bring me back to the parent call.
            # See tree diagram for illustration.
            return memo[targetSum]
    memo[targetSum] = None
    return None


print(howSum(7, [2, 3], {}))  # [3, 2, 2]
print(howSum(9, [2, 3, 4], {}))  # [3, 2, 2, 2]
print(howSum(8, [2, 3, 4], {}))  # [2, 2, 2, 2]
print(howSum(5, [2, 4], {}))  # None
print(howSum(0, [1, 2, 3], {}))  # []
print(howSum(36, [7, 6, 3, 2, 5], {}))  # [2, 6, 7, 7, 7, 7]
print(howSum(300, [7, 14], {}))  # None
print(howSum(300, [7, 14, 15], {}))
# [15, 15, 15, 15, 15, 15, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
