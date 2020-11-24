# Delete the elements in a linked list whose sum is zero
class Node():
    def __init__(self,data):
        self.data = data
        self.nextNode = None

class LinkedList():
    def __init__(self):
        self.size = 0
        self.head = None

    
    # inserting at start of linked list 
    def insertAtStart(self,data):
        node = Node(data)
        self.size+=1
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        node.nextNode = currentNode
        self.head = node

    # deleting elements with sum zero
    def deleteZeroSum(self):
        found = False
        # checking if list is empty
        if self.head is None:
            print("List is empty")
            return
        firstNode = self.head
        secondNode = None
        previousFirstNode = None
        previousSecondNode = None
        # checking if list contains only one node
        if firstNode.nextNode is None:
            print('Not enough Length')
            return
        initialData = 0
        # looping over every element and finding a match
        # first secondNode will loop over list and check after that firstNode will
        # total iterations will be Σ(self.size - 1)
        while firstNode is not None and not found:
            # second node is always a node ahead of firstNode
            secondNode = firstNode.nextNode

            while secondNode is not None:
                initialData = firstNode.data + secondNode.data
                if initialData == 0:
                    print('Found Number')
                    self.size -= 2
                    found = True
                    if previousFirstNode is None:
                        self.head = firstNode.nextNode
                    else:
                        previousFirstNode.nextNode = firstNode.nextNode
                    previousSecondNode.nextNode = secondNode.nextNode
                    break
                if secondNode.nextNode is not None:
                    previousSecondNode = secondNode
                secondNode = secondNode.nextNode
            previousFirstNode = firstNode
            firstNode = firstNode.nextNode
        if not found:
            print('Not found')
    def display(self):
        currentNode = self.head
        while currentNode is not None:
            print("Data : ",currentNode.data)
            currentNode = currentNode.nextNode

link = LinkedList()
link.insertAtStart(-2)
link.insertAtStart(3)
link.insertAtStart(4)
link.insertAtStart(3)
link.insertAtStart(2)
link.display()
print(link.size)
link.deleteZeroSum()
link.display()
print(link.size)