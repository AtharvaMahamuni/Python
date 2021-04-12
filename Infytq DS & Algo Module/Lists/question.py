

def add(num1, num2, count=0):
    n = len(num1)

    if n == 1:
        return -1

    for i in range(1, n):
        if num1 == num2:
            return count

        if int(num1[:i])+int(num1[i:]) == int(num2):
            return count+1

        else:
            num1 = str(int(num1[:-1])+int(num1[-1]))
            return add(num1, num2, count+1)


while True:
    num1, num2 = input().split("=")
    print(add(num1, num2))
