# check palindrome using linked list

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
    def insertAtStart(self,data):
        # print('inside 1')
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        node.next = current
        self.head = node
    def display(self):
        # print('inside 2')
        if self.head is None:
            print('List is Empty')
            return
        current = self.head
        while current is not None:
            print('Data : ',current.data)
            current = current.next
    def checkPalindrome(self):
        palin = []
        current = self.head
        while current is not None:
            palin.append(f'{current.data}')
            current = current.next
        check = ''.join(palin)
        if check == check[::-1]:
            print('Palindrome')
        else:
            print('Not palindrome')
            
link = LinkedList()
link.insertAtStart(1)
link.insertAtStart(2)
link.insertAtStart(3)
link.display()
link.checkPalindrome()
