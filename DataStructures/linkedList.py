# Best Linked List Resource :
# https://www.geeksforgeeks.org/linked-list-set-1-introduction/


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
            print(temp.data, end=' ')
            temp = temp.next

    def createAtStart(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def createAtEnd(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while(temp.next != None):
            temp = temp.next

        new_node = Node(new_data)
        temp.next = new_node

    def createAtGivenLocation(self, location, new_data):

        new_node = Node(new_data)

        if self.head is None and location == 1:
            self.head = new_node
        else:
            if location == 1:
                new_node.next = self.head
                self.head = new_node

            else:
                temp = self.head

                i = 1
                while(temp.next != None and i < location - 1):
                    temp = temp.next
                    i += 1

                new_node.next = temp.next
                temp.next = new_node

    def deleteAtStart(self):

        if self.head == None:
            print("Linked list is empty")

        else:
            temp = self.head
            self.head = self.head.next
            del temp

    def deleteAtEnd(self):

        if self.head == None:
            print("Linked list is Empty")

        else:

            temp = self.head
            prev = None

            while(temp.next != None):
                prev = temp
                temp = temp.next

            prev.next = None
            del temp

    def deleteAtGivenLocation(self, location):

        if self.head == None:
            print("Linked List is Empty")

        elif location == 1:
            temp = self.head
            self.head = self.head.next
            del temp

        else:
            temp = self.head
            prev = None

            i = 1

            while (i < location):
                prev = temp
                temp = temp.next
                i += 1

        prev.next = temp.next
        del temp


if __name__ == '__main__':

    ll = LinkedList()

    ll.printList()

    ll.head = Node(1)

    # ll.printList()

    second = Node(2)
    ll.head.next = second

    # ll.printList()

    third = Node(3)
    second.next = third

    # ll.printList()

    ll.createAtStart(4)
    # ll.printList()

    ll.createAtStart(5)
    # ll.printList()

    ll.createAtEnd(6)
    # ll.printList()

    ll.createAtStart(0)

    ll.createAtEnd(7)

    ll.createAtGivenLocation(5, 15)

    ll.deleteAtStart()
    ll.deleteAtStart()

    ll.deleteAtEnd()
    ll.deleteAtEnd()

    ll.deleteAtGivenLocation(3)

    ll.printList()
