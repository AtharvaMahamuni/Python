# 6. Reverse a vector (first element becomes last)

import numpy as np

print("Enter the range of the vector")

n = int(input())

vector1 = np.zeros(n)
vector2 = np.zeros(n)

print("Enter the elements in the vector")

for i in range(n):
    vector1[i] = int(input())

print("vector is = ", vector1)

vector2 = vector1[::-1]

print("reverse of the vector is =", vector2)

'''
Enter the range of the vector
6
Enter the elements in the vector
10
20
30
40
50
60
vector is =  [10. 20. 30. 40. 50. 60.]
reverse of the vector is = [60. 50. 40. 30. 20. 10.]
'''
