class Computer:
    def config(self):
        print("i5, 8GB RAM, HP 15'inch")


com1 = Computer()
com2 = Computer()

com1.config()
Computer.config(com2)
