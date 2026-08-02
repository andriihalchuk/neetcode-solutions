class MinStack:

    def __init__(self):
        self.stack = []
        self.auxStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.auxStack.append(min(val, self.auxStack[-1] if self.auxStack else val))

    def pop(self) -> None:
        self.stack.pop()
        self.auxStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.auxStack[-1]
