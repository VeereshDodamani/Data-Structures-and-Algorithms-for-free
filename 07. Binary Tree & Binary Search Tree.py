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
def in_order(node):
    if not node:
        return
    
    in_order(node.left)
    print(node)
    in_order(node.right)

in_order(A)

# Recursive Post-order traversal (DFS)
# Time: O(n)
# Space: O(n)
print("Recursive Post-order traversal")
def post_order(node):
    if not node:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node)

post_order(A)

# Itreative Post-order/In-order/Post-order traversal (DFS)
print("Itreative Post-order traversal")
def iterative_pre_order(node):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)
iterative_pre_order(A)

# Level order traversal (BFS)
print("Level order traversal")
from collections import deque

def level_order(node):
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        print(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
level_order(A)

# Search for a value (DFS)
# Time: O(n)
# Value: O(n)
print("Searching a node using DFS")
def search(node, target):
    if not node:
        return False
    if node.val == target:
        return f"Target: {target} present in tree"
    
    return search(node.left, target) or search(node.right, target)

print(search(A,10))
