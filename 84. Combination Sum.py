# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinationsof candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Leetcode probelm: 39
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)

        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return
            
            if cur_sum > target or i == n:
                return
            
            backtrack(i+1, cur_sum)

            sol.append(candidates[i])
            backtrack(i, cur_sum+candidates[i])
            sol.pop()
        
        backtrack(0, 0)
        return res
