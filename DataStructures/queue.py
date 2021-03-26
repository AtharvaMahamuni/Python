
class queue:

    def __init__(self):
        self.array = []

    def enqueue(self, data):
        self.array.append(data)

    def dequeue(self):
        print(self.array.pop(0))

    def traverse(self):

        for i in self.array:
            print(i, end=" ")


q = queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)


q.traverse()

print()
q.dequeue()
q.dequeue()
q.dequeue()

q.traverse()
