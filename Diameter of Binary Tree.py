# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.
# Leetcode probelm: 543

# Leetcode solution
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diameter = [0]

        def height(root):
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)
            diameter = left+right
            largest_diameter[0] = max(diameter, largest_diameter[0])

            return 1+max(left,right)
        
        height(root)
        return largest_diameter[0]
