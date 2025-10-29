# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

#Leetcode problem : 1448
# Leetcode solution

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        stk = [(root, float('-inf'))]

        while stk:
            node, largest = stk.pop()

            if largest <= node.val:
                good_nodes += 1

            largest = max(largest, node.val)

            if node.right: stk.append((node.right, largest))
            if node.left: stk.append((node.left, largest))

        return good_nodes
