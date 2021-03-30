
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def createAtStart(self, new_data):

        p = Node(new_data)

        if self.head is None:
            self.head = p

        else:
            p.next = self.head
            self.head = p

    def createAtEnd(self, new_data):

        p = Node(new_data)

        if self.head is None:
            self.head = p

        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = p

    def createAtGivenLocation(self, loc, new_data):

        p = Node(new_data)

        if self.head is None and loc == 1:
            self.head = p

        elif self.head is not None:

            i = 1
            q = self.head

            while i < loc - 1 and q != None:
                q = q.next
                i += 1

            if q is None:
                print("Location is Invalid")

            p.next = q.next
            q.next = p

        else:
            print("Invalid Location")

    def deleteAtStart(self):

        if self.head is None:
            print("Linked List is Empty.")

        else:
            p = self.head
            self.head = self.head.next
            del p

    def deleteAtEnd(self):

        p = self.head

        if self.head is None:
            print("Linked List is Empty.")

        elif self.head.next is None:
            p = self.head
            self.head = None
            del p

        else:
            p = self.head.next
            q = self.head

            while p.next:
                q = p
                p = p.next

            q.next = None
            del p

    def deleteAtGivenLocation(self, loc):

        if loc == 1 and self.head is None:
            p = self.head
            del p
            self.head = None

        elif self.head is not None:
            p = self.head.next
            q = self.head

            i = 1
            while i < loc - 1 and p is not None:
                q = p
                p = p.next
                i += 1

            if p is None:
                print("Invalid Location")

            else:
                q.next = p.next
                del p

        else:
            print("Invalid Location")

    def traverse(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def searchNode(self, key):
        temp = self.head
        isIt = False

        while temp:
            if temp.data == key:
                isIt = True
            temp = temp.next

        if isIt:
            print("Key is Present")
        else:
            print("Key is not Present")


ll = LinkedList()

ll.createAtStart(10)
ll.createAtStart(20)
ll.createAtStart(30)
ll.createAtStart(40)

ll.traverse()

ll.createAtEnd(50)
ll.createAtEnd(60)
ll.createAtEnd(70)

ll.traverse()

ll.deleteAtStart()
ll.deleteAtStart()
ll.deleteAtStart()

ll.traverse()

ll.deleteAtEnd()
ll.deleteAtEnd()

ll.traverse()

ll.createAtStart(10)
ll.createAtEnd(60)
ll.createAtEnd(70)
ll.createAtEnd(80)

ll.traverse()

ll.createAtGivenLocation(3, 20)
ll.traverse()

ll.deleteAtGivenLocation(3)
ll.deleteAtGivenLocation(1)
ll.traverse()


ll.searchNode(50)
ll.searchNode(40)
