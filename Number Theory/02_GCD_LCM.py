
def gcd(num1, num2):
    
    if num1 == 0:
        return num2
    
    elif num2 == 0:
        return num1
    
    elif num1 >= num2:
        return gcd(num1 - num2, num2)
    
    else:
        return gcd(num1, num2 - num1)

    

num1 = int(input())
num2 = int(input())

print("GCD is ",gcd(num1, num2))
print("LCM is ",(num1*num2/gcd(num1, num2)))