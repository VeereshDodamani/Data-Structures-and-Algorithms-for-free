# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Leetcode probelm: 22

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = [], []

        def backtrack(openn, close):
            if len(sol) == 2 * n:
                ans.append(''.join(sol))
                return

            if openn < n:
                sol.append('(')
                backtrack(openn + 1, close)
                sol.pop()

            if close < openn:
                sol.append(')')
                backtrack(openn, close + 1)
                sol.pop()

        backtrack(0, 0)
        return ans
