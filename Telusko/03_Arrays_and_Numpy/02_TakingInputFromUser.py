from array import *

values = array("i", [])

n = int(input("Enter the no. of inputs: "))

for i in range(0, n):
    x = int(input("Enter the no.: "))
    values.append(x)


for i in values:
    print(i)

val = int(input("Enter the value to search: "))

for i in range(0, n):
    if(val == values[i]):
        print(i)
        break

print(values.index(val))
