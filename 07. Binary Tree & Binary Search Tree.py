# Binary Tree
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F


# Recursive Pre-order traversal (DFS)
# Time: O(n)
# Space: O(n)
print("Recursive Pre-order traversal")
def pre_order(node):
    if not node:
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)

pre_order(A)

# Recursive In-order traversal (DFS)
# Time: O(n)
# Space: O(n)
print("Recursive In-order traversal")
def pre_order(node):
    if not node:
        return
    
    pre_order(node.left)
    print(node)
    pre_order(node.right)

pre_order(A)

# Recursive Post-order traversal (DFS)
# Time: O(n)
# Space: O(n)
print("Recursive Post-order traversal")
def pre_order(node):
    if not node:
        return
    
    pre_order(node.left)
    pre_order(node.right)
    print(node)

pre_order(A)
