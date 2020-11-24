class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
class StackUsingNode():
    def __init__(self):
        self.size = 0
        self.head = None
    
    def push(self,data):
        node = Node(data)
        self.size +=1
        currentNode = self.head
        if currentNode is None:
            self.head = node
        else:
            while currentNode.nextNode is not None:
                currentNode = currentNode.nextNode
            currentNode.nextNode = node
    def pop(self):
        self.size-=1
        currentNode = self.head
        previousNode = None
        if self.head is None:
            print('Stack Underflow')
            return
        while currentNode.nextNode is not None:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        previousNode.nextNode = None
        print('\nPopped item : ',currentNode.data)
    def getSize(self):
        return self.size
    def display(self):
        currentNode = self.head
        while currentNode is not None:
            print(f'{currentNode.data} ',end=' ')
            currentNode = currentNode.nextNode
sn = StackUsingNode()
sn.push(23)
sn.push(34)
sn.push(4)
sn.display()
sn.pop()
sn.display()
class StackUsingList():
    def __init__(self):
        self.stack = []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if len(self.stack)==0:
            print('Stack Underflow')
            return
        popItem = self.stack.pop()
        print('Popped Item',popItem)
        del self.stack[-1]
    def display(self):
        for i in self.stack:
            print(i)
print('\nStack Using List')
sl = StackUsingList()
sl.push(23)
sl.push(34)
sl.push(2)
sl.display()
sl.pop()
sl.display()