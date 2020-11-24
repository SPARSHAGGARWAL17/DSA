class Node():
    def __init__(self,data):
        self.previousNode = None
        self.data = data
        self.nextNode = None
class DoubleLinkedList():
    def __init__(self):
        self.size = 0
        self.head = None
    def insertAtStart(self,data):
        node = Node(data)
        self.size+=1
        if self.head is None:
            self.head = node
        else:
            currentNode = self.head
            node.nextNode = currentNode
            currentNode.previousNode = node
            self.head = node
    def insertAtEnd(self,data):
        node = Node(data)
        self.size +=1 
        if self.head is None:
            self.head = node
        else:
            currentNode = self.head
            while currentNode.nextNode is not None:
                currentNode = currentNode.nextNode
            currentNode.nextNode = node
            node.previousNode = currentNode
    def removeAtStart(self):
        self.size-=1
        currentNode = self.head
        self.head = currentNode.nextNode
        self.head.previousNode = None
    def removeAtEnd(self):
        self.size-=1
        currentNode = self.head
        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode
        currentNode = currentNode.previousNode
        currentNode.nextNode = None
    def display(self):
        if self.head is None:
            print('List is Empty')
            return 
        else:
            currentNode = self.head
            while currentNode is not None:
                print(f'data : {currentNode.data}\nprevious node :{currentNode.previousNode }\nnext node : {currentNode.nextNode}')
                currentNode = currentNode.nextNode

dll = DoubleLinkedList()
dll.insertAtEnd(23)
dll.insertAtStart(34)
dll.insertAtStart(4)
dll.removeAtStart()
dll.display()
