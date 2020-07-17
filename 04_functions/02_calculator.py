def add(num1, num2):
    return(num1+num2)


def sub(num1, num2):
    return(num1 - num2)


def mul(num1, num2):
    return(num1*num2)


def div(num1, num2):
    return(num1/num2)


print("Choose the operation from following: ")
print("1.Add\n2.Sub\n3.Mul\n4.Div")
print("Option No.= ", end="")
n = int(input())

print("Enter the numbers: ")
num1 = int(input("First number = "))
num2 = int(input("Second number = "))

if n == 1:
    ans = add(num1, num2)
elif n == 2:
    ans = sub(num1, num2)
elif n == 3:
    ans = mul(num1, num2)
elif n == 4:
    ans = div(num1, num2)
else:
    print("Wrong Input")

print("Answer: ", ans)
