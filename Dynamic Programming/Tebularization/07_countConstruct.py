
def countConstruct(target, wordBank):

    table = [0 for x in range(len(target)+1)]
    table[0] = 1

    for i in range(len(target)+1):
        if table[i] > 0:
            for word in wordBank:
                if word == target[i:i+len(word)]:
                    # table[i+len(word)] += 1 # It is wrong
                    table[i+len(word)] += table[i]

    return table[len(target)]


print(countConstruct('purple', ['pur', 'p', 'le', 'ur', 'ple']))
print(countConstruct('abcdef', ['abc', 'ab', 'cd', 'cde', 'f']))
print(countConstruct('skateboard', [
      'skate', 'eboard', 'ard', 'ska', 'rd']))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee',
]
))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeeef',
    'eeeee',
    'eeeeee',
]
))
