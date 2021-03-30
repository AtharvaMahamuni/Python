
num = int(input())

div = 0
rem = 0
result = []
ans = 0


def calculate(self, n):

    rem = n % 10
    result.append(rem)
    div = n/10

    if div == 0:
        return

    else:
        calculate(div)


if num < 10:
    print(-1)

else:
    calculate(num)

    for i in result:
        ans = abs(ans - i)


if ans == 1:
    print(1)
else:
    print(-1)
