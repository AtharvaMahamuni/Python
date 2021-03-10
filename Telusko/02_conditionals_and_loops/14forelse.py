list = [4, 13, 23, 44, 56]

for i in list:
    if i % 5 == 0:
        print(i)
        break
else:
    print("Not Found")
