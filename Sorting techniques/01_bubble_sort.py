
array = [5, 2, 6, 8, 3, 2, 1, 6, 4, 8, 7]

print(array)


for i in range(len(array)):

    for j in range(len(array) - i - 1):

        if array[j] > array[j + 1]:

            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp


print(array)
