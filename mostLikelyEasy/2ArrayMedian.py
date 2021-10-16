
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


set1 = set(arr1+arr2)

arr1 = list(set1)

print(arr1[(len(arr1)-1)//2])