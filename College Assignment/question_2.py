
num = int(input())

result = []

i = 10

if num < 10:
    print(-1)

else:
    while i <= num:
        num1 = i % 10
        num2 = i // 10

        if(abs(num1 - num2) == 1):
            result.append(i)

        i += 1

    for i in result:
        print(i, end=" "),
