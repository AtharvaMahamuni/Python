
num = int(input())

sum_is = 0

while num != 0:

    sum_is = sum_is + num%10
    num //= 10

print(sum_is)