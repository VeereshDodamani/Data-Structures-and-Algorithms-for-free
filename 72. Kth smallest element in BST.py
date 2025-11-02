# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
# Leetcode problem: 230

# WAY: 1
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [k]
        ans = [0]

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            count[0] -= 1

            if count[0] == 0:
                ans[0] = node.val
                return
            
            dfs(node.right)

        dfs(root)
        return ans[0]

# WAY: 2
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [k]
        ans = [0]

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            count[0] -= 1
            if count[0] == 0:
                ans[0] = node.val
                
            if count[0] > 0:
                dfs(node.right)

        dfs(root)
        return ans[0]
