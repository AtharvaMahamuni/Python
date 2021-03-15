# 16. Given a 1D array, negate all elements which are between 3 and 8, in place.
import numpy as np


arr = np.arange(0, 9)

a = (arr > 3) & (arr < 8)

arr[a] *= -1

print(arr)

'''
[ 0  1  2  3 -4 -5 -6 -7  8]
'''
