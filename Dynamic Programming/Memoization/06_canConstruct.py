
# Classical implementation
'''
def canConstruct(target, wordBank):
    if target == '':
        return True

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]

            if(canConstruct(suffix, wordBank) == True):
                return True
    return False
'''

# DP implementation

def canConstruct(target, wordBank, memo={}):
    if target in memo.keys():
        return memo[target]
    if target == '':
        return True

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]

            if(canConstruct(suffix, wordBank, memo) == True):
                memo[target] = True
                return True
    memo[target] = False
    return False


print(canConstruct('abcdef', ['abc', 'ab', 'cd', 'cde', 'f'], {}))
print(canConstruct('skateboard', ['skate', 'eboard', 'ard', 'ska', 'rd'], {}))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee',
], {}
))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeeef',
    'eeeee',
    'eeeeee',
], {}
))
