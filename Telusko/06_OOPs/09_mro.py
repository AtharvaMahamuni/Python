class A():
    def __init__(self):
        print("In init of class A")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")


class B():
    def __init__(self):
        print("In init of class B")

    def feature1(self):
        print("Feature 1-B working")

    def feature3(self):
        print("Feature 3 working")


class C(A, B):  # Multiple inheritance
    def __init__(self):
        super().__init__()  # here it will invoke constructor of A not of B because prefernce is given to left(first defined class) it is called as MRO(Method Resolution Order)
        print("In init of class C")


c1 = C()
c1.feature1()  # It will call feature1 from class A due to prefernce i.e.MRO
