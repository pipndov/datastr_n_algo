class Node:
    def __init__ (self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, val):
        new_node = Node(val)            # the value is inserted into the node class providing it with a next pointer
        self.head = new_node            # initialize Linked List will have first Node be head
        self.tail = new_node            # initialize Linked List will have first Node be tail
        self.length = 1                 # track length 

    def insertNode(self,val):
        new_node = Node(val)            
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        self.tail.next = new_node       # have the tail point the new node
        self.tail = new_node            # new node now becomes the tail
        self.length += 1

