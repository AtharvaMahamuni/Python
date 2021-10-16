def isPrime(num):

    for i in range(2, num//2):
        if num % i == 0:
            return 0
        
    return 1


n = int(input())

for _ in range(n):

    num = int(input())

    if isPrime(num):
        print("Prime")
    
    else:
        print("Composite")