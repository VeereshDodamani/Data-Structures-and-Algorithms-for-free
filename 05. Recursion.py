# Fibonacci
# F(0) = 0
# F(1) = 1
# F(2) = 2
# n>1; F(n)=(n-1)+(n-2)

# Time: O(2^n)
# Space: O(n)
def F(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return F(n-1) +F(n-2)

print(F(5))

# Linked list

# Time: O(n)
# Space: O(n)
class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(5)
C = SinglyNode(2)

Head.next = A
A.next = B
B.next = C
def reverse(node):
    if not node:
        return
    
    reverse(node.next)
    print(node)

print("Given linked list in reverse:")
reverse(Head)
