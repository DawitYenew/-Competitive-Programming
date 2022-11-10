class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = 999999999999
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(self.minimum, val)
        

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp == self.minimum:
            if self.stack:
                self.minimum  = min(self.stack)
            else:
                self.minimum = 999999999999

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.stack:
            return self.minimum
        else:
            return None

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
