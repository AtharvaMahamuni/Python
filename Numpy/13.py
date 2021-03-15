# 13. Create a 2d array with 1 on the border and 0 inside.

import numpy as np

arr = np.ones((5, 5))

arr[1:-1, 1:-1] = 0

print(arr)

'''
[[1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1.]]
'''
