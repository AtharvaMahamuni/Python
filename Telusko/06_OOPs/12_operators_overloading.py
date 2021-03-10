a = 5
b = 6

print(a+b)
print(int.__add__(a, b))


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, value):
        s1 = self.m1 + self.m2
        s2 = value.m1 + value.m2
        if s1 > s2:
            return True
        else:
            return False

    def __str__(self):
        return '{}  {}'.format(self.m1, self.m2)


s1 = Student(58, 69)
s2 = Student(60, 65)


s3 = s1 + s2
print(s3.m1)
print(s3.m2)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")


a = 9
print(a.__str__())

print(s1.__str__())
