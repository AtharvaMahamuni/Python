class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40


t1 = Test()
t2 = Test()

del t1.a

print(t2.__dict__)
