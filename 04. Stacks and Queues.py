# Stacks: Last In First Out

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
