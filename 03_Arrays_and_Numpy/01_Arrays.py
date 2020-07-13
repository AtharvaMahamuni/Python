from array import *

values = array('i', [19, 12, 2, 34, 4, 29, 55])

print(values)


for i in values:
    print(i)

print("--------------------")
newValue = array(values.typecode, (a for a in values))

for i in newValue:
    print(i)

values.reverse()

print("---------------------")

for i in values:
    print(i)
