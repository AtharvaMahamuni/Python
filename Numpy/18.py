# 18. Create a random vector of size 10 and sort it.

import numpy as np

vector1 = np.zeros(10)
vector1 = [8, 74, 3, 16, 4, 6, 91, 6, 56, 9]

print("vector is =\n", vector1)

vector2 = np.zeros(10)
vector2 = np.sort(vector1)

print("sorted vector =\n", vector2)

'''
vector is =
 [8, 74, 3, 16, 4, 6, 91, 6, 56, 9]
sorted vector =
 [ 3  4  6  6  8  9 16 56 74 91]
'''
