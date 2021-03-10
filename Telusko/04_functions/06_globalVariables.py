a = 15  # global variable


def function():
    # global a
    a = 30
    print(a)
    globals()['a'] = 10


function()
print(a)
