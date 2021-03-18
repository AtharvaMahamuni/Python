class parrot:

    # class attributes
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


# instance of the parrot class
blu = parrot('blu', '14')
woo = parrot('woo', '11')

print(blu.name)
print(blu.age)

print(blu.species)

print("{} is {} year old.".format(woo.name, woo.age))
print("{} is {} year old.".format(blu.name, blu.age))
