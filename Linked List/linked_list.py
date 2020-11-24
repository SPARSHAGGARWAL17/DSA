class Node(object):
    def __init__(self,data):
        self.data = data
        self.nextNode = None

class LinkedList():
    def __init__(self):
        self.size = 0
        self.head = None
    def insertAtStart(self,data):
        node = Node(data)
        self.size = self.size+1
        currentNode = self.head
        if self.head is not None:
            print('after that')
            node.nextNode = currentNode
            self.head = node
        else:
            print('first time')
            self.head = node
    def insertAtIndex(self,data,index):
        node = Node(data)
        currentNode = self.head
        size = self.size
        previousNode = None
        i = 0
        if size<index+1:
            return
        elif index ==0:
            self.insertAtStart(data)
            return 
        elif index+1 == size:
            self.insertAtEnd(data)
            return
        while i!= index:
            previousNode = currentNode
            currentNode = currentNode.nextNode
            i+=1
        previousNode.nextNode = node
        node.nextNode = currentNode
        self.size+=1
    def insertAtEnd(self,data):
        node = Node(data)
        self.size+=1
        currentNode = self.head
        if currentNode is None:
            self.head = node
            return
        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode
        currentNode.nextNode = node
    def traverse(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode
    def getSize(self):
        return self.size
    def printAtIndex(self,index):
        currentNode = self.head
        size = self.size
        if currentNode is None:
            print('List is Empty')
            return 
        if index>=size:
            print('Invalid Index. Size of list is ',size)
            return
        i = 0
        while i!=index:
            currentNode = currentNode.nextNode
            i+=1
        print(f'Data at index {index} = {currentNode.data}')
    def remove(self,data):
        currentNode = self.head
        previousNode = None
        if currentNode is None:
            return
        while currentNode.data!=data:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        if currentNode.data == data:
            self.size -= 1
            previousNode.nextNode = currentNode.nextNode
        else:
            print(f'{data} not found.')


if __name__=='__main__':
    link = LinkedList()
    while True:
        print('Select Options:')
        choice = int(input(' 1. Insert At Start \n 2. Insert At End \n 3. Display \n 4. Remove \n 5. Insert at Index \n 6. Exit \n :'))
        if choice == 1:
            data = int(input('Enter Data to insert at start : '))
            link.insertAtStart(data)
        elif choice == 2:
            data = int(input('Enter Data to insert at end : '))
            link.insertAtEnd(data)
        elif choice == 3:
            print('Data :')
            link.traverse()
        elif choice == 4:
            data = int(input('Enter Data to remove : '))
            link.remove(data)
        elif choice ==5 :
            index = int(input('Enter index to insert : '))
            data = int(input('Enter data to insert : '))
            link.insertAtIndex(data,index)
        else:
            break

