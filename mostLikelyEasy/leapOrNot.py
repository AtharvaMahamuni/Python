
given_year = int(input())

if((given_year%4 == 0) and (given_year%400 == 0 or given_year %100 != 0)):
    print(given_year, "is leap year")
else:
    print(given_year, "is not a leap year")