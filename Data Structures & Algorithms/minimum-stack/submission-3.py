class MinStack:

    def __init__(self):
        self.minStack = []
        self.mainStack = []
        

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append(val)
            self.mainStack.append(val)
            return
        self.minStack.append(min(self.minStack[-1], val))
        self.mainStack.append(val)
        
    def pop(self) -> None:
        self.minStack.pop()
        self.mainStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
