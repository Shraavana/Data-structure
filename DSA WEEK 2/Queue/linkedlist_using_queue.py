class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  
        
class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def Enqueue(self, item):
        newNode = Node(item)
        if self.rear == None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode 
            self.rear = newNode

    def Dequeue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if (self.front == None):
            self.rear = None

    def display(self):
        currentNode = self.front
        while currentNode!= None:
            print(currentNode.data, end=" ")
            currentNode = currentNode.next
        print() 


q = Queue()
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.display()  