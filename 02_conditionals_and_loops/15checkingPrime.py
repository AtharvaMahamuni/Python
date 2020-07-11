
num = 11111111111111111111111111111111111

for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("prime")
