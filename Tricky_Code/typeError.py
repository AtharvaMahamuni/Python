class Parent:
    num = 100

    def mtd(self):
        print(self.num)
        self.num = 200
        return self.num+10


print(Parent().mtd())
