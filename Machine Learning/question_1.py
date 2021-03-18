
import numpy as np 

n = int(input())

data = []

# i = n
# while i != 0:
#     data.append(int(input()))
#     i -= 1

data = [int(i) for i in input().split()]

num = [int(i) for i in input().split()]

num1, num2 = num


ind1 = []
ind2 = []

i = 0
for dataList in data:
    if dataList == num1:
        ind1.append(i)
    elif dataList == num2:
        ind2.append(i)
    i += 1
        
# print(ind1)
# print(ind2)

length1 = len(ind1)
length2 = len(ind2)


result = []
for i in range(length1):
    for j in range(length2):
        result.append(abs(ind1[i] - ind2[j]))

print(min(result))