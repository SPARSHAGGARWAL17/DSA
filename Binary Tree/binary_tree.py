# binary tree

class Node():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree():
    def __init__(self):
        self.head = None
        self.size = 0
    def insert(self,data):
        if not self.head:
            self.head = Node(data)
        else:
            self.insertNode(data,self.head)
    def insertNode(self,data,node):
        if data<node.data:
            if node.left:
                self.insertNode(data,node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insertNode(data,node.right)
            else:
                node.right = Node(data)
    
    def getMinValue(self):
        if self.root:
            return self._getMin(self.root)
    
    def _getMin(self,node):
        if node.left:
            return self._getMin(node.left)
        return node.data
    
    def getMaxValue(self):
        if self.root:
            return self._getMax(self.root)
    
    def _getMax(self,node):
        if node.right:
            return self._getMax(node.right)
        return node.data

    def traverse(self):
        if self.head:
            self._traverseInOrder(self.head)
    def _traverseInOrder(self,node):
        # print(f'node = {node.data}')
        if node.left:
            self._traverseInOrder(node.left)
        print(f'{node.data}',end=' ')

        if node.right:
            self._traverseInOrder(node.right)

bst = BinaryTree()
bst.insert(10)
bst.insert(8)
bst.insert(12)
bst.insert(9)
bst.insert(6)
bst.insert(11)
bst.insert(14)
bst.traverse()