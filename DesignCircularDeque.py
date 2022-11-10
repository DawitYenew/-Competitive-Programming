class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.front = self.rear = -1
        self.deque=[None for i in range(k)]

    def insertFront(self, value: int) -> bool:
        if (self.front == 0 and self.rear == self.k - 1) or (self.front == self.rear+1):
            return False
        elif self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
            self.deque[self.front] = value
        elif self.front == 0:
            self.front = self.k - 1
            self.deque[self.front] = value
        else:
            self.front -= 1
            self.deque[self.front] = value
        return True
        
    def insertLast(self, value: int) -> bool:
        if (self.front == 0 and self.rear == self.k - 1) or (self.front == self.rear + 1):
            return False
        elif self.rear == -1 and self.front == -1:
            self.front = 0
            self.rear = 0
            self.deque[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.k
            self.deque[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        if self.front == -1 and self.rear == -1:
            return False
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.front == self.k -1:
            self.front = 0
        else:
            self.front += 1
        return True

    def deleteLast(self) -> bool:
        if self.front == -1 and self.rear == -1:
            return False
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.rear == 0:
            self.rear = self.k -1
        else:
            self.rear -= 1
        return True

    def getFront(self) -> int:
        if self.front == -1 and self.rear == -1:
            return -1
        else:
            return self.deque[self.front]

    def getRear(self) -> int:
        if self.front == -1 and self.rear == -1:
            return -1
        else:
            return self.deque[self.rear]
        
    def isEmpty(self) -> bool:
        if self.front == -1 and self.rear == -1:
            return True
        else:
            return False
        
    def isFull(self) -> bool:
        if (self.front == 0 and self.rear == self.k - 1) or (self.front == self.rear + 1):
            return True
        else:
            return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
