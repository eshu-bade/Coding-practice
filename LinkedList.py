# Creating a Linked List

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

myList = LinkedList()
myList.head = Node(5)
second = Node(6)
third = Node(7)

# Linking the nodes to each other
myList.head.next = second
second.next = third
"""#-------------------------------------------------------------
# Traversing the list

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
            print(temp.data)
            temp=temp.next


myList = LinkedList()
myList.head= Node(5)
myList.head.next =Node(6)
third = Node(7)

myList.head.next.next = third
myList.printList()