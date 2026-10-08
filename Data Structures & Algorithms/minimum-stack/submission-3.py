class MinStack:

    def __init__(self):
        self.contents = []
        

    def push(self, val: int) -> None:
        self.contents.append(val)

        

    def pop(self) -> None:
        return self.contents.pop()
        

    def top(self) -> int:
        return self.contents[-1]
        

    def getMin(self) -> int:
        return min(self.contents)
        
