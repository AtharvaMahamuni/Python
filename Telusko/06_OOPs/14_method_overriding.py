class A:
    def show(self):
        print("In show of A")


class B(A):
    # def show(self):
    #     print("In show of B")
    pass


b = B()

b.show()
# when you call show method it will get called from class B
# If you don't have show method in class B then it will get called from class A
