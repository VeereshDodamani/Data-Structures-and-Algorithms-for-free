# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.
# Leetcode probelm: 77

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, sol = [], []

        def backtrack(x):
            if len(sol) == k:
                ans.append(sorted(sol[:]))
                return

            left = x
            still_need = k - len(sol)

            if left > still_need and x > 0:
                backtrack(x-1)

            if x > 0:
                sol.append(x)
                backtrack(x-1)
                sol.pop()

        backtrack(n)
        return ans
