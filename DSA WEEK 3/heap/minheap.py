class MinHeap:
    def __init__(self):
        self.heap = []

    def min_heap(self, arr):
        self.heap = arr[:]
        self.buildMinHeap()

    def buildMinHeap(self):
        size = len(self.heap)
        for i in range(self.parent(size - 1), -1, -1):
            self.shiftDown(i)

    def shiftUp(self, currentIdx):
        parentIdx = self.parent(currentIdx)
        while currentIdx > 0 and self.heap[currentIdx] < self.heap[parentIdx]:
            self.heap[currentIdx], self.heap[parentIdx] = self.heap[parentIdx], self.heap[currentIdx]
            currentIdx = parentIdx
            parentIdx = self.parent(currentIdx)

    def shiftDown(self, currentIdx):
        endIdx = len(self.heap) - 1
        leftIdx = self.leftChild(currentIdx)
        while leftIdx <= endIdx:
            rightIdx = self.rightChild(currentIdx)
            if rightIdx <= endIdx and self.heap[rightIdx] < self.heap[leftIdx]:
                idxToShift = rightIdx
            else:
                idxToShift = leftIdx
            if self.heap[idxToShift] < self.heap[currentIdx]:
                self.heap[currentIdx], self.heap[idxToShift] = self.heap[idxToShift], self.heap[currentIdx]
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
        removed_value = self.heap.pop()
        self.shiftDown(0)
        return removed_value

    def peak(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def display(self):
        print(self.heap)

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

# Example usage:
m = MinHeap()
m.min_heap([10, 8, 6])
m.display()  # Output: [6, 8, 10]
m.insert(9)
m.insert(12)
m.display()  # Output: [6, 8, 10, 9, 12]
m.remove()
m.display()  # Output: [8, 9, 10, 12]
