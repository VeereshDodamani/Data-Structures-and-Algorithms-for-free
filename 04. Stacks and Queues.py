# Stacks: Last In First Out
print("STACK")
stk = []
print(f"Initial stack: {stk}")

# Append to top of stack: O(1)
stk.append(1)
stk.append(2)
stk.append(3)
print(f"After appending: {stk}")

# Poping a element: O(1)
stk.pop()
print(f"Ater poping: {stk}")

# To check what is on top of stack: O(1)
print(f"Latest emelemt: {stk[-1]}")

# Check stack is empty: O(1)
if stk:
    print(f"Stack elements: {stk}")
else:
    print(f"Empty stack: {stk}")
print("\n")

# Queues: First In First Out
print("QUEUES")
from collections import deque
q = deque()
# deque: Double ended queue
print(q)

# Enqueue a element on the right: O(1)
q.append(5)
q.append(6)
q.append(7)
q.append(8)
print(f"After Enqueuing: {q}")

# Dequeue a element from left: O(1)
q.popleft()
print(f"After Dequeuing: {q}")

# Peek from left side: O(1)
print(f"Leftmost element: {q[0]}")

# Peek from right side: O(1)
print(f"Leftmost element: {q[-1]}")
