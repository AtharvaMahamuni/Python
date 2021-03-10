import sys

sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())


def greet():
    print("Hello")
    greet()


greet()

# the default recursion limit is 1000 in python but we can exceed
# this limit with the functions from sys.
