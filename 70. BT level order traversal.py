# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# Leetcode probelm: 102

# Leetcode solution
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            ans.append(level)
        return ans
