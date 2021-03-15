# 8. Find indices of nonzeroelements from [1,2,0,0,4,0]

import numpy as np

arr = np.array([1, 2, 0, 0, 4, 0])

result = np.where(arr != 0)

print(result)

'''
(array([0, 1, 4], dtype=int64),)
'''
