def remove_duplicates(arr, n):
    set_record = set([])

    read_stream = 0
    write_stream = 0

    for i in range(n):
        if arr[read_stream] not in set_record:
            set_record.add(arr[read_stream])
            arr[write_stream] = arr[read_stream]
            write_stream += 1
        read_stream += 1

    return arr[:write_stream]



given_array_1 = list(map(int, input().split()))
given_array_2 = list(map(int, input().split()))

given_array_1 = remove_duplicates(given_array_1, len(given_array_1))
given_array_2 = remove_duplicates(given_array_2, len(given_array_2))

print(given_array_1)
print(given_array_2)

combined_array = given_array_1 + given_array_2
print(combined_array)
combined_array.sort()
print(combined_array)

median = 0

if (len(combined_array) % 2 == 0):
    median = (combined_array[len(combined_array)//2] + combined_array[len(combined_array)//2 + 1]) // 2
else:
    median = combined_array[len(combined_array)//2]

print(median)