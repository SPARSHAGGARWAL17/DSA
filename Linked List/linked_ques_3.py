# sorting linked list and removing duplicate element

class Node():
    def __init__(self,data):
        self.data = data
        self.nextNode = None
class LinkedList():
    def __init__(self):
        self.size = 0
        self.head = None
    def insertAtStart(self,data):
        node = Node(data)
        currentNode = self.head
        if self.head is None:
            self.head = node
            return
        node.nextNode = currentNode
        self.head = node
    # def sort(self):
