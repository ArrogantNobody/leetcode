class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if not self.stack2 or x <= self.getMin():
            self.stack2.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.getMin():
            self.stack2.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack2[-1]