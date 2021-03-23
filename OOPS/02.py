
class Parrot:

    # instance attributes
    def __init__(self):
        self.__name = 'blu'

    def display(self):
        print("{} is bird".format(self.__name))


blu = Parrot()

blu.display()

blu.__name = "kulkanri"
blu.display()


#         self._age = age

#     # instance methods

#     def sings(self, song):
#         return("{} sings {}".format(self._name, song))

#     def dance(self):
#         return("{} is now started to dance".format(self.name))


# # instantiate the object
# blu = Parrot('blu', 12)

# # calling instance method
# print(blu.sings("'Happy'"))
# print(blu.dance())

# blu._age = 15
# blu._name = "Happy"

# print(blu.sings())
