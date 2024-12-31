class Node:
    def __init__ (self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, val):
        new_node = Node(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def insertNode(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

