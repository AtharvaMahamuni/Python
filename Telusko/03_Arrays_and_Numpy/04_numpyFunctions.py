from numpy import *

values = array([1, 2, 3, 4, 5.9, 6], int)

print(values)

values = array([1., 2, 3.9, 4, 5, 6])
print(values)

values = array([1, 2, 3, 4, 5, 6])
print(values)


values = linspace(0, 9, 4)  # It will divide 0 to 9 in 4 parts
print(values)

# If we not specify the no. it will devide it in 50 parts which is by default
values = linspace(0, 49)
print(values)

values = zeros(5)
print(values)

values = ones(5)  # , int)
print(values)
