# Given a binary tree, determine if it is height-balanced.
# Leetcode problme: 110


# Leetcode solution
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    balanced = [True]

    def height(root):
        if not root:
            return 0
        
        left = height(root.left)
        right = height(root.right)

        if abs(left-right) > 1:
            balanced[0] = False
            return 0

        return 1+max(left,right)
    
    height(root)
    return balanced[0]

# VS code solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    if not root:
        return True

    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return height(root) != -1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print("Given root is balanced: ",isBalanced(root))
