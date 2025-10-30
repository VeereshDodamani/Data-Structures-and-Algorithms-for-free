# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

# Leetcode probelm : 112
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def has_sum(root, cur_sum):
            if not root:
                return False

            cur_sum += root.val
            if not root.left and not root.right:
                return cur_sum == targetSum
            
            return has_sum(root.left, cur_sum) or has_sum(root.right, cur_sum)
            
        return has_sum(root, 0)
