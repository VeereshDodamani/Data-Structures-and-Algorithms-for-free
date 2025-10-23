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
