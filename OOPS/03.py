class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')
        


p = Person()
# Output: 10
print(Person.age)

# Output: <function Person.greet>
print(Person.greet)

p.greet()

# Output: "This is a person class"
print(Person.__doc__)
