available = 5

numberOfCandies = int(input("Enter no. of Candies: "))

for i in range(1, numberOfCandies+1):
    if(i > available):
        print("Out of Stock")
        break

    print("candy")
