class MinStack:

    def __init__(self):
        self.stack=[]
        self.curr_min=float('inf')

    def push(self, val: int) -> None:
        if val < self.curr_min:
            self.curr_min=val
        self.stack.append((val,self.curr_min))

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack)==0:
            self.curr_min=float('inf')
        else:
            self.curr_min=self.stack[-1][1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()