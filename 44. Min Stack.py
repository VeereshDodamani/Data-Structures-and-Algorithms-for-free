# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


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
    print("Current min:", min_stack.getMin()) 
    min_stack.push(2)
    min_stack.push(1)
    print("Current min:", min_stack.getMin()) 
    min_stack.pop()
    print("Current min after pop:", min_stack.getMin()) 
    print("Top element:", min_stack.top())
    min_stack.pop()
    print("Top element after popping:", min_stack.top())
    print("Current min:", min_stack.getMin())
