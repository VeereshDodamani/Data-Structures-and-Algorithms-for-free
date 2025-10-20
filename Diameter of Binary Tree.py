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


# VS Code solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.res = 0
        def dfs(node):
            if not node: return 0
            l, r = dfs(node.left), dfs(node.right)
            self.res = max(self.res, l + r)
            return 1 + max(l, r)
        dfs(root)
        return self.res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Maximum Diameter of Binary Tree: ",Solution().diameterOfBinaryTree(root))
