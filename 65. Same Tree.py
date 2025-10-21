# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
# Leetcode probelm: 100

# Leetcode solution
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def balanced(p,q):
            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False
            
            if p.val != q.val:
                return False

            return balanced(p.left, q.left) and balanced(p.right, q.right)

        return balanced(p,q)

# VS Code solution
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def balanced(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return balanced(p.left, q.left) and balanced(p.right, q.right)

p = Node(1)
p.left = Node(2)
p.right = Node(3)

q = Node(1)
q.left = Node(2)
q.right = Node(3)

print("Given p and q tree are same: ",balanced(p, q))
