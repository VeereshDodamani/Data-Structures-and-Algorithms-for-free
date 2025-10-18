# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Leetcode probelm: 104

# Leetcode solution
def maxDepth(self, root) -> int:
    if root is None:
        return 0
        
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)

    return 1+max(left,right)

root = [3,9,20,None,None,15,7]
print("Maximum Depth: ", maxDepth(root))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print("Maximum Depth of the Binary Tree:", sol.maxDepth(root))
