
class stack:
    def __init__(self):
        self.array = []

    def push(self, data):
        self.array.append(data)

    def pop(self):
        self.array.pop()

    def traverse(self):

        for i in self.array:
            print(i, end=' ')

    def tos(self):

        print(self.array[len(self.array)-1])


s = stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)


s.traverse()

s.pop()
s.pop()
s.pop()

print()


s.push(1000)
s.traverse()

print()
s.tos()
