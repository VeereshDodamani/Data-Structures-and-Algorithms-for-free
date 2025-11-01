# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
#Leetcode probelm: 367

# WAY 1
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avgs = []
        q = deque([root])

        while q:
            total = 0
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                total += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            avgs.append(total / n)
        return avgs
    
#WAY 2
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []

        avgs = []
        q = deque([root])
        avg = 0

        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                avg += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            avg /= n
            avgs.append(avg)
            avg = 0
        return avgs
    
# WAY 3
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []

        avgs = []
        q = deque([root])

        while q:
            avg = 0
            n = len(q)
            avg /= n
            for _ in range(n):
                node = q.popleft()
                avg += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            avgs.append(avg)
        return avgs
