# Given the root of a binary tree, invert the tree, and return its root.

# Leetcode problem: 226

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root is None:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

root = TreeNode(4,
                TreeNode(2, TreeNode(1), TreeNode(3)),
                TreeNode(7, TreeNode(6), TreeNode(9)))

print("Original tree inorder:", inorder(root))

inverted_root = invertTree(root)
print("Inverted tree inorder:", inorder(inverted_root))
