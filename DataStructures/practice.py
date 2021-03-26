
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

    def createAtGivenLocation(self):
        pass

    def deleteAtStart(self):
        pass

    def createAtEnd(self):
        pass

    def createAtGivenLocation(self):
        pass

    def traverse(self):
        pass
