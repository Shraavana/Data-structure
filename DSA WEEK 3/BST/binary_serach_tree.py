class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, data):
        current = self.root
        while current is not None:
            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                return True
        return False
    
    def remove(self, data):
        self.root = self.removeHelper(data, self.root)
    
    def removeHelper(self, data, current):
        if current is None:
            return current
        if data < current.data:
            current.left = self.removeHelper(data, current.left)
        elif data > current.data:
            current.right = self.removeHelper(data, current.right)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            current.data = self.getMinValue(current.right)
            current.right = self.removeHelper(current.data, current.right)
        return current

    def getMinValue(self, current):
        while current.left is not None:
            current = current.left
        return current.data
    
    def inOrder(self):
        self.inOrderHelper(self.root)
        print()  # for a new line after printing all elements
    
    def inOrderHelper(self, current):
        if current is not None:
            self.inOrderHelper(current.left)
            print(current.data, end=' ')
            self.inOrderHelper(current.right)

    def preOrder(self):
        self.preOrderHelper(self.root)
        print()  # for a new line after printing all elements
    
    def preOrderHelper(self, current):
        if current is not None:
            print(current.data, end=' ')
            self.preOrderHelper(current.left)
            self.preOrderHelper(current.right)

    def postOrder(self):
        self.postOrderHelper(self.root)
        print()  # for a new line after printing all elements
    
    def postOrderHelper(self, current):
        if current is not None:
            self.postOrderHelper(current.left)
            self.postOrderHelper(current.right)
            print(current.data, end=' ')

# Test the BinarySearchTree class
bst = BinarySearchTree()
bst.insert(10)
bst.insert(8)
bst.insert(12)
bst.insert(4)
bst.insert(9)

print("InOrder Traversal:")
bst.inOrder()  # Output should be: 4 8 9 10 12

print("PreOrder Traversal:")
bst.preOrder()  # Output should be: 10 8 4 9 12

print("PostOrder Traversal:")
bst.postOrder()  # Output should be: 4 9 8 12 10

# Testing removal
print("Removing 8...")
bst.remove(8)
print("InOrder Traversal after removing 8:")
bst.inOrder()  # Output should be: 4 9 10 12
