from numpy import *

arr1 = array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print(arr1)

arr1 = matrix(arr1)
print(arr1)

arr1 = matrix("1 2 3; 4 5 6; 7 8 9")
arr2 = matrix("5 6 7; 8 9 1; 2 3 4")
print(arr2)

arr3 = arr1 + arr2
print(arr3)

arr4 = arr1 * arr2
print(arr4)
