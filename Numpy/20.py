'''
20. Perform the following operations on an array of mobile phones prices 6999, 7500, 11999,
27899, 14999, 9999.
a. Create a 1d-array of mobile phones prices
b. Convert this array to float type
c. Append a new mobile having price of 13999 Rs. to this array
d. Reverse this array of mobile phones prices
e. Apply GST of 18% on mobile phones prices and update this array.
f. Sort the array in descending order of price
g. What is the average mobile phone price
h. What is the difference b/w maximum and minimum price
'''

import numpy as np

arr = np.array([6999, 7500, 11999, 27899, 14999, 9999])

print("Mobile phone price array = ", arr)

arr = arr.astype(np.float_)

print("Conversion of Float = ", arr)

print("Enter the price of mobile in the array")
a = float(input())
arr = np.append(arr, a)
print(arr)
arr1 = np.array
arr1 = arr[::-1]

print("Reverse of the array = ", arr1)
m = arr1 != 0
arr1[m] = arr[m]-(arr[m]*(18/100))

print("Mobile price with 18% GST = ", arr1)
arr = np.sort(arr1)
arr1 = arr[::-1]

print("array in decending order is = ", arr1)
arr = np.average(arr1)

print("average of the mobile price is = ", arr)
dif = max(arr1)-min(arr1)

print("the difference between maximum and minimum price = ", dif)


'''
Mobile phone price array =  [ 6999  7500 11999 27899 14999  9999]
Conversion of Float =  [ 6999.  7500. 11999. 27899. 14999.  9999.]
Enter the price of mobile in the array
14999
[ 6999.  7500. 11999. 27899. 14999.  9999. 14999.]
Reverse of the array =  [14999.  9999. 14999. 27899. 11999.  7500.  6999.]
Mobile price with 18% GST =  [ 5739.18  6150.    9839.18 22877.18 12299.18  8199.18 12299.18]
array in decending order is =  [22877.18 12299.18 12299.18  9839.18  8199.18  6150.    5739.18]        
average of the mobile price is =  11057.582857142856
the difference between maximum and minimum price =  17138.0
'''
