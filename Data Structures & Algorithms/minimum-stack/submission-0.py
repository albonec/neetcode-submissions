class MinStack:
    def __init__(self):
        self.contents = []
        
    def push(self, val: int) -> None:
        if self.contents:
            current_min = min(val, self.contents[-1][1])
        else:
            current_min = val
        
        self.contents.append((val, current_min))

    def pop(self) -> None:
        self.contents.pop()

    def top(self) -> int:
        return self.contents[-1][0]
        
    def getMin(self) -> int:
        return self.contents[-1][1]
        
