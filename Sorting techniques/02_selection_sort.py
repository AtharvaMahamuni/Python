
array = [4, 6, 3, 2, 8, 6, 5, 1, 5, 3, 8, 5, 0, 9]

print(array)

for i in range(len(array)):

    min = i

    j = i
    while j < len(array):

        if array[j] < array[min]:
            min = j

        j = j + 1

    temp = array[i]
    array[i] = array[min]
    array[min] = temp


print(array)
