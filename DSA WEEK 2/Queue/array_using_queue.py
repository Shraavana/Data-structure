class Queue:
    def __init__(self,c):
        self.queue=[]
        self.front=self.rear=0
        self.capacity=c
    def  Enqueue(self,data):
        if (self.capacity==self.rear):
            print("\n Queue is full")
        else:
            self.queue.append(data)
            self.rear += 1
    def Dequeue(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            x = self.queue.pop(0)
            self.rear-=1
    def display(self):
        if self.front==self.rear:
            print("\n queue is empty")
        for i in self.queue:
            print(i,"<--",end=" ")
    def peek(self):
        if self.front == self.rear:
            print("\n queue is empty")
            print("\n front element is :")
            self.queue[self.front]
q=Queue(4)
q.display()
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.display()