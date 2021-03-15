# 7. Write code to create a 4x3 matrix with values ranging from 2 to 13

import numpy as np

matrix = np.arange(2, 14).reshape((4, 3))

print(matrix)

'''
[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]
 [11 12 13]]
'''
