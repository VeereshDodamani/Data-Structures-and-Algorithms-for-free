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

# Binary Search Tree (BST)
A2 = TreeNode(5)
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 = TreeNode(7)
G2 = TreeNode(9)

A2.left, A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

# Can use the same in-order on BST
print("In-order on Binary Search Tree")
in_order(A2)

# Time: O(log n)
# Space: O(log n)
print("Searching node in BST")
def search_bst(node, target):
    if not node:
        return f"Target {target} not present in BST"
    
    if node.val == target:
        return f"Target {target} present in BST"
    
    if target<node.val:
        return search_bst(node.left, target)
    if target>node.val:
        return search_bst(node.right, target)

print(search_bst(A2,10))
