
def canConstruct(target, wordBank):

    table = [False for x in range(len(target)+1)]
    table[0] = True

    for i in range(len(target)+1):
        if table[i] == True:
            for word in wordBank:
                # If the word matches at the string present at postion i
                if (target[i: i+len(word)] == word):
                    table[i+len(word)] = True

    return table[len(target)]


print(canConstruct('abcdef', ['abc', 'ab', 'abcd', 'cd', 'cdef', 'f']))
print(canConstruct('skateboard', ['skate', 'eboard', 'ard', 'ska', 'rd']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee',
]
))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeeef',
    'eeeee',
    'eeeeee',
]
))
