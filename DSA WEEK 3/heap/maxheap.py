class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def max_heap(self, arr):
        self.heap = arr[:]
        self.buildMaxHeap()

    def buildMaxHeap(self):
        size = len(self.heap)
        for i in range(self.parent(size - 1), -1, -1):
            self.shiftDown(i)
        
    def shiftUp(self, currentIdx):
        parentIdx = self.parent(currentIdx)
        while currentIdx > 0 and self.heap[parentIdx] < self.heap[currentIdx]:
            self.heap[parentIdx], self.heap[currentIdx] = self.heap[currentIdx], self.heap[parentIdx]
            currentIdx = parentIdx
            parentIdx = self.parent(currentIdx)

    def shiftDown(self, currentIdx):
        size = len(self.heap)
        endIdx = size - 1
        leftIdx = self.leftChild(currentIdx)
        while leftIdx <= endIdx:
            rightIdx = self.rightChild(currentIdx)
            if rightIdx <= endIdx and self.heap[rightIdx] > self.heap[leftIdx]:
                idxToShift = rightIdx
            else:
                idxToShift = leftIdx
            if self.heap[idxToShift] > self.heap[currentIdx]:
                self.heap[idxToShift], self.heap[currentIdx] = self.heap[currentIdx], self.heap[idxToShift]
                currentIdx = idxToShift
                leftIdx = self.leftChild(currentIdx)
            else:
                return
            
    def insert(self, value):
        self.heap.append(value)
        self.shiftUp(len(self.heap) - 1)

    def remove(self):
        size = len(self.heap)
        if size == 0:
            return None
        self.heap[0], self.heap[size - 1] = self.heap[size - 1], self.heap[0]
        max_value = self.heap.pop()
        self.shiftDown(0)
        return max_value
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def display(self):
        print(self.heap)

    def parent(self, i):
        return (i - 1) // 2
    
    def leftChild(self, i):
        return 2 * i + 1
    
    def rightChild(self, i):
        return 2 * i + 2
    

# Test the MaxHeap class
max_heap = MaxHeap()
max_heap.max_heap([6, 2, 8])
max_heap.display()
max_heap.insert(15)
max_heap.insert(5)
max_heap.insert(4)
max_heap.display()
max_heap.remove()
max_heap.display()
