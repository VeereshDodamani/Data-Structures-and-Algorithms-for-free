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
