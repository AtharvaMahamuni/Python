def allConstruct(target, wordBank):

    table = [[] for x in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(table)+1):
        for word in wordBank:
            if target[i:i+len(word)] == word:
                newCombination = list(map(
                    lambda subArray: subArray + [word], table[i]))
                table[i+len(word)] = table[i+len(word)]+newCombination

    return table[len(target)]


print(allConstruct('purple', ['pur', 'p', 'le', 'ur', 'ple']))
print(allConstruct('abcdef', ['abc', 'ab', 'cd', 'cde', 'f']))
print(allConstruct('skateboard', [
      'skate', 'eboard', 'ard', 'ska', 'rd']))
# print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
#     'e',
#     'ee',
#     'eee',
#     'eeee',
#     'eeeee',
#     'eeeeee',
# ]
# ))
