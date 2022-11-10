class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        

    def push(self, x: int) -> None:
        self.stack_1.append(x)
        

    def pop(self) -> int:
        if self.stack_2:
            return self.stack_2.pop()
        else:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
            if self.stack_2:
                return self.stack_2.pop()
     

    def peek(self) -> int:
        if self.stack_2:
            return self.stack_2[-1]
        else:
            return self.stack_1[0]

    def empty(self) -> bool:
        return not self.stack_1 and not self.stack_2
           


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
