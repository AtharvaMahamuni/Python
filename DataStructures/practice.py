
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):

        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    def createAtStart(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def createAtEnd(self, new_data):

        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node

        else:
            temp = self.head

            while (temp.next):
                temp = temp.next

            temp.next = new_node


ll = LinkedList()

ll.createAtEnd(10)
ll.createAtEnd(20)
ll.createAtEnd(30)
ll.createAtStart(1)
ll.createAtStart(2)
ll.createAtStart(3)

ll.printList()
