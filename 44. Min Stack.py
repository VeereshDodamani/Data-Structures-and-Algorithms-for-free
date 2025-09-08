class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif self.min_stack[-1] < val:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        raise IndexError("Stack is empty")

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("Stack is empty")

if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(3)
    min_stack.push(5)
    print("Current min:", min_stack.getMin())  # Output: 3
    min_stack.push(2)
    min_stack.push(1)
    print("Current min:", min_stack.getMin())  # Output: 1
    min_stack.pop()
    print("Current min after pop:", min_stack.getMin())  # Output: 2
    print("Top element:", min_stack.top())  # Output: 2
    min_stack.pop()
    print("Top element after popping:", min_stack.top())  # Output: 5
    print("Current min:", min_stack.getMin())  # Output: 3
