# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Leetcode probelm: 104

def maxDepth(self, root) -> int:
    if root is None:
        return 0
        
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)

    return 1+max(left,right)
    

root = [3,9,20,null,null,15,7]
print("Given Tree: ", root)
print("Maximum Depth: ", maxDepth)
