# reverse of a linked list

class Node():
    def __init__(self,data):
        self.data = data
        self.nextNode = None
class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
    def insertAtStart(self,data):
        self.size += 1
        node = Node(data)
        currentNode = self.head
        if self.head is None:
            self.head = node
            return
        node.nextNode = currentNode
        self.head = node
        return
    def display(self):
        currentNode = self.head
        if self.head is None:
            print('List is Empty')
            return 
        while currentNode is not None:
            print('Data : ',currentNode.data)
            currentNode = currentNode.nextNode
    def reverse(self):
        if self.head is None:
            print('List is empty')
            return
        current = self.head
        prev = None
        while current is not None:
            nextNode = current.nextNode
            current.nextNode = prev
            prev = current
            current = nextNode
        self.head = prev
    
            
link = LinkedList()
link.insertAtStart(4)
link.insertAtStart(3)
link.insertAtStart(2)
link.insertAtStart(1)
link.display()
link.reverse()
link.display()