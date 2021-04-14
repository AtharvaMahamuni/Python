# Classical implementation
'''
def bestSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers)

        if remainderCombination != None:
            numList = [num]
            combination = remainderCombination + numList

            # If combination is shorter  than the current shortest then update it.
            if shortestCombination == None or (len(combination) < len(shortestCombination)):
                shortestCombination = combination

    return shortestCombination
'''
# DP implementation


def bestSum(targetSum, numbers, memo={}):
    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, memo)

        if remainderCombination != None:
            numList = [num]
            combination = remainderCombination + numList

            # If combination is shorter  than the current shortest then update it.
            if shortestCombination == None or (len(combination) < len(shortestCombination)):
                shortestCombination = combination

    memo[targetSum] = shortestCombination
    return memo[targetSum]


print(bestSum(7, [2, 3], {}))
print(bestSum(9, [2, 3, 4], {}))
print(bestSum(8, [2, 3, 4], {}))
print(bestSum(5, [2, 4], {}))
print(bestSum(0, [1, 2, 3], {}))
print(bestSum(36, [7, 6, 3, 2, 5], {}))
print(bestSum(300, [7, 14], {}))
print(bestSum(300, [7, 14, 15], {}))
