class A():

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")


class B(A):

    def __init__(self):
        super().__init__()
        # When you create object of sub-class it will call init of sub-class first
        # If you have call super then it will first call init of Super class then call init of sub-class
        print("In B init")
        # if you create object of sub-class it will first try find init of sub-class
        # if it is not found then it will call init of super class

    def feature1(self):
        print("Feature 1-B working")

    def feature4(self):
        print("Feature 4 working")


b1 = B()
# b1.feature3()
b1.feature2()
b1.feature1()  # It will call feature 1 from class B
