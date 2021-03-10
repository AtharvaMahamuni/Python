a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

try:
    print(a/b)
# except Exception as e:
except ZeroDivisionError as e:
    print("Hey you can't divide by zero.", e, "exception")

except ValueError as e:
    print("Invalid Input", e)

except Exception as e:
    print("Something went wrong...")

print("BYE!!!")
