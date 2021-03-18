
class Parrot:

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance methods

    def sings(self, song):
        return("{} sings {}".format(self.name, song))

    def dance(self):
        return("{} is now started to dance".format(self.name))


# instantiate the object
blu = Parrot('blu', 12)

# calling instance method
print(blu.sings("'Happy'"))
print(blu.dance())
