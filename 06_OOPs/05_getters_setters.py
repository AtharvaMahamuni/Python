
class Student:

    school = "Telusko"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def info(cls): #cls is used for class which refers to whole class differnt from self
        return cls.school


s1 = Student(34, 46, 32)
s2 = Student(89, 32, 12)

print(s1.avg())
print(s2.avg())

s1.set_m1(23)
print(s1.get_m1())

print(Student.info())
