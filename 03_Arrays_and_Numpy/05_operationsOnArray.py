from numpy import *

# arr1 = array([1, 2, 3, 4])
# arr2 = array([5, 6, 7, 8])

# arr3 = arr1 + arr2

# print(arr3)

# arr1 = arr1 + 3
# print(arr1)


arr1 = array([1, 2, 3, 4, 5])
arr2 = arr1

# After coping 1st array into second they both have same address
# There are no two seperate arrays
# It is also called as alising
print(id(arr1))
print(id(arr2))


# It is a deep copy
arr2 = arr1.copy()
print(id(arr1))
print(id(arr2))


# Here two different arrays are created
# It is shallow copy
arr2 = arr1.view()
print(id(arr1))
print(id(arr2))
