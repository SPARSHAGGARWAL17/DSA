# Delete middle of linked list 
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
        self.size +=1
        if self.head is None:
            self.head = node
            return
        node.nextNode = currentNode
        self.head = node
    def deleteAtMiddle(self):
        currentNode = self.head
        if self.head is None:
            print('list is empty')
            return
        previousNode = None
        i = 0
        while i < self.size//2:
            previousNode = currentNode
            currentNode = currentNode.nextNode
            i+=1
        previousNode.nextNode = currentNode.nextNode
    def display(self):
        currentNode = self.head
        if self.head is None:
            print("List is empty")
            return
        while currentNode is not None:
            print("Data : ",currentNode.data)
            currentNode = currentNode.nextNode
link = LinkedList()
link.insertAtStart(1)
link.insertAtStart(2)
link.insertAtStart(3)
link.insertAtStart(4)
link.insertAtStart(5)
print('BEFORE DELETING')
link.display()
link.deleteAtMiddle()
print('AFTER DELETING')
link.display()
        