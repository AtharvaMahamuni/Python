# 15. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
import numpy as np

arr1 = np.arange(1, 16).reshape(5, 3)
arr2 = np.arange(1, 7).reshape(3, 2)

print("first array is = \n", arr1)
print("first array is = \n", arr2)

arr3 = np.array
arr3 = np.dot(arr1, arr2)

print("multiplication of array is = \n", arr3)


'''
first array is = 
 [[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]
 [13 14 15]]
first array is =
 [[1 2]
 [3 4]
 [5 6]]
multiplication of array is =
 [[ 22  28]
 [ 49  64]
 [ 76 100]
 [103 136]
 [130 172]]
'''
