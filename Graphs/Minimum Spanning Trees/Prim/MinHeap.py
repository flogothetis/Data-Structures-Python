class MinHeap:
    def __init__(self, maxSize):
        self.heap = [[0, 0]] * maxSize
        self.heapSize = maxSize
        self.size = 0
        self.pos = [0] * maxSize

    def leftChild(self, pos):
        return 2 * pos

    def isInMinHeap(self, v):
        if (self.pos[v] < self.size):
            return True
        return False

    def rightChild(self, pos):
        return (2 * pos) + 1

    def parent(self, pos):
        return pos // 2

    def swap(self, pos1, pos2):
        # Swap values and position of elements
        temp_pos = self.pos[self.heap[pos2][0]]
        self.pos[self.heap[pos2][0]] = self.pos[self.heap[pos1][0]]
        self.pos[self.heap[pos1][0]] = temp_pos

        temp = self.heap[pos2]
        self.heap[pos2] = self.heap[pos1]
        self.heap[pos1] = temp

    def insertWithoutHeaping(self, id, key):
        if (self.size == self.heapSize):
            return None

        self.heap[self.size] = [id, key]
        self.pos[id] = self.size
        self.size += 1

    def isLeaf(self, pos):
        if (pos >= self.size // 2 and pos < self.size):
            return True
        return False

    def getMin(self):
        return self.heap[0]

    def heapify(self, pos):
        if self.isLeaf(pos) == False and self.size > 0:
            left = self.leftChild(pos)
            right = self.rightChild(pos)
            # Check if a child value is greater than its parent
            # If it happens then swap parent with its child.

            if (self.heap[left][1] < self.heap[pos][1] or
                    self.heap[right][1] < self.heap[pos][1]):
                if self.heap[left][1] < self.heap[pos][1]:
                    self.swap(left, pos)
                    self.heapify(left)
                else:
                    self.swap(right, pos)
                    self.heapify(right)

    def decreaseKey(self, v, dist):
        pos = self.pos[v]
        self.heap[pos][1] = dist

        while (pos > 0 and self.heap[pos][1] < self.heap[self.parent(pos)][1]):
            self.swap(pos, self.parent(pos))
            pos = self.parent(pos)

    def isEmpty(self):
        if (self.size == 0):
            return True
        return False

    def extractMin(self):
        min = self.getMin()
        self.swap(0, self.size - 1)
        self.size -= 1
        self.heapify(0)
        return min
