# Classical Impelentation
'''
def countConstruct(target, wordBank):
    if target == '':
        return 1

    totalCout = 0

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            numWaysForRest = countConstruct(suffix, wordBank)
            totalCout += numWaysForRest

    return totalCout
'''

# DP implementation


def countConstruct(target, wordBank, memo={}):
    if target in memo.keys():
        return memo[target]

    if target == '':
        return 1

    totalCout = 0

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            numWaysForRest = countConstruct(suffix, wordBank, memo)
            totalCout += numWaysForRest

    memo[target] = totalCout
    return totalCout


print(countConstruct('purple', ['pur', 'p', 'le', 'ur', 'ple'], {}))
print(countConstruct('abcdef', ['abc', 'ab', 'cd', 'cde', 'f'], {}))
print(countConstruct('skateboard', [
      'skate', 'eboard', 'ard', 'ska', 'rd'], {}))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee',
], {}
))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeeef',
    'eeeee',
    'eeeeee',
], {}
)