class MinStack:

    def __init__(self):
        self.lst = []
        self.minimum = [float('inf')]

    def push(self, val: int) -> None:
        self.lst.append(val)
        self.minimum.append(min(self.minimum[-1], val))

    def pop(self) -> None:
        self.lst.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
        
