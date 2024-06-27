class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        #check to see if the length of the stack is equal to zero before checking the last value of the stack to avoid
        #an index out of bounds exception
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:  
            self.min_stack.append(val)
        
        self.stack.append(val)
        

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.min_stack and popped == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
        
