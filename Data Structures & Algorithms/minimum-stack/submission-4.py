class MinStack:

    def __init__(self):
        self.minStack = []
        self.mainStack = []
        

    def push(self, val: int) -> None:
        smaller = val if not self.minStack else min(self.minStack[-1], val)
        self.minStack.append(smaller)
        self.mainStack.append(val)
        
    def pop(self) -> None:
        self.minStack.pop()
        self.mainStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
