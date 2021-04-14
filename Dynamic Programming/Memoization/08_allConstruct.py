
# Classical Impelentation
'''
def allConstruct(target, wordBank):
    if target == '':
        return [[]]

    result = []

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank)
            targetWays = list(map(lambda way: [word] + way, suffixWays))
            result = result + targetWays

    return result
'''

# DP implementation


def allConstruct(target, wordBank, memo={}):
    if target == '':
        return [[]]
    if target in memo.keys():
        return memo[target]

    result = []

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank, memo)
            targetWays = list(map(lambda way: [word] + way, suffixWays))
            result = result + targetWays
    memo[target] = result
    return result


print(allConstruct('purple', ['pur', 'p', 'le', 'ur', 'ple'], {}))
print(allConstruct('abcdef', ['abc', 'ab', 'cd', 'cde', 'f'], {}))
print(allConstruct('skateboard', [
      'skate', 'eboard', 'ard', 'ska', 'rd'], {}))
print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee',
], {}
))

# This test case is the worst case where we have to create this kind of big 2D array
# print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
#     'e',
#     'ee',
#     'eee',
#     'eeeef',
#     'eeeee',
#     'eeeeee',
# ], {}
# ))
