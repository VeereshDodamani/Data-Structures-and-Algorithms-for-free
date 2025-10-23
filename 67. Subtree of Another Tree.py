# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
# Leetcode probelm: 572

# Leetcode solution
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p,q):
            if not p and not q:
                return True

            if (p and not q) or (q and not p):
                return False

            if p.val != q.val:
                return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        def has_subTree(root):
            if not root:
                return False
            
            if sameTree(root, subRoot):
                return True
            return has_subTree(root.left) or has_subTree(root.right)
        
        return has_subTree(root)
# VS Code solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def same(a, b):
    if not a and not b: return True
    if not a or not b or a.val != b.val: return False
    return same(a.left, b.left) and same(a.right, b.right)

def isSubtree(r, s):
    if not r: return False
    return same(r, s) or isSubtree(r.left, s) or isSubtree(r.right, s)

root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))

print(isSubtree(root, subRoot))
