# class Computer:
#     pass

# c1 = Computer()
# print(id(c1))

class Person:

    def __init__(self):
        self.name = "atharva"
        self.age = 20

    def getInfo(self):
        print(self.name, self.age)

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


p1 = Person()
p2 = Person()

# p1.getInfo()

# print(p1.name)
# p2.getInfo()

# p2.name = "not atharva"
# print(p2.name)

# p2.getInfo()

p2.age = 22
result = p1.compare(p2)

if result:
    print("age is same")
else:
    print("age is different")
