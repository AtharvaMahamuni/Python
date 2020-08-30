
class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        print("Inside __init__")

    def config(self):
        print("Specs are " + self.cpu + "  " + self.ram)


com1 = Computer("i5", 16)
com2 = Computer("Rhyzen 3", 8)

com1.config()
com2.config()
