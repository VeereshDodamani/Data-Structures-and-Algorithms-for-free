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
