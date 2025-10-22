# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# leetcode problem : 101

# Leetcode solution
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def same(root1, root2):
            if not root1 and not root2:
                return True
            
            if not root1 or not root2:
                return False

            if root1.val != root2.val:
                return False

            return same(root1.left, root2.right) and same(root1.right, root2.left)
        
        return same(root, root)
    
root = [1,2,2,3,4,4,3]

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# leetcode problem : 101


# VS Code solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def isSymmetric(self, root):
        def same(a, b):
            return not a and not b or (a and b and a.val == b.val and same(a.left, b.right) and same(a.right, b.left))
        return same(root, root)

def build(vals):
    n = [TreeNode(v) if v is not None else None for v in vals]
    for i in range(len(n)):
        if n[i]:
            l, r = 2*i+1, 2*i+2
            if l < len(n): n[i].left = n[l]
            if r < len(n): n[i].right = n[r]
    return n[0]

root = build([1, 2, 2, 3, 4, 4, 3])
print("Is Symmetric: ",Solution().isSymmetric(root))
